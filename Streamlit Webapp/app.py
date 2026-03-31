import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve, accuracy_score
import os
from utils import load_and_preprocess_data, simulate_sensor_data
from models import load_models, predict_failure

st.set_page_config(
    page_title="Machine Failure Prediction",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stButton>button { background-color: #6c5ce7; color: white; }
    section[data-testid="stSidebar"] {
        background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
        color: #222;
    }
    h1, h2, h3 { color: #6c5ce7; }
    .metric-card { background-color: #e3f2fd; padding: 10px; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    X, y, X_scaled, scaler, columns = load_and_preprocess_data("Predictive Maintainance Dataset.csv")
    return X, y, X_scaled, scaler, columns

@st.cache_resource
def load_trained_models():
    if not os.path.exists('models/log_model.pkl'):
        st.error("Models not found. Please run the training script first.")
        st.stop()
    log_model, knn_model = load_models()
    return log_model, knn_model

X, y, X_scaled, scaler, columns = load_data()
log_model, knn_model = load_trained_models()

pages = {
    "Realtime Dashboard": "dashboard",
    "Key Visualizations": "visualizations",
    "Failure Alerts": "alerts"
}

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", list(pages.keys()))

if page == "Realtime Dashboard":
    st.title("🔧 Realtime Machine Dashboard")
    if st.button("Refresh Sensor Data"):
        simulated_raw, simulated_scaled = simulate_sensor_data(X, scaler)
        st.session_state['sensor_data'] = simulated_raw
        st.session_state['scaled_data'] = simulated_scaled
    if 'sensor_data' not in st.session_state:
        simulated_raw, simulated_scaled = simulate_sensor_data(X, scaler)
        st.session_state['sensor_data'] = simulated_raw
        st.session_state['scaled_data'] = simulated_scaled
    sensor_data = st.session_state['sensor_data']
    scaled_data = st.session_state['scaled_data']
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Air Temperature", f"{sensor_data[0]:.2f} K")
    with col2:
        st.metric("Process Temperature", f"{sensor_data[1]:.2f} K")
    with col3:
        st.metric("Rotational Speed", f"{sensor_data[2]:.0f} rpm")
    st.subheader("Sensor Readings")
    st.write(pd.DataFrame([sensor_data], columns=columns[:-1]))
    prob, pred = predict_failure(scaled_data, log_model, knn_model, "Logistic Regression")
    st.subheader("Prediction")
    st.write(f"Failure Probability: {prob:.3f}")
    st.write(f"Status: {'Failure Detected' if pred == 1 else 'No Failure'}")

elif page == "Key Visualizations":
    st.title("📊 Key Visualizations")
    from sklearn.model_selection import train_test_split
    import seaborn as sns
    _, X_test, _, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)
    log_prob = log_model.predict_proba(X_test)[:,1]
    knn_prob = knn_model.predict_proba(X_test)[:,1]

    tab1, tab2, tab3 = st.tabs([
        "Accuracy Comparison", "ROC Curve", "Feature Importance"])

    with tab1:
        acc_log = accuracy_score(y_test, log_model.predict(X_test))
        acc_knn = accuracy_score(y_test, knn_model.predict(X_test))
        fig, ax = plt.subplots(figsize=(3,2))
        ax.bar(['Logistic', 'KNN'], [acc_log, acc_knn], color=['#6c5ce7','#74b9ff'], width=0.4)
        ax.set_ylim(0.7, 1.0)
        ax.set_title('Accuracy')
        for idx, val in enumerate([acc_log, acc_knn]):
            ax.text(idx, val + 0.01, f'{val:.3f}', ha='center', fontsize=9)
        st.pyplot(fig, clear_figure=True)
        st.caption("Smaller, focused accuracy comparison.")

    with tab2:
        fpr_log, tpr_log, _ = roc_curve(y_test, log_prob)
        fpr_knn, tpr_knn, _ = roc_curve(y_test, knn_prob)
        fig, ax = plt.subplots(figsize=(3,2))
        ax.plot(fpr_log, tpr_log, label=f'Logistic AUC={roc_auc_score(y_test, log_prob):.3f}')
        ax.plot(fpr_knn, tpr_knn, label=f'KNN AUC={roc_auc_score(y_test, knn_prob):.3f}')
        ax.plot([0,1],[0,1],'k--', alpha=0.5)
        ax.set_xlabel('FPR')
        ax.set_ylabel('TPR')
        ax.set_title('ROC Curve')
        ax.legend(fontsize=8)
        st.pyplot(fig, clear_figure=True)
        st.caption("Compact ROC curve for both models.")

    with tab3:
        st.subheader("Feature Importance / Key Feature Distribution")
        # If Logistic Regression, show feature importances
        if hasattr(log_model, 'coef_'):
            importances = abs(log_model.coef_[0])
            feature_names = columns[:-1]
            sorted_idx = importances.argsort()[::-1]
            top_features = [feature_names[i] for i in sorted_idx[:5]]
            top_importances = importances[sorted_idx[:5]]
            fig, ax = plt.subplots(figsize=(4,2))
            ax.barh(top_features[::-1], top_importances[::-1], color="#6c5ce7")
            ax.set_title("Top Feature Importances (Logistic Regression)")
            st.pyplot(fig, clear_figure=True)
        else:
            # Fallback: show distribution of first feature
            df_X = pd.DataFrame(X, columns=columns[:-1])
            key_col = columns[0]
            fig, ax = plt.subplots(figsize=(3,2))
            sns.histplot(df_X[key_col], bins=20, ax=ax, color="#6c5ce7", kde=True)
            ax.set_title(f"{key_col} Distribution")
            st.pyplot(fig, clear_figure=True)
        st.caption("Most important features for prediction.")
elif page == "Failure Alerts":
    st.title("🚨 Failure Alerts & Recommendations")
    # Use current sensor data or simulate if not present
    if 'sensor_data' in st.session_state and 'scaled_data' in st.session_state:
        sensor_data = st.session_state['sensor_data']
        scaled_data = st.session_state['scaled_data']
    else:
        sensor_data, scaled_data = simulate_sensor_data(X, scaler)
    prob, pred = predict_failure(scaled_data, log_model, knn_model, "Logistic Regression")
    st.subheader("Prediction Result")
    st.write(f"Failure Probability: {prob:.3f}")
    if pred == 1:
        st.error("⚠️ Failure Detected!")
        st.write("### Recommendations:")
        st.markdown("""
        - **Schedule immediate maintenance.**
        - Inspect air temperature and process temperature sensors.
        - Check for abnormal rotational speed or vibration.
        - Review recent maintenance logs for unresolved issues.
        - Ensure all safety protocols are followed.
        """)
    else:
        st.success("✅ No Failure Detected. Machine is operating normally.")
        st.write("### Recommendations:")
        st.markdown("""
        - Continue regular monitoring.
        - Perform routine maintenance as scheduled.
        - Ensure sensors are calibrated.
        - Keep maintenance logs up to date.
        """)