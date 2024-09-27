import { useState } from 'react';
import api from '../api';

function FraudDetectionForm() {
    const [formData, setFormData] = useState({
        amt: '',
        zip: '',
        category: '',
        cc_num: '',
        datetime: '' 
    });
    const [result, setResult] = useState(null);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        const date = new Date(formData.datetime);
        const transData = {
            ...formData,
            trans_day: date.getDate(),
            trans_hour: date.getHours(),
            trans_month: date.getMonth() + 1, 
            trans_year: date.getFullYear(),
            trans_minute: date.getMinutes()
        };

        api.post('/accounts/predict/', transData)
            .then(response => setResult(response.data.is_fraud ? 'Fraud' : 'Not Fraud'))
            .catch(error => console.error(error));
    };

    return (
        <div>
            <h2>Fraud Detection</h2>
            <form onSubmit={handleSubmit}>
                <input
                    name="amt"
                    value={formData.amt}
                    onChange={handleChange}
                    placeholder="Amount"
                    required
                    type="number"
                />
                <input
                    name="zip"
                    value={formData.zip}
                    onChange={handleChange}
                    placeholder="Zip Code"
                    required
                    type="text"
                />
                <select
                    name="category"
                    value={formData.category}
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Category</option>
                    <option value="personal_care">Personal Care</option>
                    <option value="entertainment">Entertainment</option>
                    <option value="groceries">Groceries</option>
                    <option value="restaurants">Restaurants</option>
                </select>
                <input
                    name="cc_num"
                    value={formData.cc_num}
                    onChange={handleChange}
                    placeholder="Credit Card Number"
                    required
                    type="text"
                    maxLength="16"
                />
                <input
                    name="datetime"
                    value={formData.datetime}
                    onChange={handleChange}
                    placeholder="Transaction Date & Time"
                    required
                    type="datetime-local"
                />
                <button type="submit">Check Fraud</button>
            </form>
            {result && <p>Result: {result}</p>}
        </div>
    );
}

export default FraudDetectionForm;
