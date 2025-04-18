// App.js
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext.jsx';
import { BookmarkProvider } from './context/BookmarkContext/BookmarkContext.js';
import Layout from './components/Layout/Layout.js';

import HomePage from './pages/HomePage/HomePage.js';
import AboutPage from './pages/AboutPage/AboutPage.js';
import LatestVolume from './pages/LatestVolumes/LatestVolumes.js';
import ContactPage from './pages/ContactPage/ContactPage.js';
import Instructions from './pages/Instructions/Instructions.js';
import Comites from './pages/Comites/Comites.js';
import Login from './pages/Profile/Login.js';
import Register from './pages/Profile/Register.js';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <BookmarkProvider>
          <Routes>
            <Route path="/" element={<Layout><HomePage /></Layout>} />
            <Route path="/about" element={<Layout><AboutPage /></Layout>} />
            <Route path="/latest-volumes" element={<Layout><LatestVolume /></Layout>} />
            <Route path="/contact" element={<Layout><ContactPage /></Layout>} />
            <Route path="/instructions" element={<Layout><Instructions /></Layout>} />
            <Route path="/comites" element={<Layout><Comites /></Layout>} />
            <Route path="/login" element={<Layout><Login /></Layout>} />
            <Route path="/register" element={<Layout><Register /></Layout>} />
          </Routes>
        </BookmarkProvider>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;