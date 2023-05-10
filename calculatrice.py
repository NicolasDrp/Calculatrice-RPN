def multiplication(tableau):
    resultat = tableau[0]*tableau[1]
    tableau.remove(tableau[0])
    tableau.remove(tableau[0])
    tableau.insert(0,resultat)

def division(tableau):
    resultat = tableau[0]/tableau[1]
    tableau.remove(tableau[0])
    tableau.remove(tableau[0])
    tableau.insert(0,resultat)

def addition(tableau):
    resultat = tableau[0]+tableau[1]
    tableau.remove(tableau[0])
    tableau.remove(tableau[0])
    tableau.insert(0,resultat)

def soustraction(tableau):
    resultat = tableau[0]-tableau[1]
    tableau.remove(tableau[0])
    tableau.remove(tableau[0])
    tableau.insert(0,resultat)

calcul = "4 6 * 7 / 5 +"

# Recuperer les nombres du calcul
nombres = [int(chiffre) for chiffre in calcul.split() if chiffre.isdigit()]

# Recuperer les operateurs du calcul
operateurs = [str(signe)
              for signe in calcul.split() if signe.isdigit() == False]

while len(nombres) > 1 or len(operateurs)!=0:
    if len(operateurs) > 0:
        match operateurs[0]:
            case "+":
                addition(nombres)
            case "-":
                soustraction(nombres)
            case "*":
                multiplication(nombres)
            case "/":
                division(nombres)
    operateurs.remove(operateurs[0])

print(f"le resultat de '{calcul}' est {nombres[-1]}")