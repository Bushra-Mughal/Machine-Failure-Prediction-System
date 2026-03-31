import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def train_and_save_models(X_scaled, y, save_path='models/'):
    import os
    os.makedirs(save_path, exist_ok=True)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)
    log_model = LogisticRegression(max_iter=1000, random_state=42)
    log_model.fit(X_train, y_train)
    joblib.dump(log_model, f'{save_path}log_model.pkl')
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train, y_train)
    joblib.dump(knn_model, f'{save_path}knn_model.pkl')
    log_acc = accuracy_score(y_test, log_model.predict(X_test))
    knn_acc = accuracy_score(y_test, knn_model.predict(X_test))
    best_model_name = 'Logistic Regression' if log_acc >= knn_acc else 'KNN'
    return best_model_name, log_acc, knn_acc

def load_models(save_path='models/'):
    log_model = joblib.load(f'{save_path}log_model.pkl')
    knn_model = joblib.load(f'{save_path}knn_model.pkl')
    return log_model, knn_model

def predict_failure(sample_scaled, log_model, knn_model, best_model_name):
    if best_model_name == 'Logistic Regression':
        model = log_model
    else:
        model = knn_model
    prob = model.predict_proba(sample_scaled)[0, 1]
    pred = model.predict(sample_scaled)[0]
    return prob, pred
