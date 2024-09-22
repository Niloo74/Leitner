import React, { useState } from 'react';
import axios from 'axios';

function AddCard() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/add_card', {
        question,
        answer,
      });
      setMessage(response.data.message);
      setQuestion('');
      setAnswer('');
    } catch (error) {
      console.error('Error adding card:', error);
      setMessage('Error adding card');
    }
  };

  return (
    <div>
      <h1>Add a New Card</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Question: </label>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Answer: </label>
          <input
            type="text"
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            required
          />
        </div>
        <button type="submit">Add Card</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default AddCard;
