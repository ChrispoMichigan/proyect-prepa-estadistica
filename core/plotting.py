# -*- coding: utf-8 -*-

"""
Módulo para generar gráficos estadísticos
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import scipy.stats as stats

class StatPlotter:
    def __init__(self):
        self.colors = {
            'primary': '#404040',   # Gris oscuro
            'secondary': '#808080', # Gris medio
            'highlight': '#2C3E50', # Azul oscuro neutro
            'background': '#F5F5F5' # Gris muy claro
        }
    
    def create_z_plot(self, frame, z_value=None, area=None):
        """
        Crea un gráfico de la distribución normal estándar, 
        opcionalmente marcando un valor z y sombreando el área
        """
        fig = Figure(figsize=(5, 3), dpi=100)
        fig.patch.set_facecolor(self.colors['background'])
        ax = fig.add_subplot(111)
        
        # Valores de x para la distribución normal
        x = np.linspace(-4, 4, 1000)
        y = stats.norm.pdf(x)
        
        # Gráfica base
        ax.plot(x, y, color=self.colors['primary'])
        ax.axhline(y=0, color=self.colors['secondary'], linestyle='-', alpha=0.3)
        ax.axvline(x=0, color=self.colors['secondary'], linestyle='-', alpha=0.3)
        
        # Si se proporciona un valor z, marcarlo en la gráfica
        if z_value is not None:
            # Punto z
            ax.plot([z_value], [stats.norm.pdf(z_value)], 'o', 
                    color=self.colors['highlight'])
            ax.axvline(x=z_value, color=self.colors['highlight'], 
                      linestyle='--', alpha=0.6)
            
            # Sombrear el área si se proporciona
            if area is not None:
                fill_x = np.linspace(-4, z_value, 1000)
                fill_y = stats.norm.pdf(fill_x)
                ax.fill_between(fill_x, fill_y, 0, alpha=0.2, 
                               color=self.colors['highlight'])
                
                # Añadir texto con el área
                ax.text(z_value+0.1, stats.norm.pdf(z_value), 
                       f'z = {z_value:.4f}\nárea = {area:.4f}', 
                       fontsize=9, color=self.colors['primary'])
        
        # Etiquetas y título
        ax.set_title('Distribución Normal Estándar', fontsize=12)
        ax.set_xlabel('z')
        ax.set_ylabel('f(z)')
        
        # Eliminar bordes del gráfico
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # Crear el lienzo para Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        
        return canvas.get_tk_widget()
    
    def create_t_plot(self, frame, df, t_value=None, area=None):
        """
        Crea un gráfico de la distribución t con los grados de libertad dados,
        opcionalmente marcando un valor t y sombreando el área
        """
        fig = Figure(figsize=(5, 3), dpi=100)
        fig.patch.set_facecolor(self.colors['background'])
        ax = fig.add_subplot(111)
        
        # Valores de x para la distribución t
        x = np.linspace(-4, 4, 1000)
        y = stats.t.pdf(x, df)
        
        # También graficar la distribución normal para comparación
        y_norm = stats.norm.pdf(x)
        
        # Gráficas base
        ax.plot(x, y, color=self.colors['primary'], label=f't ({df} g.l.)')
        ax.plot(x, y_norm, color=self.colors['secondary'], linestyle='--', 
               alpha=0.5, label='Normal estándar')
        ax.axhline(y=0, color=self.colors['secondary'], linestyle='-', alpha=0.3)
        ax.axvline(x=0, color=self.colors['secondary'], linestyle='-', alpha=0.3)
        
        # Si se proporciona un valor t, marcarlo en la gráfica
        if t_value is not None:
            # Punto t
            ax.plot([t_value], [stats.t.pdf(t_value, df)], 'o', 
                   color=self.colors['highlight'])
            ax.axvline(x=t_value, color=self.colors['highlight'], 
                      linestyle='--', alpha=0.6)
            
            # Sombrear el área si se proporciona
            if area is not None:
                fill_x = np.linspace(-4, t_value, 1000)
                fill_y = stats.t.pdf(fill_x, df)
                ax.fill_between(fill_x, fill_y, 0, alpha=0.2, 
                               color=self.colors['highlight'])
                
                # Añadir texto con el área
                ax.text(t_value+0.1, stats.t.pdf(t_value, df), 
                       f't = {t_value:.4f}\nárea = {area:.4f}', 
                       fontsize=9, color=self.colors['primary'])
        
        # Etiquetas y título
        ax.set_title(f'Distribución t-Student (df={df})', fontsize=12)
        ax.set_xlabel('t')
        ax.set_ylabel('f(t)')
        ax.legend(loc='best', fontsize=8)
        
        # Eliminar bordes del gráfico
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # Crear el lienzo para Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        
        return canvas.get_tk_widget()