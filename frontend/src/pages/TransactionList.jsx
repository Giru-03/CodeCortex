import { useState, useEffect } from 'react';
import api from '../api';

function TransactionsList() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetchTransactions();
  }, []);

  const fetchTransactions = () => {
    api.get('/accounts/transactions/', {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    })
      .then((response) => {
        setTransactions(response.data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const handleDelete = (id) => {
    api.delete(`/accounts/transactions/${id}/`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    })
      .then(() => {
        alert('Transaction deleted successfully');
        fetchTransactions();
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <div>
      <h1>Transactions</h1>
      <ul>
        {transactions.map(transaction => (
          <li key={transaction.id}>
            Amount: {transaction.amount}, Category: {transaction.category}, Date: {transaction.trans_day}/{transaction.trans_month}/{transaction.trans_year}
            <button onClick={() => handleDelete(transaction.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TransactionsList;
