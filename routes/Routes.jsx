import { Routes, Route } from 'react-router-dom';
import { Home, Login, Register, Articles, Volumes, Issues, Profile } from '../pages';
import { ProtectedRoute } from './ProtectedRoute';

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      
      <Route element={<ProtectedRoute />}>
        <Route path="/articles" element={<Articles />} />
        <Route path="/volumes" element={<Volumes />} />
        <Route path="/issues" element={<Issues />} />
        <Route path="/profile" element={<Profile />} />
      </Route>
    </Routes>
  );
};

export default AppRoutes;