import tkinter as tk
from user import User
from jeux.jeu import Jeu
from jeux.machineasous import MachineASous
from jeux.roulette import Roulette

def display_scores(score):
    """
    Affiche les scores des joueurs.

    Args:
        score (list): Liste contenant le nom du joueur et son score.
    """
    print(f"Nom du joueur : {score[0]}")
    print(f"Score : {score[1]}€")

def update_scores(scores, user):
    """
    Met à jour les scores des joueurs.

    Args:
        scores (list): Liste contenant les scores des joueurs.
        user (User): Objet représentant le joueur connecté.
    """
    for score in scores:
        if score[0] == user.name:
            score[1] = str(user.money)
            scores.sort(key=lambda x: int(x[1]), reverse=True)
            break

def main():
    user = User("John Doe", "password")

    jeux = [MachineASous(), Roulette()]

    scores = [["John Doe", "1000"], ["yellow Smith", "500"], ["Bob Johnson", "2000"]]

    window = tk.Tk()
    window.title("Menu")

    label = tk.Label(window, text="Bienvenue au casino !")
    label.pack()

    for jeu in jeux:
        button = tk.Button(window, text=jeu.nom_du_jeu, command=lambda jeu=jeu: jeu.run(user))
        button.pack()

    score_label = tk.Label(window, text="Scores :")
    score_label.pack()

    for score in scores:
        display_scores(score)

    user.update_scores()

    update_scores(scores, user)

    window.mainloop()

if __name__ == "__main__":
    main()
