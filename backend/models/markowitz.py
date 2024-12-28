import numpy as np
from scipy.optimize import minimize

def optimizacion_markowitz(rendimientos):
    """
    Optimiza los pesos de la cartera usando el modelo de Markowitz.
    """
    medias = rendimientos.mean()
    cov = rendimientos.cov()
    num_activos = len(medias)

    def objetivo(pesos):
        return np.dot(pesos.T, np.dot(cov, pesos))  # Minimizar varianza

    # Restricción: suma de pesos = 1
    restricciones = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(num_activos))

    # Pesos iniciales
    pesos_iniciales = np.ones(num_activos) / num_activos

    # Optimización
    resultado = minimize(objetivo, pesos_iniciales, bounds=bounds, constraints=restricciones)
    return resultado.x
