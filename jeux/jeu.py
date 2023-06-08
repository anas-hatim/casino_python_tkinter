import tkinter as tk

class Jeu:
    def __init__(self, nom_du_jeu):
        """
        Initialise un objet Jeu.

        Args:
            nom_du_jeu (str): Nom du jeu.
        """
        self.nom_du_jeu = nom_du_jeu  # Définit le nom du jeu

    def bienvenue(self):
        """
        Affiche un message de bienvenue pour le jeu.
        """
        print(f"Bienvenue dans {self.nom_du_jeu}")  # Affiche un message de bienvenue avec le nom du jeu
        
        # Ajoutez ici le code pour afficher l'interface graphique de bienvenue avec Tkinter
        window = tk.Tk()
        window.title("Bienvenue")

        label = tk.Label(window, text=f"Bienvenue dans {self.nom_du_jeu}")
        label.pack()

        window.mainloop()
