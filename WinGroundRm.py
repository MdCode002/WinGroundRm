import winreg as reg
import os
from rembg import remove
from PIL import Image
import sys
key_path = r"*\shell\WinGroundRm"
command_key_path = r"*\shell\WinGroundRm\command"

def remove_background(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)

def registry_key_exists(key_path):
    """
    Vérifie si une clé du registre existe.

    :param key_path: Chemin de la clé du registre.
    :return: True si la clé existe, False sinon.
    """
    try:
        reg.OpenKey(reg.HKEY_CLASSES_ROOT, key_path)
        return True
    except FileNotFoundError:
        return False

def add_registry_entry(script_name):
    """
    Ajoute une entrée au registre pour le clic droit.

    :param script_name: Nom du script.
    :return: True si l'entrée existe déjà, False sinon.
    """
    
   

    if not registry_key_exists(key_path):
        try:
            pythonw_executable = os.path.join(sys.base_prefix, "pythonw.exe")
            key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
            command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path)

            reg.SetValue(key, "", reg.REG_SZ, "WinGroundRm remove Background image")
            script_dir = os.path.abspath(os.path.dirname(__file__))
            reg.SetValue(
                command_key,
                "",
                reg.REG_SZ,
                rf'"{pythonw_executable}" "{os.path.join(script_dir, script_name)}" "%1"',
            )
            remove_background(
            os.path.join(script_dir, "test.png"),
            os.path.join(script_dir, "test_result.png"),
        )
        except Exception as e:
            print(f"Erreur : {str(e)}")
            return False
        finally:
            reg.CloseKey(key)
            reg.CloseKey(command_key)
        
        
        print("Option ajoutée avec succès !")
        return False
    else:
        print("La clé du registre existe déjà.")
        return True

# ... (autres fonctions)

def main():
    """
    Fonction principale.
    """
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        output_path = os.path.splitext(file_path)[0] + "_no_background.png"
        remove_background(file_path, output_path)
    else:
        print("WinGround a déjà été installé!! ")
        print("Vous devez faire un clic droit sur une image ->  afficher d'autre options -> Enlever le background avec WinGroundRm")

if __name__ == "__main__":
    script_name = r"WinGroundRm.py"
    if add_registry_entry(script_name):
        main()
