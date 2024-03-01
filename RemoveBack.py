import os
from rembg import remove
from PIL import Image
import sys

def remove_background(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)

def main():
    # Récupération du chemin du fichier sur lequel le clic droit a été effectué
    file_path = sys.argv[1]

    # Création du chemin de sortie pour l'image modifiée
    output_path = os.path.splitext(file_path)[0] + "_no_background.png"

    # Suppression de l'arrière-plan de l'image et sauvegarde
    remove_background(file_path, output_path)

if __name__ == "__main__":
    main()
