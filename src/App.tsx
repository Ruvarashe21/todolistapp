import { Routes, Route } from "react-router-dom";
import Home from "./home.tsx";
import Todo from "./todo.tsx";
import Login from "./login.tsx";
import Register from "./register.tsx";
import Protected from "./protected.tsx";


function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/protected" element={<Protected />} />
      <Route path="/home" element={<Home />} />
      <Route path="/todo" element={<Todo />} />
    </Routes>
  );
}

export default App;