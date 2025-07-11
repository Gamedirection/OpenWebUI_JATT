# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['openwebui_gui_converter.py'],
    pathex=[],
    binaries=[],
    datas=[('app_icon.icns', '.')],
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
    name='OpenWebUI Chat Exporter',
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
    icon=['app_icon.icns'],
)
app = BUNDLE(
    exe,
    name='OpenWebUI Chat Exporter.app',
    icon='app_icon.icns',
    bundle_identifier='com.gameDirection.openwebuiconverter',
)
