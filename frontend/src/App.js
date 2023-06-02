import './App.css';
import { getter } from './Utils';

const App = () => {
    // want function to POST user data

    return (
        <div className="App">
            <div>
                <h1>Login</h1>
            </div>
            <div>
                <form>
                    <label for="username">{ "Username: " }</label>
                    <input type="text" id="username" name="username"/>
                    <div></div>
                    <label for="password">{ "Password: " }</label>
                    <input type="text" id="password" name="password"/>
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
