import hashlib

class User:
    def __init__(self, name, password):
        """
        Initialise un objet User.

        Args:
            name (str): Nom du joueur.
            password (str): Mot de passe du joueur.
        """
        self.name = name  # Définit le nom du joueur
        self.password = self._hash_password(password)  # Hache et définit le mot de passe du joueur
        self.money = 1000  # Initialise l'argent du joueur à 1000€

    def _hash_password(self, password):
        """
        Hache le mot de passe à l'aide de l'algorithme de hachage SHA256.

        Args:
            password (str): Mot de passe du joueur.

        Returns:
            str: Mot de passe haché.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def update_scores(self):
        """
        Met à jour les scores du joueur dans la base de données.
        """
        # Ajoutez ici le code pour mettre à jour les scores du joueur dans la base de données
        pass
