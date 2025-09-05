import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:3001'
});

export const registerUser = (data: { email: string; password: string }) =>
  api.post("/register", data);

export const loginUser = (data: { email: string; password: string }) =>
  api.post("/login", data);

export const getTodos = (token: string) =>
  api.get("/todos", {
    headers: { Authorization: `Bearer ${token}` },
  });

export const createTodo = (token: string, text: string) =>
  api.post("/todos", { text }, {
    headers: { Authorization: `Bearer ${token}` },
  });

export const updateTodo = (token: string, id: number, text: string, completed: boolean) =>
  api.put(`/todos/${id}`, { text, completed }, {
    headers: { Authorization: `Bearer ${token}` },
  });

export const deleteTodo = (token: string, id: number) =>
  api.delete(`/todos/${id}`, {
    headers: { Authorization: `Bearer ${token}` },
  });

export default api;