# -*- coding: utf-8 -*-

"""
Módulo para cálculos relacionados con la distribución normal estándar (Z)
"""

import numpy as np
from scipy import stats
import pandas as pd
from scipy import integrate

class ZDistribution:
    def __init__(self):
        # Cargar o crear tablas de la distribución Z si son necesarias
        self.z_table = self._generate_z_table()
    
    def _generate_z_table(self):
        """Genera una tabla de probabilidades para la distribución normal estándar"""
        z_values = np.arange(-5.0, 5.01, 0.01)
        probs = [stats.norm.cdf(z) for z in z_values]
        return pd.DataFrame({'z': z_values, 'prob': probs})
    
    def calculate_area(self, z_value):
        """
        Calcula el área bajo la curva normal estándar hasta el valor z dado
        Retorna el valor de probabilidad (alpha)
        """
        return stats.norm.cdf(z_value)
    
    def calculate_z_for_alpha(self, alpha):
        """
        Para un valor de alpha dado, encuentra el valor Z correspondiente
        para el cual P(Z <= z) = alpha
        """
        return stats.norm.ppf(alpha)
    
    def calculate_area_between(self, z1, z2):
        """Calcula el área entre dos valores z"""
        return abs(self.calculate_area(z2) - self.calculate_area(z1))
    
    def calculate_area_integral(self, z_value):
        """
        Calcula el área bajo la curva normal estándar hasta el valor z 
        usando integración numérica
        """
        def normal_pdf(x):
            return (1/np.sqrt(2*np.pi)) * np.exp(-0.5 * x**2)
        
        result, error = integrate.quad(normal_pdf, -np.inf, z_value)
        return result