import { useState } from "react";
import api from "./api";
import { useNavigate } from "react-router-dom";

function Register() {
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>("");
  const [success, setSuccess] = useState<string>("");
  const navigate = useNavigate();

  const handleRegister = async () => {
    setLoading(true);
    setError("");
    setSuccess("");
    try {
      await api.post("/register", { email, password });
      setSuccess("Registration successful! Please log in.");
      setTimeout(() => navigate("/login"), 1500);
    } catch (error: any) {
      console.error("Registration error:", error);
      if (error.response?.status === 409) {
        setError("User already exists. Try a different email.");
      } else {
        setError(`Registration failed: ${error.response?.data?.detail || error.message}`);
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="header">
        <h1>WELCOME</h1>
        <div className="toggle">
          <button onClick={() => navigate("/login")}>Login</button>
          <button className="active">Register</button>
        </div>
      </div>

      <div className="card">
        <h2>Register</h2>
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
        <button onClick={handleRegister}>Register</button>
        {loading && <div className="spinner">Loading...</div>}
        {error && <div className="error">{error}</div>}
        {success && <div className="success">{success}</div>}
      </div>
    </div>
  );
}

export default Register;