
# ChatBot with RAG using FastAPI + Aval AI

یک چت‌بات ساده و کاربردی بر پایه معماری RAG (Retrieval-Augmented Generation) که با استفاده از FastAPI و مدل GPT-4.1-mini از Aval AI پیاده‌سازی شده است.

## ویژگی‌ها

- استفاده از **FastAPI** برای ساخت REST API
- یکپارچه‌سازی با مدل GPT از Aval AI برای تولید پاسخ
- استفاده از **SentenceTransformer** و **FAISS** برای بازیابی نزدیک‌ترین پاسخ‌ها از دیتاست
- پشتیبانی از دو دیتاست: 
  - داده‌های عمومی (dataset.json)
  - سوالات پرتکرار (FAQ)

---

## پیش‌نیازها

```bash
pip install fastapi uvicorn requests numpy faiss-cpu sentence-transformers
```

---

## اجرا

برای اجرای برنامه:

```bash
uvicorn main:app --reload
```

در صورت موفقیت، API روی آدرس زیر در دسترس خواهد بود:

```
http://127.0.0.1:8000/chat
```

---

## ساختار فایل‌ها

- `main.py`: فایل اصلی اجرای FastAPI
- `dataset.json`: دیتاست عمومی
- `faq_clothing_store.json`: دیتاست سوالات پرتکرار
