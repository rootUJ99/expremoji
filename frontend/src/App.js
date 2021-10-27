import {useEffect, useState} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [data, setData] = useState(null);
  useEffect(()=>{
    (async () => {
      try {

        const data = await fetch(`http://${process.env.REACT_APP_API_BASE_URL}:8000/api/v1/start`);
        const jsonData = await data.json();
        setData(jsonData);
      }
      catch (err) {
        console.log(err, 'err');
      }
    })()
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React {data?.start}
        </a>
      </header>
    </div>
  );
}

export default App;
