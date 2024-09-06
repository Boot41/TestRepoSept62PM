import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import FresherInterviewPage from './pages/FresherInterviewPage';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <nav>
            <Link to="/">Home</Link>
            <Link to="/fresher-interview">Fresher Interview</Link>
          </nav>
          <Routes>
            <Route path="/" element={<p>Welcome Home!</p>} />
            <Route path="/fresher-interview" element={<FresherInterviewPage />} />
          </Routes>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    </Router>
  );
}

export default App;