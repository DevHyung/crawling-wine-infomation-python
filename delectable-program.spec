# -*- mode: python -*-

block_cipher = None


a = Analysis(['delectable-program.py'],
             pathex=['D:\\ProjPy3\\Å©¸ù¿ÜÁÖ\\wine-scrapping'],
             binaries=[],
             datas=[],
             hiddenimports=['bs4','selenium','os','openpyxl','lxml'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='delectable-program',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='favi.ico')
