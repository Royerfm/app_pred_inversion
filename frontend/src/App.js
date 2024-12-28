import React, { useState } from "react";
import axios from "axios";
import Chart from "chart.js/auto";

function App() {
  const [tickers, setTickers] = useState("AAPL,MSFT,GOOG");
  const [data, setData] = useState(null);

  const fetchData = async () => {
    const response = await axios.post("http://localhost:5000/datos", {
      tickers: tickers.split(","),
      start: "2020-01-01",
      end: "2023-01-01",
    });
    setData(response.data);
  };

  return (
    <div>
      <h1>Optimizador de Cartera</h1>
      <input
        value={tickers}
        onChange={(e) => setTickers(e.target.value)}
        placeholder="Tickers separados por coma"
      />
      <button onClick={fetchData}>Obtener Datos</button>

      {data && (
        <div>
          <h2>Rendimientos</h2>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;