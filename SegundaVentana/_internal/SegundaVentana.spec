# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:/Trabajo de Grado Juan Argoti  2024/SegundaVentana.py'],
    pathex=[],
    binaries=[],
    datas=[('D:/Trabajo de Grado Juan Argoti  2024/scripts/*.py', 'scripts/'), ('D:/Trabajo de Grado Juan Argoti  2024/ui/*.ui', 'ui/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SegundaVentana',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
