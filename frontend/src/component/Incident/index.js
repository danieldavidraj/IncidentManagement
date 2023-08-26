import './styles.css';

export default function Incident() {
    return (
      <div className='page'>
        <div className='card-container'>
          <div className="card">
            <div className="main-content">
              <div className="header">
                <span>Article on</span>
                <span>29-June-2023</span>
              </div>
              <p className="heading">Different ways to use CSS in React</p>
              <div className="categories">
                <span>React</span>
                <span>Css</span>
              </div>
            </div>
            <div className="footer">
              by Harsh Gupta
            </div>
          </div>
        </div>
        <div className="help-form-container">
          <form className="help-form">
            <div className="help-form-group">
              <label for="email">Company Email</label>
              <input type="text" id="email" name="email" required="" />
            </div>
            <div className="help-form-group">
              <label for="textarea">How Can We Help You?</label>
              <textarea name="textarea" id="textarea" rows="10" cols="50" required="">          </textarea>
            </div>
            <button className="help-form-submit-btn" type="submit">Submit</button>
          </form>
        </div>
        </div>
    );
}