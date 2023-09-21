# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


import os
import sys

# ...

a = Analysis(
    ['cubematchfinance/__main__.py'], 
    pathex=[],
    binaries=[],
    datas=[
        ('requirements.txt', '.'),
        (os.path.join('assets', 'images', '*.png'), 'assets/images'), 
        (os.path.join('assets', 'images', '*.ico'), 'assets/images') 
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

# ...


pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher,
          additional_files=[
              (os.path.join('cubematchfinance', '__main__.py'), '__main__.py')
          ])

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
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
    name='main',
)
