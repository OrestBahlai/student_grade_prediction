import  pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="X does not have valid feature names")


__model = None

def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __model
    with open("/Users/orest/Documents/study/Курсова/grade_prediction/server/artifacts/random_forest_model.pkl", "rb") as file:
        __model = pickle.load(file)
        print("Model loaded successfully")

    print("loading saved artifacts...done")


def get_predicted_grade(g1, g2, medu, higher_yes, fedu, failures, studytime, internet_yes):
    x = np.array([[
        g1,
        g2,
        medu,
        fedu,
        failures,
        studytime,
        1 if internet_yes == 'yes' else 0,
        1 if higher_yes == 'yes' else 0
    ]])

    predicted_grade = __model.predict(x)

    return predicted_grade[0]

if __name__ == "__main__":
    load_saved_artifacts()

    predicted_grade = get_predicted_grade(19, 19, 3, 'yes', 3, 0, 3, 'yes')
    predicted_grade1 = get_predicted_grade(19, 16, 3, 'yes', 3, 0, 3, 'yes')
    print(f"Predicted Grade: {predicted_grade}")
    print(f"Predicted Grade: {predicted_grade1}")