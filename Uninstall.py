import os
import shutil
import winreg as reg

def remove_model():
    model_path = os.path.join(os.path.expanduser("~"), ".u2net")
    if os.path.exists(model_path):
        try:
            shutil.rmtree(model_path)
            print("Modèle U2Net supprimé avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression du modèle : {str(e)}")
    else:
        print("Le modèle U2Net n'a pas été trouvé.")

def remove_registry_entries():
    key_path = r"*\shell\WinGroundRm"
    command_key_path = r"*\shell\WinGroundRm\command"

    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, command_key_path)
        print("Clé du registre 'command' supprimée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression de la clé 'command' : {str(e)}")

    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        print("Clé du registre 'WinGroundRm' supprimée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression de la clé 'WinGroundRm' : {str(e)}")

def main():
    remove_model()
    remove_registry_entries()

if __name__ == "__main__":
    main()