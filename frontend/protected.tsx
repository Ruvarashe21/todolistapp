import { useEffect, useState } from "react";
import api from "./api";
import { useNavigate } from "react-router-dom";


function Protected() {
  const [message, setMessage] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(true);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login");
      return;
    }

    api.get("/protected", {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then(res => {
      setMessage((res.data as { message: string }).message);
      setLoading(false);
    })
    .catch(() => {
      localStorage.removeItem("token");
      navigate("/login");
      setLoading(false);
    });
  }, []);

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <div>
      {loading ? (
        <div className="spinner">Loading...</div>
      ) : (
        <>
          <h2>{message}</h2>
          <button onClick={logout}>Logout</button>
        </>
      )}
    </div>
  );
}

export default Protected;