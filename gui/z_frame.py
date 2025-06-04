# -*- coding: utf-8 -*-

"""
Frame para trabajar con la distribución normal estándar (Z)
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

from core.z_distribution import ZDistribution
from core.plotting import StatPlotter

class ZFrame(tk.Frame):
    def __init__(self, parent, styles):
        super().__init__(parent, bg=styles.colors['background'])
        self.styles = styles
        self.z_dist = ZDistribution()
        self.plotter = StatPlotter()
        
        # Variables para entrada de datos
        self.z_value = tk.StringVar()
        self.alpha_value = tk.StringVar()
        self.result_text = tk.StringVar(value="Resultados aparecerán aquí")
        self.use_complement = tk.BooleanVar(value=False)  # Para usar 1-alpha
        
        # Crear widgets
        self.create_widgets()
        
        # Gráfico inicial
        self.update_plot()
    
    def create_widgets(self):
        """Crea los elementos de la interfaz para la distribución Z"""
        # Título
        title_label = tk.Label(
            self, 
            text="Distribución Normal Estándar (Z)",
            font=self.styles.fonts['title'],
            bg=self.styles.colors['background']
        )
        title_label.pack(pady=(20, 10))
        
        # Frame para los controles
        controls_frame = tk.Frame(self, bg=self.styles.colors['background'])
        
        # Sección para calcular alpha dado Z
        z_frame = tk.LabelFrame(
            controls_frame, 
            text="Calcular área (alpha) dado un valor Z",
            bg=self.styles.colors['frame_bg'],
            font=self.styles.fonts['subheader']
        )
        
        # Entrada para Z
        z_label = tk.Label(
            z_frame, 
            text="Valor Z:",
            bg=self.styles.colors['frame_bg']
        )
        z_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        z_entry = tk.Entry(
            z_frame,
            textvariable=self.z_value,
            width=10
        )
        z_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        
        # Botón para calcular alpha
        calc_alpha_button = tk.Button(
            z_frame,
            text="Calcular área",
            command=self.calculate_alpha
        )
        calc_alpha_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Posicionar frame de Z
        z_frame.pack(fill='x', padx=10, pady=10)
        
        # Sección para calcular Z dado alpha
        alpha_frame = tk.LabelFrame(
            controls_frame, 
            text="Calcular valor Z dado un área (alpha)",
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
        
        # Botón para calcular Z
        calc_z_button = tk.Button(
            alpha_frame,
            text="Calcular Z",
            command=self.calculate_z
        )
        calc_z_button.grid(row=0, column=2, padx=10, pady=10)
        
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
    
    def calculate_alpha(self):
        """Calcular el área (alpha) dado un valor Z"""
        try:
            z_val = float(self.z_value.get())
            
            # Calcular alpha usando la distribución normal
            alpha = self.z_dist.calculate_area(z_val)
            
            # También calcular usando integración numérica
            alpha_integral = self.z_dist.calculate_area_integral(z_val)
            
            # Calcular también el valor complemento (1-alpha)
            alpha_complement = 1 - alpha
            
            # Actualizar texto de resultados
            self.result_text.set(
                f"Para Z = {z_val}:\n" + 
                f"Área (alpha) = {alpha:.8f}\n" +
                f"Complemento (1-alpha) = {alpha_complement:.8f}\n" +
                f"Área (integración numérica) = {alpha_integral:.8f}\n\n" +
                f"Interpretación: La probabilidad de que una variable aleatoria normal estándar " +
                f"sea menor o igual que {z_val} es {alpha:.8f} o {alpha*100:.4f}%.\n" +
                f"La probabilidad de que sea mayor que {z_val} es {alpha_complement:.8f} o {alpha_complement*100:.4f}%."
            )
            
            # Actualizar gráfico
            self.update_plot(z_val, alpha)
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido para Z.")
            
    def calculate_z(self):
        """Calcular el valor Z dado un área (alpha)"""
        try:
            alpha_val = float(self.alpha_value.get())
            
            if alpha_val <= 0 or alpha_val >= 1:
                messagebox.showerror(
                    "Error", 
                    "El valor de alpha debe estar entre 0 y 1."
                )
                return
            
            # Usar complemento si está marcado
            if self.use_complement.get():
                # Si queremos usar 1-alpha, entonces buscamos el valor Z para el cual
                # P(Z >= z) = alpha_val, que es equivalente a P(Z <= z) = 1-alpha_val
                effective_alpha = 1 - alpha_val
                z_val = self.z_dist.calculate_z_for_alpha(effective_alpha)
                
                self.result_text.set(
                    f"Para un área en cola derecha (1-alpha) = {alpha_val}:\n" + 
                    f"El valor Z = {z_val:.8f}\n\n" +
                    f"Interpretación: El {alpha_val*100:.4f}% de los valores en una distribución " +
                    f"normal estándar son mayores que {z_val:.8f}."
                )
                
                # Actualizar gráfico (mostrando el área como 1-alpha_val)
                self.update_plot(z_val, effective_alpha, is_right_tail=True)
            else:
                # Calcular Z normalmente
                z_val = self.z_dist.calculate_z_for_alpha(alpha_val)
                
                # Actualizar texto de resultados
                self.result_text.set(
                    f"Para un área (alpha) = {alpha_val}:\n" + 
                    f"El valor Z = {z_val:.8f}\n\n" +
                    f"Interpretación: El {alpha_val*100:.4f}% de los valores en una distribución " +
                    f"normal estándar son menores o iguales a {z_val:.8f}."
                )
                
                # Actualizar gráfico
                self.update_plot(z_val, alpha_val)
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido para alpha.")
    
    def update_plot(self, z_value=None, area=None, is_right_tail=False):
        """Actualiza el gráfico de la distribución normal"""
        # Limpiar frame anterior
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        
        # Crear nuevo gráfico
        plot_widget = self.plotter.create_z_plot(self.plot_frame, z_value, area, is_right_tail)
        
        # Colocar el gráfico en el frame
        plot_widget.pack(fill='both', expand=True)