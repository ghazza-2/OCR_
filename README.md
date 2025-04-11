#  Projet OCR - Extraction de texte depuis une image

Ce projet a pour objectif d'extraire du texte à partir d'images en utilisant la reconnaissance optique de caractères (**OCR**) grâce à Python, OpenCV et Tesseract.

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
- **Pillow (PIL)** — manipulation d’images
- **Matplotlib** — affichage graphique

---

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




