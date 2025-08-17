let rawData = [];

async function loadData() {
  const res = await fetch("data.json");
  rawData = await res.json();
  renderDashboard(rawData);
}

function applyFilters() {
  const rsiMin = parseFloat(document.getElementById("rsiFilter").value);
  const rvolMin = parseFloat(document.getElementById("rvolFilter").value);
  const sentiment = document.getElementById("sentimentFilter").value;

  const filtered = rawData.filter(asset =>
    asset.rsi >= rsiMin &&
    asset.rvol >= rvolMin &&
    (!sentiment || asset.sentiment === sentiment)
  );

  renderDashboard(filtered);
}

function renderDashboard(data) {
  const container = document.getElementById("dashboard");
  container.innerHTML = "";

  data.forEach(asset => {
    const card = document.createElement("div");
    card.className = "asset-card";
    card.innerHTML = `
      <h2>${asset.symbol}</h2>
      <p>Price: $${asset.price}</p>
      <p>RSI: ${asset.rsi}</p>
      <p>RVOL: ${asset.rvol}</p>
      <p>Sentiment: ${asset.sentiment || "N/A"}</p>
      <canvas id="chart-${asset.symbol}" height="100"></canvas>
    `;
    container.appendChild(card);
    drawChart(asset);
  });
}

function drawChart(asset) {
  const ctx = document.getElementById(`chart-${asset.symbol}`).getContext("2d");
  const labels = asset.ohlc.map(p => new Date(p.t * 1000).toLocaleTimeString());
  const prices = asset.ohlc.map(p => p.c);
  const volumes = asset.ohlc.map(p => p.v);

  new Chart(ctx, {
    type: "line",
    data: {
      labels,
      datasets: [
        {
          label: "Price",
          data: prices,
          borderColor: "#00ffcc",
          yAxisID: "y",
        },
        {
          label: "Volume",
          data: volumes,
          borderColor: "#ff00cc",
          yAxisID: "y1",
        }
      ]
    },
    options: {
      scales: {
        y: { type: "linear", position: "left" },
        y1: { type: "linear", position: "right", grid: { drawOnChartArea: false } }
      }
    }
  });
}

loadData();
