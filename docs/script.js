async function refresh() {
  const res = await fetch("data.json");
  const data = await res.json();
  const container = document.getElementById("dashboard");
  container.innerHTML = "";

  data.forEach(ticker => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <h2>${ticker.symbol}</h2>
      <p>Price: $${ticker.price} | TP: $${ticker.TP} | SL: $${ticker.SL}</p>
      <p>RSI: ${ticker.RSI} | EMA: ${ticker.EMA} | VWAP: ${ticker.VWAP}</p>
      <p>MACD: ${ticker.MACD} | RVOL: ${ticker.RVOL} | Sentiment: ${ticker.sentiment}</p>
    `;
    container.appendChild(card);
  });

  const ctx = document.getElementById("chart").getContext("2d");
  const first = data[0];
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: first.chart.map((_, i) => i),
      datasets: [{
        label: `${first.symbol} Price`,
        data: first.chart,
        borderColor: 'orange',
        fill: false
      }]
    }
  });
