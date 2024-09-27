import { useState } from 'react';
import api from '../api';

function TransactionForm() {
  const [formData, setFormData] = useState({
    amount: '',
    zip_code: '',
    category: '',
    cc_num: '',
    datetime: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    api.post('/accounts/transaction/', formData, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    })
      .then(() => {
        alert('Transaction added successfully');
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Amount</label>
        <input type="number" step="0.01" name="amount" value={formData.amount} onChange={handleChange} required />
      </div>
      <div>
        <label>ZIP Code</label>
        <input type="number" name="zip_code" value={formData.zip_code} onChange={handleChange} required />
      </div>
      <div>
        <label>Category</label>
        <select name="category" value={formData.category} onChange={handleChange} required>
          <option value="groceries">Groceries</option>
          <option value="entertainment">Entertainment</option>
          <option value="utilities">Utilities</option>
        </select>
      </div>
      <div>
        <label>Credit Card Number</label>
        <input type="text" maxLength="16" name="cc_num" value={formData.cc_num} onChange={handleChange} required />
      </div>
      <div>
        <label>Date & Time</label>
        <input type="datetime-local" name="datetime" value={formData.datetime} onChange={handleChange} required />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
}

export default TransactionForm;
