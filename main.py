from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

app = FastAPI()


API_KEY = 'aa-3sgBf8IxObkRyorUpVifD39z5yzQwBg78nwO9xqwSQdhCjDK'
BASE_URL = "https://api.avalai.ir/v1"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

MODEL_NAME = "gpt-4.1-mini"  

with open('faq_clothing_store.json','r',encoding='utf-8') as f :
    faq_dataset = json.load(f)

with open("dataset.json", "r", encoding="utf-8") as f:
    data_sentences = json.load(f)


model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

faq_question = [item['question'] for item in faq_dataset]
faq_answer = [item['answer'] for item in faq_dataset ]

faq_embedding = model.encode(faq_question).astype('float32')
faq_index = faiss.IndexFlatL2(faq_embedding.shape[1])
faq_index.add(faq_embedding)

embeddings = model.encode(data_sentences).astype("float32")
embedding_dim = embeddings.shape[1]
index = faiss.IndexFlatL2(embedding_dim)
index.add(embeddings)

class Query(BaseModel):
    question: str


def ask_llm(prompt):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(f"{BASE_URL}/chat/completions", headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"


@app.post("/chat")
def chat_endpoint(query: Query):
    user_question = query.question
    query_embedding = model.encode([user_question]).astype("float32")

    q = 1
    faq_distances , faq_indices = faq_index.search(query_embedding,q)
    if faq_distances[0][0] < 5:
        faq_response = faq_answer[faq_indices[0][0]]
        return {'answer':faq_response}

    k = 3
    distances, indices = index.search(query_embedding, k)
    retrieved = [data_sentences[i] for i in indices[0]]


    context = "\n".join(retrieved)
    final_prompt = f"""سؤال کاربر: {user_question}
پاسخ را با استفاده از اطلاعات زیر بده:
{context}
پاسخ:"""


    response = ask_llm(final_prompt)
    cleaned_response = response.replace("\\n", "<br>").replace("\n", "<br>")
    
    return {"answer": cleaned_response}
