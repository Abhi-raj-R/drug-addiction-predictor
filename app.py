from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load(open("logistic_addiction_model.pkl", "rb"))

# Feature list
features = [
    "Experimentation",
    "Academic_Performance_Decline",
    "Social_Isolation",
    "Financial_Issues",
    "Physical_Mental_Health_Problems",
    "Legal_Consequences",
    "Relationship_Strain",
    "Risk_Taking_Behavior",
    "Withdrawal_Symptoms",
    "Denial_and_Resistance_to_Treatment"
]

@app.route('/')
def home():
    return render_template('index.html', features=features)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [int(request.form[feature]) for feature in features]
        input_df = pd.DataFrame([data], columns=features)
        prediction = model.predict(input_df)[0]
        result_text = "⚠️ Likely to be Addicted" if prediction == 1 else "✅ Not Likely to be Addicted"
        return render_template('result.html',
                               prediction=result_text,
                               prediction_value=prediction,
                               features=features,
                               values=data)
    except Exception as e:
        return render_template('result.html',
                               prediction=f"Error: {str(e)}",
                               features=features,
                               values=[0]*len(features))

if __name__ == '__main__':
    app.run(debug=True)
