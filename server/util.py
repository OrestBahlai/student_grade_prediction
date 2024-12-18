import  pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="X does not have valid feature names")


__rf_model = None
__xgb_model = None
__dt_model = None

def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __rf_model, __xgb_model, __dt_model

    with open("/Users/orest/Documents/study/Курсова/grade_prediction/server/artifacts/random_forest_model.pkl", "rb") as file:
        __rf_model = pickle.load(file)
        print("Random Forest model loaded successfully")

    with open("/Users/orest/Documents/study/Курсова/grade_prediction/server/artifacts/xgb_regressor_model.pkl", "rb") as file:
        __xgb_model = pickle.load(file)
        print("XGB Regressor model loaded successfully")

    with open("/Users/orest/Documents/study/Курсова/grade_prediction/server/artifacts/decision_tree_model.pkl", "rb") as file:
        __dt_model = pickle.load(file)
        print("Decision Tree model loaded successfully")

    print("loading saved artifacts...done")


def get_predicted_grade(model_name, g1, g2, medu, higher_yes, fedu, failures, studytime, internet_yes):
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

    if model_name == "random_forest":
        predicted_grade = __rf_model.predict(x)
    elif model_name == "xgb_regressor":
        predicted_grade = __xgb_model.predict(x)
    elif model_name == "decision_tree":
        predicted_grade = __dt_model.predict(x)
    else:
        raise ValueError("Invalid model name. Choose from: random_forest, xgb_regressor, decision_tree")

    return predicted_grade[0]

if __name__ == "__main__":
    load_saved_artifacts()

    predicted_grade = get_predicted_grade("random_forest", 19, 19, 3, 'yes', 3, 0, 3, 'yes')
    predicted_grade1 = get_predicted_grade("xgb_regressor",19, 16, 3, 'yes', 3, 0, 3, 'yes')
    print(f"Predicted Grade: {predicted_grade}")
    print(f"Predicted Grade: {predicted_grade1}")