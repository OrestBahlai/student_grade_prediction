function performPrediction() {
    const method = document.getElementById('method').value;
    const data = document.getElementById('input-data').value;
    if (!data) {
        document.getElementById('result').innerText = 'Please provide input data.';
        return;
    }

    // Simulate prediction logic (replace with real API calls later)
    let accuracy = Math.random() * 100;
    document.getElementById('result').innerText = `Method: ${method}, Accuracy: ${accuracy.toFixed(2)}%`;
}
