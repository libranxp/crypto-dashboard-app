let rawData = [];

async function loadData() {
  const res = await fetch("data.json");
  rawData = await res.json();
  const qualified = rawData.filter(a => a.qualified);
  renderDashboard(qualified);
}

function applyFilters() {
  const rsiMin = parseFloat(document.getElementById("rsiFilter").value);
  const rvolMin = parseFloat(document.getElementById("rvolFilter").value);
  const sentiment = document.getElementById("sentimentFilter").value;

  const filtered = rawData.filter(asset =>
    asset.qualified &&
    asset.rsi >= rsiMin &&
    asset.rvol >= rvolMin &&
    (!sentiment || asset.sentiment_score >= 0.2 && sentiment === "positive" ||
     asset.sentiment_score <= -0.2 && sentiment === "negative" ||
     Math.abs(asset.sentiment_score) < 0.2 && sentiment === "neutral")
  );

  renderDashboard(filtered);
}
