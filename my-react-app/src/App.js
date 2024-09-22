import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import AddCard from './AddCard';  // Your AddCard component
import Home from './Home';  // Your Home component

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/add-card">Add Card</Link></li>
          </ul>
        </nav>
        
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/add-card" element={<AddCard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
