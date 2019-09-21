# -*- mode: python ; coding: utf-8 -*-
import platform

block_cipher = None


a = Analysis(
    ["demo.py"],
    pathex=["/media/sam/Data/dev/freezing-demo"],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="demo",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
if platform.system() == "Darwin":
    info_plist = {
        "NSHighResolutionCapable": "True",
        "NSPrincipalClass": "NSApplication",
        "CFBundleName": "demo",
        "CFBundleDisplayName": "demo",
    }
    app = BUNDLE(exe, name="demo.app", bundle_identifier=None, info_plist=info_plist)
