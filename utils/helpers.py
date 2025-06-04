# -*- coding: utf-8 -*-

"""
Funciones de utilidad para la aplicación
"""

def format_number(number, precision=6):
    """
    Formatea un número para mostrar solo los decimales necesarios
    hasta la precisión especificada
    """
    if isinstance(number, float):
        # Convertir a string con la precisión especificada
        str_num = f"{number:.{precision}f}"
        
        # Eliminar ceros finales y punto decimal si son innecesarios
        str_num = str_num.rstrip('0').rstrip('.') if '.' in str_num else str_num
        
        return str_num
    return str(number)