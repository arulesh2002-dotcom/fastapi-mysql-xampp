# 🚀 FastAPI + MySQL (XAMPP) API Project

A beginner-friendly FastAPI project that connects to a **MySQL database** running locally via **XAMPP**.  
This project demonstrates how to build and structure a simple CRUD API with **connection pooling**, **environment variables**, and **clean modular design**.

---

## 🧱 Project Structure

```
📦 fastapi-mysql-xampp
├── main.py              # FastAPI entry point (endpoints and app startup)
├── database.py          # Database connection pool and table initialization
├── config.py            # Loads environment variables (from .env)
├── requirements.txt     # All project dependencies
└── .env                 # MySQL credentials (NOT uploaded to GitHub)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/fastapi-mysql-xampp.git
cd fastapi-mysql-xampp
```

### 2️⃣ Create a virtual environment
```bash
python -m venv env
# Activate it:
# Windows:
env\Scripts\activate
# macOS / Linux:
source env/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a file named **`.env`** in the root folder and add your MySQL credentials:

```bash
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_DB=your_database
```

💡 **Note:**  
- The `.env` file is intentionally excluded from GitHub using `.gitignore`.  
- You can find these credentials in your **XAMPP/phpMyAdmin** setup.

---

## 🧩 Start XAMPP MySQL Server

1. Open XAMPP Control Panel.  
2. Start **MySQL** service.  
3. Make sure your database (`your_database`) exists in **phpMyAdmin**.

---

## 🚀 Run the FastAPI App

Start your server using Uvicorn:

```bash
uvicorn main:app --reload
```

Then open your browser and visit:

📄 Swagger Docs → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
🧾 ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧠 Example API Usage

### ➕ Create a User
**POST** `/users/`

Request body:
```json
{
  "name": "Attractor",
  "age": 25
}
```

Response:
```json
{
  "id": 1,
  "name": "Attractor",
  "age": 25
}
```

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|----------|
| **FastAPI** | Modern Python web framework |
| **Uvicorn** | ASGI server for FastAPI |
| **MySQL Connector** | Connects Python to MySQL |
| **python-dotenv** | Loads `.env` environment variables |
| **XAMPP** | Local MySQL + phpMyAdmin server |

---

## 🧾 Features

✅ MySQL connection pooling using `mysql.connector.pooling`  
✅ Environment variable management via `.env`  
✅ CRUD-ready structure  
✅ Automatic table initialization at startup  
✅ Swagger UI (`/docs`) for interactive testing  

---

## 🧱 Future Improvements

- Add full CRUD endpoints (read, update, delete)
- Switch to **SQLAlchemy ORM** for cleaner queries
- Add **Alembic** for database migrations
- Implement error handling and validation middleware
- Dockerize for easy deployment

---

## ⚠️ Important Notes

- Do **NOT** upload your `.env` file (it contains sensitive credentials).
- Always close database connections properly.
- Use **async drivers** like `aiomysql` for high-concurrency production systems.

---


