#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Programa Estadístico para Distribuciones Z y T
Desarrollado para estudiantes de preparatoria
"""

import tkinter as tk
from gui.app import EstadisticaApp

if __name__ == "__main__":
    root = tk.Tk()
    app = EstadisticaApp(root)
    root.mainloop()