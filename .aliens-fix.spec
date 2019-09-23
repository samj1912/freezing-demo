# -*- mode: python ; coding: utf-8 -*-
import platform
block_cipher = None


a = Analysis(['.aliens-fix.py'],
             pathex=['/media/sam/Data/dev/freezing-demo'],
             binaries=[],
             datas=[('data', 'data')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='aliens',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

info_plist = {
    "NSHighResolutionCapable": "True",
    "NSPrincipalClass": "NSApplication",
    "CFBundleName": "aliens",
    "CFBundleDisplayName": "aliens",
}

app = BUNDLE(exe, name="aliens.app", bundle_identifier=None, info_plist=info_plist)
