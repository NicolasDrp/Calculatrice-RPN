calcul = "( ( 5 + 2 ) / 3 ) + 8 * 3"

# Va recuperer les nombres du calcul
nombres = []

# Va recuperer les operateurs du calcul
operateurs = []

total =[char for char in calcul.split()]

print(total)

resultat = []

while len(total) >0:
    if total[0].isdigit():
        nombres.append(total[0])
    elif total[0] == "*" or total[0] == "+" or total[0] == "-" or total[0] == "/":
        operateurs.insert(0,total[0])
    total.remove(total[0])

print(nombres)
print(operateurs)

resultat = nombres+operateurs

print(" ".join(resultat))



# def convertion(total):
#     calcul = {'+': 1, '-': 1, '*': 2, '/': 2}
#     sortie = []
#     operateur = []

#     for item in total:
#         if item.isdigit():
#             sortie.append(item)
#         elif item in calcul:
#             while operateur and operateur[-1] != '(' and calcul[operateur[-1]] >= calcul[item]:
#                 sortie.append(operateur.pop())
#             operateur.append(item)
#         elif item == '(':
#             operateur.append(item)
#         elif item == ')':
#             while operateur and operateur[-1] != '(':
#                 sortie.append(operateur.pop())
#             if operateur and operateur[-1] == '(':
#                 operateur.pop()

#     while operateur:
#         sortie.append(operateur.pop())

#     return sortie

# total = "3 * ( ( 5 * 8 ) + 7 )"
# items = total.split()
# resultat = convertion(items)

# print(" ".join(resultat))




    # tant qu’il y a des tokens à lire :

    #     lire le token.

    #         si c’est un nombre l’ajouter à la sortie.
    #         si c'est une fonction, le mettre sur la pile.
    #         si c'est un séparateur d'arguments de fonction (par exemple une virgule) :

    #             jusqu'à ce que l'élément au sommet de la pile soit une parenthèse gauche, retirer l'élément du sommet de la pile et l'ajouter à la sortie. Si toute la pile est dépilée sans trouver de parenthèse gauche, c’est qu’il y a un mauvais parenthésage.

    #         si c’est un opérateur o1 alors

    #         1) tant qu’il y a un opérateur o2 sur le haut de la pile et si l’une des conditions suivantes est remplie.

    #                     o1 est associatif ou associatif à gauche et sa priorité est inférieure ou égale à celle d’o2, ou
    #                     o1 est associatif à droite et sa priorité est inférieure à celle d’o2,

    #             retirer o2 de la pile pour le mettre dans la sortie

    #         2) mettre o1 sur la pile

    #         si le token est une parenthèse gauche, le mettre sur la pile.
    #         si le token est une parenthèse droite, alors dépiler les opérateurs et les mettre dans la sortie jusqu’à la parenthèse gauche qui elle aussi sera dépilée, mais pas mise dans la sortie. Après cela, si le token au sommet de la pile est une fonction, le dépiler également pour l'ajouter à la sortie. Si toute la pile est dépilée sans trouver de parenthèse gauche c’est qu’il y a un mauvais parenthésage.

    # après la lecture du dernier token, s'il reste des éléments dans la pile il faut tous les dépiler pour les mettre dans la sortie (il ne doit y avoir que des opérateurs. Si on trouve une parenthèse gauche alors il y a eu un mauvais parenthésage).