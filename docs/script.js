async function refresh() {
  const tickers = prompt("Enter comma-separated tickers").split(",");
  const res = await fetch('/scan', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({tickers})
  });
  const data = await res.json();
  document.getElementById('dashboard').innerHTML = JSON.stringify(data, null, 2);
}
