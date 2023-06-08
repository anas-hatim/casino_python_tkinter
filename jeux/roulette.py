import random
import tkinter as tk
from .jeu import Jeu

class Roulette(Jeu):
    def __init__(self):
        super().__init__("Roulette")

    def run(self, user):
        def jouer():
            amount = int(amount_entry.get())
            selected_number = int(number_entry.get())

            if amount <= 0:
                result_label.config(text="La somme doit être positive.")
                return

            if amount > user.money:
                result_label.config(text="Vous n'avez pas assez d'argent pour jouer cette somme.")
                return

            user.money -= amount

            roulette_number = random.randint(0, 49)

            result_label.config(text=f"Numéro tiré : {roulette_number}")

            if roulette_number == selected_number:
                user.money += amount * 3
                result_label.config(text=f"Félicitations ! Vous avez gagné {amount * 3}€ !")
            else:
                result_label.config(text="Dommage, vous n'avez pas gagné cette fois-ci.")

            user.update_scores()

        window = tk.Tk()
        window.title("Roulette")

        # Ajoutez ici le code pour afficher l'interface graphique de la roulette avec Tkinter
        amount_label = tk.Label(window, text="Somme à parier :")
        amount_label.pack()

        amount_entry = tk.Entry(window)
        amount_entry.pack()

        number_label = tk.Label(window, text="Numéro à parier (entre 0 et 49) :")
        number_label.pack()

        number_entry = tk.Entry(window)
        number_entry.pack()

        play_button = tk.Button(window, text="Jouer", command=jouer)
        play_button.pack()

        result_label = tk.Label(window, text="")
        result_label.pack()

        window.mainloop()
