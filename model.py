import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score, root_mean_squared_error
from sklearn.linear_model import Ridge
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

df = pd.read_csv(r"C:\Users\ahmed\OneDrive\Desktop\House-price-app\df_cleaned-Copy1.csv")

X = df.drop("Sale Amount", axis=1)
y = df["Sale Amount"]

# Identify categorical columns
cat_cols = X.select_dtypes(include='object').columns.tolist()

# Identify numeric columns
num_cols = X.select_dtypes(include='number').columns.tolist()

# Preprocessing
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

# Combine preprocessing for numeric and categorical features
preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, num_cols),
    ("cat", categorical_transformer, cat_cols)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=8
)

def evaluate_model(name, model, X_train, X_test, y_train, y_test):
    pipe = Pipeline(steps=[("preprocessor", preprocessor),
                           ("model", model)])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print(f"\n📊 {name} Model Evaluation:")
    print(f"MAE : {mae:,.2f}")
    print(f"RMSE: {rmse:,.2f}")
    print(f"R²  : {r2:.4f}")

evaluate_model("XGBoost", XGBRegressor(random_state= 8),X_train, X_test, y_train, y_test)


import optuna
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np

def objective(trial):
    params = {
        "n_estimators": trial.suggest_int("n_estimators", 100, 500),
        "max_depth": trial.suggest_int("max_depth", 3, 15),
        "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3),
        "subsample": trial.suggest_float("subsample", 0.5, 1.0),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.5, 1.0),
        "reg_alpha": trial.suggest_float("reg_alpha", 0.0, 1.0),
        "reg_lambda": trial.suggest_float("reg_lambda", 0.0, 2.0),
    }

    xgb = XGBRegressor(**params, random_state=42)
    
    pipe = Pipeline([
        ("preprocessor", preprocessor),
        ("model", xgb)
    ])
    
    # Using 3-fold cross-validation and negative MAE (lower is better)
    score = cross_val_score(pipe, X_train, y_train, cv=3, scoring="neg_mean_absolute_error")
    
    return -1.0 * score.mean() 

study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=50)

print("✅ Best trial:")
print("  Value: ", study.best_value)
print("  Params:", study.best_params)

best_params = study.best_params
final_xgb = XGBRegressor(**best_params, random_state=42)

xgb_optuna_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", final_xgb)
])

xgb_optuna_pipeline.fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_pred = xgb_optuna_pipeline.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print("\n📊 Optuna Tuned XGBoost Evaluation:")
print(f"MAE : {mae:,.2f}")

print(f"R²  : {r2:.4f}")

import joblib
joblib.dump(xgb_optuna_pipeline, "xgb_optuna_pipeline.pkl")
