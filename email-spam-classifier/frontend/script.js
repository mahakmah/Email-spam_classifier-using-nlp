function checkSpam() {
    const message = document.getElementById("emailInput").value.trim();
    const resultBox = document.getElementById("resultBox");
    const result = document.getElementById("result");
  
    if (!message) {
      result.textContent = "Please enter some text.";
      result.style.color = "red";
      return;
    }
  
    fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ email: message })
    })
      .then((response) => response.json())
      .then((data) => {
        result.textContent = "Prediction: " + data.result;
        result.style.color = data.result === "Spam" ? "crimson" : "green";
      })
      .catch((error) => {
        result.textContent = "Error: Could not connect to server.";
        result.style.color = "red";
        console.error("Error:", error);
      });
  }
  