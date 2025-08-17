function applyFilters() {
  const rsiMin = parseFloat(document.getElementById("rsiFilter").value);
  const rvolMin = parseFloat(document.getElementById("rvolFilter").value);
  const sentiment = document.getElementById("sentimentFilter").value;
  const type = document.getElementById("typeFilter").value;

  const filtered = rawData.filter(asset =>
    asset.qualified &&
    asset.rsi >= rsiMin &&
    asset.rvol >= rvolMin &&
    (!sentiment || asset.sentiment_score >= 0.2 && sentiment === "positive" ||
     asset.sentiment_score <= -0.2 && sentiment === "negative" ||
     Math.abs(asset.sentiment_score) < 0.2 && sentiment === "neutral") &&
    (!type || asset.asset_type === type)
  );

  renderDashboard(filtered);
}
