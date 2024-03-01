import winreg as reg

def add_registry_entry(script_path):
    key_path = r"*\shell\WinGroundRm"
    command_key_path = r"*\shell\WinGroundRm\command"

    try:
        # Création des clés dans le registre
        key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
        command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path)

        # Définition de la valeur par défaut pour la clé principale
        reg.SetValue(key, "", reg.REG_SZ, "Remove Background image")

        # Définition de la valeur par défaut pour la clé de commande
        reg.SetValue(command_key, "", reg.REG_SZ, rf'"C:\Users\hp\AppData\Local\Programs\Python\Python311\pythonw.exe" "{script_path}" "%1"')

        # Fermeture des clés
        reg.CloseKey(key)
        reg.CloseKey(command_key)

        print("Option ajoutée avec succès !")

    except Exception as e:
        print(f"Erreur : {str(e)}")


if __name__ == "__main__":
    # Remplacez cela par le chemin absolu de votre script
    current_script_path = r"C:\Users\hp\Desktop\WinGroundRm\RemoveBack.py"

    # Ajout de l'entrée au registre
    add_registry_entry(current_script_path)
