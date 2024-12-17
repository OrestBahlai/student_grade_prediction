function performPrediction() {
    const g1 = document.getElementById('g1').value.trim();
    const g2 = document.getElementById('g2').value.trim();
    const medu = document.getElementById('medu').value.trim();
    const fedu = document.getElementById('fedu').value.trim();
    const failures = document.getElementById('failures').value.trim();
    const studytime = document.getElementById('studytime').value.trim();
    const internet_yes = document.getElementById('internet_yes').value.trim();
    const higher_yes = document.getElementById('higher_yes').value.trim();

    if (!g1 || !g2 || !medu || !fedu || !failures || !studytime || !internet_yes || !higher_yes) {
        document.getElementById('result').innerText = 'Please fill in all fields.';
        return;
    }

    const input = [g1, g2, medu, fedu, failures, studytime, internet_yes, higher_yes];

    const formData = new FormData();
    formData.append('g1', input[0]);
    formData.append('g2', input[1]);
    formData.append('medu', input[2]);
    formData.append('fedu', input[3]);
    formData.append('failures', input[4]);
    formData.append('studytime', input[5]);
    formData.append('internet_yes', input[6]);
    formData.append('higher_yes', input[7]);

    fetch('http://127.0.0.1:5000/predict_grade', { // URL до Flask
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').innerText = `Error: ${data.error}`;
        } else {
            document.getElementById('result').innerText = `Predicted Grade: ${data.predicted_grade}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'An error occurred while predicting the grade.';
    });
}