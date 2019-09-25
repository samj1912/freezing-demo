# -*- mode: python ; coding: utf-8 -*-
import platform

block_cipher = None

os_name = platform.system()
if os_name == "Windows":
    binaries = [("*process*.pyd", ".")]
else:
    binaries = [("*process*.so", ".")]
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['cython-demo'],
             pathex=['/media/sam/Data/dev/freezing-demo'],
             binaries=binaries,
             datas=[],
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
          name='cython-demo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
