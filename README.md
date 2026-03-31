# Aether Intelligence 🤖
**Capstone project** <br>
*Failure prediction using machine learning* <br>
An intelligent system to predict machine failures using sensor data.
## 🚀Project overview:
Aether Intelligence is a Machine Learning system that predicts machine failure in advance using sensor data, helping reduce downtime and maintenance cost.<br>

## Approach:
- Preprocess the dataset
- Add normalization layer
- Train ML models for machine failure prediction
- Suggest the most appropriate model

## Models trained:
- Logistic Regression (best performing model)
- KNN
Built using Copilot tool

## 🛠 Tech Stack
- Python
- Scikit-learn
- Pandas, NumPy
- Streamlit

## UI design (Google Stitch):
Design the user interfaces including:
- Login page
- Realtime Dashboard
- Alerts & History
- Sensors data view page

## Web application 🌐:
Built a Streamlit based webapp displaying:
- Displays machine health status
- Shows prediction results in real-time
- Visualizes sensor data

## Steps for installation and Setup:
1️⃣ Clone the Repository
git clone https://github.com/Bushra-Mughal/Machine-Failure-Prediction-System.git
cd Machine-Failure-Prediction-System

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate it:
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Jupyter Notebook (for training)
jupyter notebook

Open:
notebooks/model_training.ipynb

5️⃣ Run the Streamlit App
streamlit run app/app.py

6️⃣ Access the App
Open in browser:
http://localhost:8501




