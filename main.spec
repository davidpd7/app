# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import os

# Nombre del archivo principal (__main__.py)
main_script = 'cubematchfinance/__main__.py'

a = Analysis(
    [main_script],
    pathex=[],
    binaries=[],
    datas=[
        ('requirements.txt', '.'),
        ('cubematchfinance/assets/config/config.py', 'assets/config'),
        ('cubematchfinance/assets/config/config.json', 'assets/config'),
        ('cubematchfinance/assets/images/*.png', 'assets/images'),
        ('cubematchfinance/assets/images/*.ico', 'assets/images'),
        ('cubematchfinance/entities/tabs.py', 'entities')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher,
          additional_files=[
              (main_script, '__main__.py')
          ])

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='cubematchfinance',  
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='cubematchfinance',
)
