from utils import load_and_preprocess_data
from models import train_and_save_models

X, y, X_scaled, scaler, _ = load_and_preprocess_data("Predictive Maintainance Dataset.csv")
best_model, log_acc, knn_acc = train_and_save_models(X_scaled, y)
print(f"Best model: {best_model}, Logistic Acc: {log_acc:.3f}, KNN Acc: {knn_acc:.3f}")
