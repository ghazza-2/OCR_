import cv2
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

# Si Tesseract n'est pas dans votre PATH, spécifiez son emplacement
# Exemple pour Windows :
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def traiter_image(chemin_image):
    """Fonction pour traiter l'image et extraire le texte"""
    
    # 1. Charger l'image avec OpenCV
    image = cv2.imread(chemin_image)
    if image is None:
        print("Erreur: Impossible de charger l'image")
        return
    
    # Convertir de BGR (OpenCV) à RGB (pour l'affichage)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 2. Afficher l'image originale
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Image Originale")
    plt.axis('off')
    
    # 3. Convertir en niveaux de gris
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.subplot(2, 2, 2)
    plt.imshow(gris, cmap='gray')
    plt.title("Niveaux de Gris")
    plt.axis('off')
    
    # 4. Seuillage (binarisation) pour améliorer la détection de texte
    _, binaire = cv2.threshold(gris, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    plt.subplot(2, 2, 3)
    plt.imshow(binaire, cmap='gray')
    plt.title("Image Binarisée")
    plt.axis('off')
    
    # 5. Extraire le texte avec Tesseract
    texte = pytesseract.image_to_string(binaire, lang='eng')  # 'fra' pour français
    
    # 6. Afficher le texte extrait
    print("\nTexte extrait de l'image:")
    print("------------------------")
    print(texte)
    print("------------------------")
    
    # 7. Afficher l'image avec les zones de texte détectées
    # Détection des boîtes autour du texte
    boites = pytesseract.image_to_boxes(binaire, lang='eng')
    image_boites = image_rgb.copy()
    h, w, _ = image_boites.shape
    
    for b in boites.splitlines():
        b = b.split()
        x1, y1, x2, y2 = int(b[1]), h - int(b[2]), int(b[3]), h - int(b[4])
        cv2.rectangle(image_boites, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    plt.subplot(2, 2, 4)
    plt.imshow(image_boites)
    plt.title("Zones de Texte Détectées")
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    # Spécifiez le chemin de votre image
    chemin_image = "C:\\Users\\MSI\\OneDrive\\Documents\\tp_cv\\a.jpg"  # Remplacez par votre image
    traiter_image(chemin_image)