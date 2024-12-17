from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/predict_grade', methods=['POST'])
def predict_grade():

    g1 = int(request.form['g1'])
    g2 = int(request.form['g2'])
    medu = int(request.form['medu'])
    fedu = int(request.form['fedu'])
    failures = int(request.form['failures'])
    studytime = int(request.form['studytime'])
    internet_yes = request.form['internet_yes']
    higher_yes = request.form['higher_yes']

    response = jsonify({
        'predicted_grade': util.get_predicted_grade(g1, g2, medu, higher_yes, fedu, failures, studytime, internet_yes)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    print("Server started")
    util.load_saved_artifacts()
    app.run()