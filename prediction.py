import joblib
import pandas as pd

# Load model
model = joblib.load("model/model.pkl")


def predict_attrition(data):
    """
    Memprediksi kemungkinan karyawan mengalami attrition.

    Parameters:
        data (dict): Data satu karyawan.

    Returns:
        dict: Hasil prediksi dan probabilitas attrition.
    """

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0, 1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }


if __name__ == "__main__":

    employee = {
        "Age": 30,
        "BusinessTravel": "Travel_Frequently",
        "DailyRate": 500,
        "Department": "Sales",
        "DistanceFromHome": 10,
        "Education": 3,
        "EducationField": "Marketing",
        "EnvironmentSatisfaction": 2,
        "Gender": "Male",
        "HourlyRate": 70,
        "JobInvolvement": 2,
        "JobLevel": 1,
        "JobRole": "Sales Representative",
        "JobSatisfaction": 2,
        "MaritalStatus": "Single",
        "MonthlyIncome": 3000,
        "MonthlyRate": 15000,
        "NumCompaniesWorked": 2,
        "OverTime": "Yes",
        "PercentSalaryHike": 12,
        "PerformanceRating": 3,
        "RelationshipSatisfaction": 2,
        "StockOptionLevel": 0,
        "TotalWorkingYears": 5,
        "TrainingTimesLastYear": 2,
        "WorkLifeBalance": 2,
        "YearsAtCompany": 2,
        "YearsInCurrentRole": 1,
        "YearsSinceLastPromotion": 0,
        "YearsWithCurrManager": 1
    }

    result = predict_attrition(employee)

    print("Prediksi Attrition:", result["prediction"])
    print("Probabilitas Attrition:", f"{result['probability']:.2%}")