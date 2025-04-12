#  Projet OCR - Extraction de texte depuis une image

 Ce projet consiste à développer un système de reconnaissance optique de caractères (OCR) permettant d'extraire du texte à partir d'images. L'objectif est de traiter des images contenant du texte, comme des scans ou des photos de documents, et d'en extraire le contenu textuel de manière automatisée.

---

## Fonctionnalités

- Chargement et affichage d'une image
- Prétraitement de l'image (niveaux de gris, binarisation)
- Extraction du texte avec Tesseract OCR
- Affichage des zones de texte détectées

---

##  Technologies utilisées

- **Python** — langage principal
- **OpenCV** — traitement et manipulation d'images
- **Tesseract OCR** — moteur de reconnaissance optique de caractères    
- **Matplotlib** — affichage graphique

---
## Exemples d'utilisation 

-Scanner des documents papier pour les convertir en texte modifiable (PDF, Word, etc.)

-Extraire le texte de reçus pour la gestion de dépenses

-Numériser des livres ou des articles pour les archiver

-Lire automatiquement des cartes d’identité ou passeports

-Récupérer le numéro de carte bancaire lors d’un paiement en ligne

-Reconnaître les plaques d’immatriculation (radars, parkings, péages)

-Lire les étiquettes de colis pour la logistique ou le tri automatique

---
### Exemple d'éxecution:


![image](https://github.com/user-attachments/assets/9a4c1289-fe87-40f4-953f-737338b1c9e9)


![Capture d'écran 2025-04-12 102835](https://github.com/user-attachments/assets/86824352-ce9c-4d9b-97a7-c36070ec4460)




##  Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ghazza-2/ocr.git
cd ocr
```
### 2. Installer les dépendances

Assurez-vous d'avoir **Python** installé, puis exécutez la commande suivante dans votre terminal :

```bash
pip install -r requirements.txt
```
### 3. Installer Tesseract

#### sur Ubuntu / Debian :

```bash
sudo apt update
sudo apt install tesseract-ocr




