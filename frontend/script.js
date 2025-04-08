function callBackend() {
  fetch('/.netlify/functions/app')
    .then(res => res.json())
    .then(data => {
      document.getElementById("response").textContent = data.message;
    });
}
