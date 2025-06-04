# -*- mode: python ; coding: utf-8 -*-

import sys
import os
from PyInstaller.utils.hooks import collect_all

block_cipher = None

# Directorio base del proyecto (usando ruta absoluta directamente)
project_dir = os.path.abspath(os.getcwd())  # Usar el directorio de trabajo actual

# Recolectar todos los datos necesarios de los paquetes
datas = []
binaries = []
hiddenimports = ['numpy', 'matplotlib', 'scipy.stats', 'pandas', 'scipy.integrate', 'tkinter']

# Recolectar datos adicionales de matplotlib, numpy, scipy
for package in ['matplotlib', 'numpy', 'scipy']:
    tmp_datas, tmp_binaries, tmp_hiddenimports = collect_all(package)
    datas.extend(tmp_datas)
    binaries.extend(tmp_binaries)
    hiddenimports.extend(tmp_hiddenimports)

# Añadir README.md solo si existe
readme_path = os.path.join(project_dir, 'README.md')
if os.path.exists(readme_path):
    datas.append((readme_path, '.'))
else:
    print(f"Advertencia: No se encontró README.md en {project_dir}, se omitirá")
    # Crear un README básico
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# Calculadora de Distribuciones Estadísticas\n\n")
        f.write("Aplicación para cálculos estadísticos usando distribuciones Z y t.\n")
        f.write("Desarrollado para estudiantes de preparatoria.\n")
    datas.append((readme_path, '.'))

# Buscar el script main.py
main_path = os.path.join(project_dir, 'main.py')
if not os.path.exists(main_path):
    raise FileNotFoundError(f"No se encontró el archivo main.py en {project_dir}")

a = Analysis(
    [main_path],  # Usamos la ruta completa
    pathex=[project_dir],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='EstadisticaApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Cambiar a True para ver errores durante la ejecución
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='EstadisticaApp',
)