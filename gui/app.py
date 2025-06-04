# -*- coding: utf-8 -*-

"""
Ventana principal de la aplicación
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

from gui.styles import AppStyles
from gui.z_frame import ZFrame
from gui.t_frame import TFrame

class EstadisticaApp:
    def __init__(self, root):
        self.root = root
        self.styles = AppStyles()
        
        # Configurar la ventana principal
        self.setup_window()
        
        # Inicializar la interfaz
        self.create_widgets()
    
    def setup_window(self):
        """Configura las propiedades de la ventana principal"""
        self.root.title("Calculadora de Distribuciones Estadísticas")
        self.root.geometry("800x700")
        self.root.minsize(800, 700)
        
        # Aplicar estilos
        self.root = self.styles.configure_widgets(self.root)
        
        # Centrar la ventana en la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 800) // 2
        y = (screen_height - 600) // 2
        self.root.geometry(f"800x600+{x}+{y}")
    
    def create_widgets(self):
        """Crea los elementos de la interfaz"""
        # Crear un notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        
        # Pestaña para distribución Z
        self.z_frame = ZFrame(self.notebook, self.styles)
        
        # Pestaña para distribución t
        self.t_frame = TFrame(self.notebook, self.styles)
        
        # Agregar pestañas al notebook
        self.notebook.add(self.z_frame, text="Distribución Z")
        self.notebook.add(self.t_frame, text="Distribución t")
        
        # Colocar notebook en la ventana
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Crear frame para mensajes de información (sin botón de ayuda)
        self.info_frame = tk.Frame(self.root, bg=self.styles.colors['background'])
        
        # Mensajes de estado
        self.status_label = tk.Label(
            self.info_frame, 
            text="Listo para calcular",
            bg=self.styles.colors['background']
        )
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Colocar el frame de información
        self.info_frame.pack(fill='x', padx=10, pady=5)