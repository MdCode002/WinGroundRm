import winreg as reg
import os
from rembg import remove
from PIL import Image
import sys


def registry_key_exists(key_path):
    try:
        reg.OpenKey(reg.HKEY_CLASSES_ROOT, key_path)
        return True
    except FileNotFoundError:
        return False


def add_registry_entry(script_name):
    key_path = r"*\shell\WinGroundRm"
    command_key_path = r"*\shell\WinGroundRm\command"
    pythonw_executable = os.path.join(sys.base_prefix, "pythonw.exe")

    if not registry_key_exists(key_path):
        try:
            # Création des clés dans le registre
            key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
            command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path)

            # Définition de la valeur par défaut pour la clé principale
            reg.SetValue(key, "", reg.REG_SZ, "WinGroundRm remove Background image")
            script_dir = os.path.abspath(os.path.dirname(__file__))
            # Définition de la valeur par défaut pour la clé de commande
            reg.SetValue(
                command_key,
                "",
                reg.REG_SZ,
                rf'"{pythonw_executable}" "{os.path.join(script_dir, script_name)}" "%1"',
            )

            # Fermeture des clés
            reg.CloseKey(key)
            reg.CloseKey(command_key)
            remove_background(
                os.path.join(script_dir, "test.png"),
                os.path.join(script_dir, "test_result.png"),
            )
            print("Option ajoutée avec succès !")
            return False

        except Exception as e:
            print(f"Erreur : {str(e)}")
            return False
    else:
        print("La clé du registre existe déjà.")
        return True


def remove_background(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)


def main():
    # Récupération du chemin du fichier sur lequel le clic droit a été effectué
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

        # Création du chemin de sortie pour l'image modifiée
        output_path = os.path.splitext(file_path)[0] + "_no_background.png"

        # Suppression de l'arrière-plan de l'image et sauvegarde
        remove_background(file_path, output_path)
    else:
        print("WinGround a déjà été installé!! Vous devez faire un clic droit sur une image pour enlever le background.")


if __name__ == "__main__":
    # Remplacez cela par le chemin absolu de votre script
    script_name = r"WinGroundRm.py"

    # Ajout de l'entrée au registre si elle n'existe pas déjà
    if add_registry_entry(script_name):
        main()
    # Appel de la fonction principale
