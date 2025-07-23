
# Student Drug Addiction Risk Predictor

A modern, responsive web application that enables students to confidentially assess their risk for drug addiction using machine learning. This app offers a secure, intuitive, and informative interface, encouraging early self-evaluation and access to helpful resources.


---

## 🔍 Overview

Student drug addiction is a pressing issue impacting academic performance, health, and future prospects. This tool leverages data-driven techniques to help identify early signs of addiction risk and support prevention strategies through timely guidance and education.

---

## 🚀 Features

- ✅ **Confidential Risk Assessment Form**
- 🌐 **Clean, Responsive UI** (Mobile-friendly, Dark Mode supported)
- 🔦 **Real-time Prediction with ML Model**
- 🧠 **Personalized Results & Recommendations**
- 📊 **Feature Summary and Risk Explanation**
- 📚 **Educational Facts, FAQs & Testimonials**
- 🖨️ **Download/Print Results**
- 💬 **Feedback Collection Form**

---

## 🛠 Tech Stack

- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend:** Python 3.11, Flask
- **Machine Learning:** scikit-learn (Logistic Regression Model)
- **Deployment Options:** Render, Ngrok, or any Flask-compatible platform

---

## 📂 Folder Structure

```
├── app.py
├── static/
│   ├── style.css
│   ├── hero_image.png
├── templates/
│   ├── index.html
│   ├── result.html
├── logistic_addiction_model.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/student-drug-predictor.git
   cd student-drug-predictor
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your Trained Model**
   - Place your `.pkl` file (e.g., `logistic_addiction_model.pkl`) in the project root.

4. **Run the Flask App**
   ```bash
   python app.py
   ```

5. **Open the Web App**
   - Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🧪 Usage Guide

1. Open the app and navigate to the home page.
2. Fill out the **risk assessment form** honestly.
3. Click **Predict** to receive your **risk level** and **advice**.
4. Use **Dark Mode toggle** for night-friendly view.
5. **Download or print** your results if needed.
6. Read through the **facts, testimonials**, and **FAQ** section.

---

## 🧠 Customization

- **ML Model:** Replace `logistic_addiction_model.pkl` with your own trained model.
- **Features:** Modify the `features` list and form inputs in `app.py`.
- **UI/UX:** Update styles in `static/style.css`, HTML in `templates/`.
- **Dark Mode:** Already included with a toggle button.
- **Images:** Store custom images in `static/` folder.

---

## 🙌 Credits

- **UI/UX Design:** Bootstrap, Font Awesome, Google Fonts
- **Hero Illustration:** [Freepik](https://www.freepik.com)
- **ML Model:** scikit-learn
- **Deployment:** Render & Ngrok for remote testing

---

## ⚠️ Disclaimer

This tool is designed **for educational and awareness purposes only**. It does **not replace professional medical advice or diagnosis**. All user inputs are kept confidential and are not stored.

---

## ⭐ Contribute

If you'd like to contribute, fork this repo and submit a pull request with improvements, bug fixes, or enhancements.

---

## 📬 Contact

- 📧 Email: abhirajr628@gmail.com

