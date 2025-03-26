class Agence:
    def __init__(self):
        self.comptes = []
        self.transactions = []
    
    def ajouter_compte(self, compte):
        if any(c.identifiant == compte.identifiant for c in self.comptes):
            raise ValueError("Identifiant de compte déjà utilisé.")
        if any(c.proprietaire == compte.proprietaire for c in self.comptes):
            raise ValueError("Un propriétaire ne peut avoir qu'un seul compte.")
        self.comptes.append(compte)
    
    def is_valid(self):
        comptes_uniques = len(self.comptes) == len(set(c.identifiant for c in self.comptes))
        proprietaires_uniques = len(self.comptes) == len(set(c.proprietaire for c in self.comptes))
        comptes_valides = all(c.is_valid() for c in self.comptes)
        return comptes_uniques and proprietaires_uniques and comptes_valides
    
    def transaction_at_date(self, date):
        return [t for t in self.transactions if t.date == date]