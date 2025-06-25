import requests
import os
import sys
import subprocess

from tqdm import tqdm
from time import sleep

os.system('title Spotifinity PC - 1.0.0')
os.system('cls' if os.name == 'nt' else 'clear')
print(r'''                     __             _   _  __ _       _ _         
                    / _\_ __   ___ | |_(_)/ _(_)_ __ (_) |_ _   _ 
                    \ \| '_ \ / _ \| __| | |_| | '_ \| | __| | | |
                    _\ \ |_) | (_) | |_| |  _| | | | | | |_| |_| |
                    \__/ .__/ \___/ \__|_|_| |_|_| |_|_|\__|\__, |
                       |_|                                  |___/

               NIENTE PUBBLICITÀ | SKIP ILLIMITATI | SEMPRE AGGIORNATO
                        creato da @gocciolabtw - gocciola.xyz
                                    versione 1.0.0
      
Benvenuto!
Con questo script potrai installare Spotify Moddato in modo semplice e veloce.

La mod consente di rimuovere la pubblicità e di saltare le canzoni illimitatamente.
Inoltre, non viene visualizzato banner pubblicitari e tasti per abbonarsi.
      
Ti consiglio di disattivare temporaneamente l'antivirus, in quanto potrebbe segnalare la mod come virus.
''')
req = input("Vuoi iniziare l'installazione? (s,n): ").lower()
if req != 's':
    print("Installazione annullata.")
    exit()
elif req == 's':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Iniziamo!")

print()
print("===== Controllo dei requisiti...")
libraries = ['requests', 'tqdm']
for library in libraries:
    try:
        __import__(library)
    except ImportError:
        print(f"Sto installando {library}...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', library])

try:
    subprocess.run(['winget', '--version'], check=True)
except Exception as e:
    print("Winget non è stato installato sul sistema, deve essere installato per continuare.")
    print("Puoi installarlo sul Microsoft Store, si chiama 'App Installer'.")
    print("https://apps.microsoft.com/detail/9NBLGGH4NNS1")
    input("Premi un tasto per continuare...")
    exit()

print()
print("===== Controllo se Spotify è già installato...")
spotify_path = os.path.join(os.environ['APPDATA'], 'Spotify')
spicetify_path = os.path.join(os.environ['APPDATA'], 'spicetify')
if os.path.exists(spotify_path):
    try:
        subprocess.run(['taskkill', '/F', '/IM', 'Spotify.exe'], check=False)
        subprocess.run([os.path.join(spotify_path, 'Spotify.exe'), '/uninstall', '/silent'], check=True)
        print("Spotify disinstallato correttamente.")
    except Exception as e:
        print("Non sono riuscito a disinstallare Spotify. Prova a farlo manualmente.")
        print(e)
        input("Premi un tasto per continuare...")
        exit()
if os.path.exists(spicetify_path):
    try:
        subprocess.run(['winget', 'uninstall', 'Spicetify.Spicetify'], check=False)
    except Exception as e:
        print("Non sono riuscito a disinstallare Spicetify. Prova a farlo manualmente.")
        print(e)
        input("Premi un tasto per continuare...")
        exit()

url = "https://download.scdn.co/SpotifyFullSetupX64.exe"
installer_path = os.path.join(os.environ['TEMP'], "SpotifySetup.exe")

print()
print("===== Download dell'ultima versione dell'installer di Spotify...")

response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))

with open(installer_path, 'wb') as file:
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)
    for data in response.iter_content(chunk_size=1024):
        file.write(data)
        progress_bar.update(len(data))
    progress_bar.close()

print()
print("===== Fatto, installazione di Spotify in corso...")
try:
    subprocess.run([installer_path, '/silent'], check=True)
    print("Spotify installato correttamente.")
    print()
    print("===== Ora installo la mod...")
except Exception as e:
    print("Non sono riuscito a installare Spotify. Prova a farlo manualmente.")
    print(e)
    input("Premi un tasto per continuare...")
    exit()
finally:
    if os.path.exists(installer_path):
        os.remove(installer_path)

subprocess.run(['winget', 'install', 'Spicetify.Spicetify'], check=True)

print()
print("===== Aspetto un po' che Spotify carichi...")
sleep(1)
subprocess.run(['taskkill', '/F', '/IM', 'Spotify.exe'], check=False)

print()
print("===== Creazione di un backup per non fare casini...")
subprocess.run(['spicetify', 'backup', 'apply'], check=True)
subprocess.run(['taskkill', '/F', '/IM', 'Spotify.exe'], check=False)

mods = [
    "https://raw.githubusercontent.com/rxri/spicetify-extensions/refs/heads/main/adblock/adblock.js"
]

print()
print("===== Download delle mod...")
for mod in mods:
    filename = os.path.basename(mod)
    filepath = os.path.join(os.environ['APPDATA'], 'spicetify', 'Extensions', filename)
    response = requests.get(mod, stream=True)
    with open(filepath, 'wb') as file:
        progress_bar = tqdm(total=int(response.headers.get('content-length', 0)), unit='B', unit_scale=True)
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            progress_bar.update(len(data))
        progress_bar.close()

print()
print("===== Applico le mod...")
subprocess.run(['spicetify', 'apply'], check=True)
subprocess.run(['taskkill', '/F', '/IM', 'Spotify.exe'], check=False)

print()
print("===== Mod applicate correttamente!")
print("Ora puoi avviare Spotify e goderti la tua esperienza senza pubblicità!")
print("Se hai aggiornato Spotify, ti consiglio di rieseguire questo script per aggiornare le mod.")
print()
input("Premi un tasto per continuare...")
exit()