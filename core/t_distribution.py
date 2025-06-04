# -*- coding: utf-8 -*-

"""
Módulo para cálculos relacionados con la distribución t
"""

import numpy as np
from scipy import stats
import pandas as pd
from scipy import integrate

class TDistribution:
    def __init__(self):
        # Opcionalmente generamos tablas t para diferentes grados de libertad
        self.t_tables = {}
        
    def generate_t_table(self, df):
        """
        Genera una tabla de valores críticos de t para un grado de libertad específico
        """
        alphas = [0.10, 0.05, 0.025, 0.01, 0.00833, 0.00625, 0.005]
        t_values = [stats.t.ppf(1-alpha/2, df) for alpha in alphas]
        
        return pd.DataFrame({
            'df': [df] * len(alphas),
            'alpha': alphas,
            't_value': t_values
        })
    
    def calculate_area(self, t_value, df):
        """
        Calcula el área bajo la curva t hasta el valor t dado con df grados de libertad
        Retorna el valor de probabilidad (alpha)
        """
        return stats.t.cdf(t_value, df)
    
    def calculate_t_for_alpha(self, alpha, df):
        """
        Para un valor de alpha dado, encuentra el valor t correspondiente
        para el cual P(T <= t) = alpha con df grados de libertad
        """
        return stats.t.ppf(alpha, df)
    
    def calculate_area_between(self, t1, t2, df):
        """Calcula el área entre dos valores t"""
        return abs(self.calculate_area(t2, df) - self.calculate_area(t1, df))
    
    def calculate_area_integral(self, t_value, df):
        """
        Calcula el área bajo la curva t hasta el valor t dado con df grados de libertad
        usando integración numérica
        """
        def t_pdf(x, df):
            return (stats.t.pdf(x, df))
        
        result, error = integrate.quad(lambda x: t_pdf(x, df), -np.inf, t_value)
        return result