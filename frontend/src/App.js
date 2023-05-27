import './App.css';
import { getter } from './Utils';

function App() {
    return (
    <div className="App">
        <div>
            <h1>Login</h1>
        </div>
        <div>
            <form>
                <label for="fname">{ "First name:" }</label>
                <input type="text" id="fname" name="fname"/>
                <div></div>
                <label for="lname">{ "Last name:" }</label>
                <input type="text" id="lname" name="lname"/>
                <div></div>
                <input type="submit" value="Submit"/>
            </form>
        </div>
        <div>
            { /* Account registration */ }
        </div>
    </div>
    );
}

export default App;
