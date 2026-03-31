import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df = df.drop_duplicates().dropna()
    for col in df.select_dtypes(include='object').columns:
        if col != 'Machine failure':
            df[col] = df[col].astype('category').cat.codes
    target_col = 'Machine failure' if 'Machine failure' in df.columns else 'failure' if 'failure' in df.columns else df.columns[-1]
    X = df.drop(columns=[target_col])
    y = df[target_col]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X, y, X_scaled, scaler, df.columns.tolist()

def simulate_sensor_data(X, scaler):
    means = np.mean(X, axis=0)
    stds = np.std(X, axis=0)
    simulated = np.random.normal(means, stds)
    simulated_scaled = scaler.transform([simulated])
    return simulated, simulated_scaled
