import './styles.css';
import {useEffect, useState} from 'react';
import axios from 'axios';

export default function Incident() {
  const [incidents, setIncidents] = useState([]);
    const token = localStorage.getItem('access');
    useEffect(() => {
      axios.get('https://incident-backend.onrender.com/incident/list/', { 
        headers: {
          'Authorization': 'Bearer ' + token
        }
      })
      .then((response) => {
        setIncidents(response.data.incidents);
      })
    }, []);

    const handleChange = evt => {
      const value = evt.target.value;
      setState({
        ...state,
        [evt.target.name]: value
      });
    };
    const [state, setState] = useState({
      message: ""
    });
  
    const handleOnSubmit = evt => {
      const token = localStorage.getItem('access');
      evt.preventDefault();
  
      const { message } = state;
      
      axios.post('https://incident-backend.onrender.com/incident/collect/', {
          message
      }, {
        headers: {
          'Authorization': 'Bearer ' + token
        }
      })
      .then((response) => {
        console.log(response);
      })
    };

    return (
      <div className='page'>
        <div className='card-container'>
          {incidents && incidents.length && incidents.map((incident) => {
            return (
              <div className="card">
                <div className="main-content">
                  <div className="header">
                    <span>Incident:</span>
                  </div>
                  <p className="heading">{incident.message}</p>
                  <div className="categories">
                    <span>{incident.resolution ? incident.resolution : 'Not categorized'}</span>
                  </div>
                </div>
              </div>
            )
          })}
        </div>
        <div className="help-form-container">
          <form className="help-form" onSubmit={handleOnSubmit}>
            <div className="help-form-group">
              <label for="email">Company Email</label>
              <input type="text" id="email" name="email" required="" />
            </div>
            <div className="help-form-group">
              <label for="textarea">How Can We Help You?</label>
              <textarea name="textarea" id="textarea" rows="10" cols="50" required="" onChange={handleChange}>          </textarea>
            </div>
            <button className="help-form-submit-btn" type="submit">Submit</button>
          </form>
        </div>
        </div>
    );
}