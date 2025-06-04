# -*- coding: utf-8 -*-

"""
Frame para trabajar con la distribución t
"""

import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys

# Agregar rutas de los módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from core.t_distribution import TDistribution
from core.plotting import StatPlotter

class TFrame(tk.Frame):
    def __init__(self, parent, styles):
        super().__init__(parent, bg=styles.colors['background'])
        self.styles = styles
        self.t_dist = TDistribution()
        self.plotter = StatPlotter()
        
        # Variables para entrada de datos
        self.df_value = tk.StringVar(value="10")  # Valor predeterminado
        self.t_value = tk.StringVar()
        self.alpha_value = tk.StringVar()
        self.result_text = tk.StringVar(value="Resultados aparecerán aquí")
        self.use_complement = tk.BooleanVar(value=False)  # Para usar 1-alpha
        
        # Crear widgets
        self.create_widgets()
        
        # Gráfico inicial
        self.update_plot()
    
    def create_widgets(self):
        """Crea los elementos de la interfaz para la distribución t"""
        # Título
        title_label = tk.Label(
            self, 
            text="Distribución t de Student",
            font=self.styles.fonts['title'],
            bg=self.styles.colors['background']
        )
        title_label.pack(pady=(20, 10))
        
        # Frame para los controles
        controls_frame = tk.Frame(self, bg=self.styles.colors['background'])
        
        # Frame para grados de libertad (común para ambos cálculos)
        df_frame = tk.LabelFrame(
            controls_frame, 
            text="Grados de Libertad",
            bg=self.styles.colors['frame_bg'],
            font=self.styles.fonts['subheader']
        )
        
        # Entrada para grados de libertad
        df_label = tk.Label(
            df_frame, 
            text="Grados de libertad (v):",
            bg=self.styles.colors['frame_bg']
        )
        df_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        df_entry = tk.Entry(
            df_frame,
            textvariable=self.df_value,
            width=10
        )
        df_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        
        # Información sobre grados de libertad
        df_info_button = tk.Button(
            df_frame,
            text="?",
            width=2,
            command=self.show_df_help
        )
        df_info_button.grid(row=0, column=2, padx=5, pady=10)
        
        # Posicionar frame de grados de libertad
        df_frame.pack(fill='x', padx=10, pady=10)
        
        # Sección para calcular alpha dado t
        t_frame = tk.LabelFrame(
            controls_frame, 
            text="Calcular área (alpha) dado un valor t",
            bg=self.styles.colors['frame_bg'],
            font=self.styles.fonts['subheader']
        )
        
        # Entrada para t
        t_label = tk.Label(
            t_frame, 
            text="Valor t:",
            bg=self.styles.colors['frame_bg']
        )
        t_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        t_entry = tk.Entry(
            t_frame,
            textvariable=self.t_value,
            width=10
        )
        t_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        
        # Botón para calcular alpha
        calc_alpha_button = tk.Button(
            t_frame,
            text="Calcular área",
            command=self.calculate_alpha
        )
        calc_alpha_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Posicionar frame de t
        t_frame.pack(fill='x', padx=10, pady=10)
        
        # Sección para calcular t dado alpha
        alpha_frame = tk.LabelFrame(
            controls_frame, 
            text="Calcular valor t dado un área (alpha)",
            bg=self.styles.colors['frame_bg'],
            font=self.styles.fonts['subheader']
        )
        
        # Entrada para alpha
        alpha_label = tk.Label(
            alpha_frame, 
            text="Valor Alpha:",
            bg=self.styles.colors['frame_bg']
        )
        alpha_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        alpha_entry = tk.Entry(
            alpha_frame,
            textvariable=self.alpha_value,
            width=10
        )
        alpha_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        
        # Checkbox para usar 1-alpha
        complement_check = tk.Checkbutton(
            alpha_frame,
            text="Usar 1-alpha (cola derecha)",
            variable=self.use_complement,
            bg=self.styles.colors['frame_bg'],
            activebackground=self.styles.colors['frame_bg']
        )
        complement_check.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10), sticky='w')
        
        # Añadir información sobre 1-alpha
        info_label = tk.Label(
            alpha_frame,
            text="Nota: Use 1-alpha para obtener el valor en la cola derecha de la distribución",
            bg=self.styles.colors['frame_bg'],
            fg=self.styles.colors['accent'],
            font=self.styles.fonts['small'],
            justify='left'
        )
        info_label.grid(row=2, column=0, columnspan=3, padx=10, pady=(0, 10), sticky='w')
        
        # Botón para calcular t
        calc_t_button = tk.Button(
            alpha_frame,
            text="Calcular t",
            command=self.calculate_t
        )
        calc_t_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Posicionar frame de alpha
        alpha_frame.pack(fill='x', padx=10, pady=10)
        
        # Posicionar frame de controles
        controls_frame.pack(fill='x', padx=10, pady=0)
        
        # Frame para resultados
        results_frame = tk.LabelFrame(
            self, 
            text="Resultados",
            bg=self.styles.colors['frame_bg'],
            font=self.styles.fonts['subheader']
        )
        
        # Etiqueta para mostrar resultados
        result_label = tk.Label(
            results_frame,
            textvariable=self.result_text,
            bg=self.styles.colors['frame_bg'],
            justify='left',
            wraplength=700
        )
        result_label.pack(padx=10, pady=10, fill='x')
        
        # Posicionar frame de resultados
        results_frame.pack(fill='x', padx=10, pady=10)
        
        # Frame para el gráfico
        self.plot_frame = tk.Frame(self, bg=self.styles.colors['frame_bg'])
        self.plot_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    def show_df_help(self):
        """Muestra ayuda sobre grados de libertad"""
        help_text = """
Grados de Libertad (v):

En estadística, los grados de libertad representan el número de valores 
que pueden variar libremente en el cálculo final.

Casos comunes:
- Para una muestra simple: v = n - 1 (donde n es tamaño de muestra)
- Para comparación de dos muestras: v = n₁ + n₂ - 2
- Para ANOVA con k grupos: v₁ = k - 1, v₂ = N - k

Ejemplos:
- Prueba t con una muestra de 15 datos: v = 14
- Prueba t con dos muestras de 10 datos cada una: v = 18
        """
        messagebox.showinfo("Grados de Libertad", help_text)
    
    def calculate_alpha(self):
        """Calcular el área (alpha) dado un valor t y grados de libertad"""
        try:
            t_val = float(self.t_value.get())
            df_val = int(self.df_value.get())
            
            if df_val <= 0:
                messagebox.showerror(
                    "Error", 
                    "Los grados de libertad deben ser un número entero positivo."
                )
                return
            
            # Calcular alpha usando la distribución t
            alpha = self.t_dist.calculate_area(t_val, df_val)
            
            # Calcular también el valor complemento (1-alpha)
            alpha_complement = 1 - alpha
            
            # También calcular usando integración numérica
            alpha_integral = self.t_dist.calculate_area_integral(t_val, df_val)
            
            # Actualizar texto de resultados
            self.result_text.set(
                f"Para t = {t_val} con {df_val} grados de libertad:\n" + 
                f"Área (alpha) = {alpha:.8f}\n" +
                f"Complemento (1-alpha) = {alpha_complement:.8f}\n" +
                f"Área (integración numérica) = {alpha_integral:.8f}\n\n" +
                f"Interpretación: La probabilidad de que una variable aleatoria t con {df_val} " +
                f"grados de libertad sea menor o igual que {t_val} es {alpha:.8f} o {alpha*100:.4f}%.\n" +
                f"La probabilidad de que sea mayor que {t_val} es {alpha_complement:.8f} o {alpha_complement*100:.4f}%."
            )
            
            # Actualizar gráfico
            self.update_plot(df_val, t_val, alpha)
            
        except ValueError:
            messagebox.showerror(
                "Error", 
                "Ingrese valores numéricos válidos para t y grados de libertad."
            )
            
    def calculate_t(self):
        """Calcular el valor t dado un área (alpha) y grados de libertad"""
        try:
            alpha_val = float(self.alpha_value.get())
            df_val = int(self.df_value.get())
            
            if df_val <= 0:
                messagebox.showerror(
                    "Error", 
                    "Los grados de libertad deben ser un número entero positivo."
                )
                return
            
            if alpha_val <= 0 or alpha_val >= 1:
                messagebox.showerror(
                    "Error", 
                    "El valor de alpha debe estar entre 0 y 1."
                )
                return
            
            # Usar complemento si está marcado
            if self.use_complement.get():
                # Si queremos usar 1-alpha, entonces buscamos el valor t para el cual
                # P(T >= t) = alpha_val, que es equivalente a P(T <= t) = 1-alpha_val
                effective_alpha = 1 - alpha_val
                t_val = self.t_dist.calculate_t_for_alpha(effective_alpha, df_val)
                
                # Actualizar texto de resultados
                self.result_text.set(
                    f"Para un área en cola derecha (1-alpha) = {alpha_val} con {df_val} grados de libertad:\n" + 
                    f"El valor t = {t_val:.8f}\n\n" +
                    f"Interpretación: El {alpha_val*100:.4f}% de los valores en una distribución " +
                    f"t con {df_val} grados de libertad son mayores que {t_val:.8f}."
                )
                
                # Actualizar gráfico (mostrando el área como 1-alpha_val)
                self.update_plot(df_val, t_val, effective_alpha, is_right_tail=True)
            else:
                # Calcular t normalmente
                t_val = self.t_dist.calculate_t_for_alpha(alpha_val, df_val)
                
                # Actualizar texto de resultados
                self.result_text.set(
                    f"Para un área (alpha) = {alpha_val} con {df_val} grados de libertad:\n" + 
                    f"El valor t = {t_val:.8f}\n\n" +
                    f"Interpretación: El {alpha_val*100:.4f}% de los valores en una distribución " +
                    f"t con {df_val} grados de libertad son menores o iguales a {t_val:.8f}."
                )
                
                # Actualizar gráfico
                self.update_plot(df_val, t_val, alpha_val)
            
        except ValueError:
            messagebox.showerror(
                "Error", 
                "Ingrese valores numéricos válidos para alpha y grados de libertad."
            )
    
    def update_plot(self, df=10, t_value=None, area=None, is_right_tail=False):
        """Actualiza el gráfico de la distribución t"""
        try:
            # Si no se especifica df, usar el valor del campo
            if not df:
                df = int(self.df_value.get())
                
            # Limpiar frame anterior
            for widget in self.plot_frame.winfo_children():
                widget.destroy()
            
            # Crear nuevo gráfico
            plot_widget = self.plotter.create_t_plot(self.plot_frame, df, t_value, area, is_right_tail)
            
            # Colocar el gráfico en el frame
            plot_widget.pack(fill='both', expand=True)
        except ValueError:
            # Si hay un error, usar valor predeterminado
            df = 10
            
            # Limpiar frame anterior
            for widget in self.plot_frame.winfo_children():
                widget.destroy()
            
            # Crear nuevo gráfico
            plot_widget = self.plotter.create_t_plot(self.plot_frame, df)
            
            # Colocar el gráfico en el frame
            plot_widget.pack(fill='both', expand=True)