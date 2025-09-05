import { useState } from "react";
import api from "./api";
import { useNavigate } from "react-router-dom";


function Login() {
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    setLoading(true);
    setError("");
    try {
      const res = await api.post("/login", { email, password });
      const data = res.data as { token: string };
      localStorage.setItem("token", data.token);
      navigate("/home");
    } catch {
      setError("Invalid credentials");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="header">
        <h1>WELCOME</h1>
        <div className="toggle">
          <button className="active">Login</button>
          <button onClick={() => navigate("/register")}>Register</button>
        </div>
      </div>

      <div className="card">
        <h2>Login</h2>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
        />
        <button onClick={handleLogin}>Login</button>
        {loading && <div className="spinner">Loading...</div>}
        {error && <div className="error">{error}</div>}
      </div>
    </div>
  );
}

export default Login;