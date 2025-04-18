// Login.js
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext.jsx";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import "./user.css";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setIsLoading(true);
  
    try {
      const response = await fetch("http://127.0.0.1:8000/api/auth/token/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });
  
      if (response.ok) {
        const data = await response.json();
        
        // Fetch user profile after successful login
        const profileResponse = await fetch("http://127.0.0.1:8000/api/user/profile/", {
          headers: {
            'Authorization': `Token ${data.auth_token}`,
          }
        });
        
        if (profileResponse.ok) {
          const userData = await profileResponse.json();
          login(data.auth_token, userData);
          
          toast.success('Login successful!', {
            position: "top-center",
            autoClose: 2000,
            onClose: () => navigate("/")
          });
        } else {
          throw new Error("Failed to fetch user profile");
        }
      } else {
        const errorData = await response.json();
        const errorMessage = errorData.non_field_errors?.[0] || 
                         "Invalid username or password";
        throw new Error(errorMessage);
      }
    } catch (error) {
      toast.error(error.message || "Login failed. Please try again.", {
        position: "top-center",
        autoClose: 4000,
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="login-page-wrapper">
      <ToastContainer />
      
      <div className="login-page-container">
        <h1 className="login-page-header">RIST</h1>
        <p className="login-page-subheader">Connect to your account</p>
        
        <form onSubmit={handleLogin} className="login-page-form">
          <div className="login-page-input-group">
            <label>Username</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
              placeholder="Enter your username"
              className="login-page-input"
              disabled={isLoading}
            />
          </div>
          
          <div className="login-page-input-group">
            <label>Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              placeholder="Enter your password"
              className="login-page-input"
              disabled={isLoading}
            />
          </div>
          
          <button 
            type="submit" 
            className="login-page-button"
            disabled={isLoading}
          >
            {isLoading ? "Logging in..." : "Log In"}
          </button>
        </form>
        
        <div className="login-page-footer-links">
          <p 
            className="login-page-link"
            onClick={() => !isLoading && navigate("/register")}
          >
            Don't have an account? Sign Up
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;