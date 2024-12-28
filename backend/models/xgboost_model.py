import xgboost as xgb

def entrenar_modelo_xgboost(X, y):
    """
    Entrena un modelo XGBoost para predicción de rendimientos.
    """
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100)
    model.fit(X, y)
    return model

def predecir_rendimientos(modelo, X):
    """
    Realiza predicciones de rendimientos con el modelo entrenado.
    """
    return modelo.predict(X)
