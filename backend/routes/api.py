from flask import Blueprint, jsonify, request
from models.markowitz import optimizacion_markowitz
from models.xgboost_model import entrenar_modelo_xgboost, predecir_rendimientos
from utils.data_loader import descargar_datos, calcular_rendimientos

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route("/datos", methods=["POST"])
def obtener_datos():
    data = request.json
    tickers = data.get("tickers")
    start = data.get("start")
    end = data.get("end")

    datos = descargar_datos(tickers, start, end)
    rendimientos = calcular_rendimientos(datos)

    return jsonify(rendimientos.to_dict())

@api_blueprint.route("/markowitz", methods=["POST"])
def markowitz():
    data = request.json
    rendimientos = pd.DataFrame(data.get("rendimientos"))
    pesos = optimizacion_markowitz(rendimientos)

    return jsonify({"pesos": pesos.tolist()})

@api_blueprint.route("/xgboost", methods=["POST"])
def xgboost():
    data = request.json
    datos = pd.DataFrame(data.get("datos"))
    X, y = datos.drop(columns=['Target']), datos['Target']
    modelo = entrenar_modelo_xgboost(X, y)
    predicciones = predecir_rendimientos(modelo, X)

    return jsonify(predicciones.tolist())




