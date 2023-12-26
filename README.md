# merge_fruit

Lancement du jeu : démarrer le programme
But du jeu : fusionner des balles de même couleur pour faire le score le plus grand possible

Derniers détails mineurs non réglés :
Dur de bien voir quelle balle on à (raffraichissement de l'écran pas complètement fonctionnel, et fonctionne que tout en haut)

Game over pas optimal (quand on lache une balle, on calcule par rapport aux balles deja présentes si elle va dépasser la ligne de game over,
on devrait prendre en compte le fait qu'une fois lâcher elle peut fusionner, ou glisser ce qui peut ne pas entrainer un game over, on a essayé de faire comme ça mais compliqué
à gérer, pas complètement fonctionnel)

Mettre des images à la place des couleurs : compliqué car on change totalement le système qu'on a mis en place (utilisation de  screen.blit au lieu de 
 pygame.draw.circle) On a pensé à laisser le système des couleurs, avec le même check de couleurs, mais sans les montrer (avec par dessus les images)
mais on a pas réussi complètement (on a réussi pour une balle, mais l'image bug au fur et à mesure qu'on lache des balles) On aurait aimé réussir pour une balle comme ça on rajoute les images correspondant à chaque balles dans le tableau balls, et en théorie ça aurait fonctionné. Pour tester il faut décommenter ce code :

            # image = pygame.transform.scale(image, (2 * balls[i-1][5], 2 * balls[i-1][5])) 
            # screen.blit(image, (balls[i-1][0] - balls[i-1][5], balls[i-1][1] - balls[i-1][5]))

            ligne 161-162

On est plus obligés de cliquer tout en haut pour faire apparaitre une balle, tout ce système à été ajusté (il manque juste l'affichage de la balle avant d'être lâchée)

Conclusion : jeu fonctionnel avec juste des détails à régler pour l'améliorer
