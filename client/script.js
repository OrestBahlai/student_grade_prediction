function performPrediction() {
    const method = document.getElementById('method').value; // Обраний метод
    const data = document.getElementById('input-data').value; // Дані введені користувачем

    if (!data) {
        document.getElementById('result').innerText = 'Please provide input data.';
        return;
    }

    // Парсимо введені дані у форматі g1, g2 тощо
    const input = data.split(',').map(val => val.trim());
    if (input.length !== 8) {
        document.getElementById('result').innerText = 'Invalid input format. Provide 8 comma-separated values.';
        return;
    }

    // Формуємо тіло POST-запиту
    const formData = new FormData();
    formData.append('g1', input[0]);
    formData.append('g2', input[1]);
    formData.append('medu', input[2]);
    formData.append('fedu', input[3]);
    formData.append('failures', input[4]);
    formData.append('studytime', input[5]);
    formData.append('internet_yes', input[6]);
    formData.append('higher_yes', input[7]);

    // Відправка POST-запиту на Flask сервер
    fetch('http://127.0.0.1:5000/predict_grade', { // Оновлений URL
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
