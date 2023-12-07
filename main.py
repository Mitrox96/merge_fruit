import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
taille_fenetre = (largeur, hauteur)

# Créer la fenêtre
fenetre = pygame.display.set_mode(taille_fenetre)

# Définir le titre de la fenêtre
pygame.display.set_caption("Ma Fenêtre Pygame")

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mettez ici le code pour le rendu ou le traitement de la fenêtre

    # Mise à jour de l'affichage
    pygame.display.flip()
