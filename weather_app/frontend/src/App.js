import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!message.trim()) return;

    try {
      const res = await axios.post('http://localhost:8000/query', { message });
      setResponse(res.data.response);
    } catch (err) {
      setResponse('Sorry, something went wrong. Try again.');
    }
  };

  return (
    <div className="container">
      <h1>Weather Assistant</h1>
      
      <form onSubmit={sendMessage}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="e.g. What's the weather in Pune?"
        />
        <button type="submit">Send</button>
      </form>

      {response && (
        <div className="response-box">
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;