import React from "react";
import { useNavigate } from "react-router-dom";

const Home: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', height: '100vh', width: '100%', backgroundColor: '#e0f7fa', padding: '20px' }}>
      <h1 style={{ fontSize: '3rem', color: '#333', marginBottom: '10px' }}>Welcome to your todo list</h1>
      <p style={{ fontSize: '1.2rem', color: '#666', marginBottom: '30px' }}>Manage your daily tasks with ease.</p>
      <div>
        <button onClick={() => navigate('/todo')} style={{ padding: '12px 24px', marginRight: '10px', cursor: 'pointer', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '5px', fontSize: '1rem' }}>View my task</button>
        <button onClick={() => navigate('/login')} style={{ padding: '12px 24px', cursor: 'pointer', backgroundColor: '#f44336', color: 'white', border: 'none', borderRadius: '5px', fontSize: '1rem' }}>Logout</button>
      </div>
    </div>
  );
};

export default Home;