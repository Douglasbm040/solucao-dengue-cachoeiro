import subprocess

def install(libraries):
# Loop para instalar cada biblioteca
    for lib in libraries:
        subprocess.call(['pip3', 'install', lib])