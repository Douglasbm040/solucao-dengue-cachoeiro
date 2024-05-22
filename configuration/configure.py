import adminstrador_libs as adm_lib
import bot_download_dados as bot_drive
import instalador as itl

# Lista de bibliotecas que você deseja instalar
LIBRARIES = ['pandas', 'numpy', 'matplotlib', 'seaborn','python-dotenv']
LIBRARIES_DRIVE = ['selenium','patoolib']

INSTALAR_LIBS = True
BAIXAR_GOOGLE_DRIVE = True
INSTALDO_FIREFOX_e_MARIONETE = False


if INSTALAR_LIBS:
    adm_lib.install(LIBRARIES)


if BAIXAR_GOOGLE_DRIVE:
    adm_lib.install(LIBRARIES_DRIVE)
    if INSTALDO_FIREFOX_e_MARIONETE:
        bot_drive.execute()
    else:
        itl.execute()





