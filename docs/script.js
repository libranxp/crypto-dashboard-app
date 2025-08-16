async function refresh() {
  try {
    const res = await fetch("data.json");
    const data = await res.json();
    const container = document.getElementById("dashboard");
    container.innerHTML = "";

    if (!Array.isArray(data) || data.length === 0) {
      container.innerHTML = "<p>No data available.</p>";
      return;
    }

    data.forEach(asset => {
      if (!asset.price) return;
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
        <h2>${asset.symbol}</h2>
        <p>Price: $${asset.price}</p>
        <p>RSI: ${asset.RSI} | MACD: ${asset.MACD} | RVOL: ${asset.RVOL}</p>
        <p>Sentiment: ${asset.sentiment_score}</p>
        <p>TP: ${asset.TP} | SL: ${asset.SL}</p>
      `;
      container.appendChild(card);
    });
  } catch (err) {
    document.getElementById("dashboard").textContent = "⚠️ Failed to load data.";
    console.error(err);
  }
}

window.onload = refresh;
