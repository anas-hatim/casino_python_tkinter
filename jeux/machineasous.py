import random
import tkinter as tk
from .jeu import Jeu

class MachineASous(Jeu):
    def __init__(self):
        super().__init__("Machine à sous")

    def run(self, user):
        """
        Lance le jeu de la machine à sous.

        Args:
            user (User): Objet représentant le joueur connecté.
        """
        window = tk.Tk()
        window.title("Machine à sous")
        # Ajoutez ici le code pour afficher l'interface graphique de la machine à sous avec Tkinter

        while True:
            print(f"\nArgent disponible : {user.money}€")
            print("1. Jouer 1€")
            print("q. Quitter")

            choice = input("Choisissez une option : ")

            if choice == "1":
                if user.money < 1:
                    print("Vous n'avez pas assez d'argent pour jouer.")
                    continue

                user.money -= 1
                numbers = [random.randint(1, 6) for _ in range(3)]

                print(f"Résultat : {numbers[0]} {numbers[1]} {numbers[2]}")

                if numbers[0] == numbers[1] == numbers[2]:
                    user.money += 500
                    print("Félicitations ! Vous avez gagné 500€ !")
                else:
                    print("Dommage, vous n'avez pas gagné cette fois-ci.")

            elif choice == "q":
                break  # Quitte la boucle du jeu
            else:
                print("Choix invalide. Veuillez réessayer.")

        # Ajoutez ici le code pour fermer l'interface graphique de la machine à sous avec Tkinter
        window.mainloop()
