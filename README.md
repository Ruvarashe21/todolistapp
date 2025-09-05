Todo app

A beginner-friendly full-stack authentication project using **FastAPI** and **React + TypeScript**. Users can register, log in, access protected content, and log out — all powered by JWT tokens and a real database.

---

 TECH

- Backend: FastAPI, Python, SQLAlchemy, JWT
- Frontend: React 18+, TypeScript, Axios, React Router
- Database: SQLite (or PostgreSQL)



sSFEATURES

- User registration and login
- JWT-based authentication
- Protected route access
- Logout and token clearing
- Loading states and error messages
- Responsive design with minimal styling



SETUP

 BACKEND

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python main.py

FRONTEND
cd frontend
npm install
npm run dev

HOW TO RUN THE APP LOCALLY

1. Clone the Repository

```bash
git clone https://github.com/Ruvarashe21/todolistapp.git
cd todolistapp

2.Test the App
 Visit http://localhost:3000
 Register a new user
 Log in and access the protected page
 Log out and try accessing the protected page again — it should redirect to login


