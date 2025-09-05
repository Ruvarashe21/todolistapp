##Todo app

A beginner-friendly full-stack authentication project using **FastAPI** and **React + TypeScript**. Users can register, log in, access protected content, and log out — all powered by JWT tokens and a real database.

---

 TECH

- Backend: FastAPI, Python, SQLAlchemy, JWT
- Frontend: React 18+, TypeScript, Axios, React Router
- Database: SQLite (or PostgreSQL)



## FEATURES

- User registration and login
- JWT-based authentication
- Protected route access
- Logout and token clearing
- Loading states and error messages
- Responsive design with minimal styling



 ##SETUP

 BACKEND

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

FRONTEND
cd frontend
npm install
npm start
