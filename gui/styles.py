# -*- coding: utf-8 -*-

"""
Definiciones de estilos y colores para la interfaz gráfica
"""

class AppStyles:
    def __init__(self):
        # Colores
        self.colors = {
            'background': '#F5F5F5',      # Fondo gris muy claro
            'text': '#333333',            # Texto gris oscuro
            'accent': '#2C3E50',          # Acento azul oscuro neutro
            'button': '#607D8B',          # Botones gris azulado
            'button_hover': '#455A64',    # Hover de botones más oscuro
            'frame_bg': '#FFFFFF',        # Fondo de frames blanco
            'separator': '#CCCCCC',       # Separadores gris claro
            'highlight': '#4CAF50',       # Resaltado verde suave
            'warning': '#FFC107',         # Advertencia amarillo suave
            'error': '#F44336'            # Error rojo suave
        }
        
        # Fuentes
        self.fonts = {
            'title': ('Segoe UI', 16, 'bold'),
            'header': ('Segoe UI', 14, 'bold'),
            'subheader': ('Segoe UI', 12, 'bold'),
            'body': ('Segoe UI', 10),
            'small': ('Segoe UI', 8),
            'button': ('Segoe UI', 10, 'bold')
        }
        
        # Padding y márgenes
        self.padding = {
            'small': 5,
            'medium': 10,
            'large': 15,
            'xl': 20
        }

    def configure_widgets(self, root):
        """
        Configura los estilos por defecto para todos los widgets
        """
        root.configure(bg=self.colors['background'])
        
        # Estilos para botones
        button_style = {
            'bg': self.colors['button'],
            'fg': '#FFFFFF',
            'font': self.fonts['button'],
            'padx': self.padding['medium'],
            'pady': self.padding['small'],
            'relief': 'flat',
            'borderwidth': 0
        }
        
        # Estilos para etiquetas
        label_style = {
            'bg': self.colors['background'],
            'fg': self.colors['text'],
            'font': self.fonts['body']
        }
        
        # Estilos para entradas
        entry_style = {
            'bg': self.colors['frame_bg'],
            'fg': self.colors['text'],
            'font': self.fonts['body'],
            'relief': 'flat',
            'borderwidth': 1
        }
        
        # Configurar estilos por defecto usando la opción option_add
        root.option_add('*Button.background', button_style['bg'])
        root.option_add('*Button.foreground', button_style['fg'])
        root.option_add('*Button.font', button_style['font'])
        root.option_add('*Button.relief', button_style['relief'])
        root.option_add('*Button.borderwidth', button_style['borderwidth'])
        
        root.option_add('*Label.background', label_style['bg'])
        root.option_add('*Label.foreground', label_style['fg'])
        root.option_add('*Label.font', label_style['font'])
        
        root.option_add('*Entry.background', entry_style['bg'])
        root.option_add('*Entry.foreground', entry_style['fg'])
        root.option_add('*Entry.font', entry_style['font'])
        root.option_add('*Entry.relief', entry_style['relief'])
        root.option_add('*Entry.borderwidth', entry_style['borderwidth'])
        
        # Configurar frames
        root.option_add('*Frame.background', self.colors['background'])
        
        return root