from Transaction import Transaction
from datetime import datetime

class Compte:
    def __init__(self, proprietaire, identifiant, solde=0):
        self.proprietaire = proprietaire
        self.identifiant = identifiant
        self.solde = solde
        self.transactions = []

    def deposer(self, montant):
        # Crée une transaction de dépôt
        transaction = Transaction(montant, datetime.now(), "dépôt", self.identifiant)
        self.solde += transaction.montant
        self.transactions.append(transaction)

    def retirer(self, montant):
        # Crée une transaction de retrait
        transaction = Transaction(montant, datetime.now(), "retrait", self.identifiant)
        if transaction.montant > self.solde:
            raise ValueError("Fonds insuffisants.")
        if transaction.montant % 10 != 0:
            raise ValueError("Les retraits doivent être des sommes rondes.")
        self.solde -= transaction.montant
        self.transactions.append(transaction)

    def transferer(self, montant, compte_dest):
        # Crée une transaction de transfert
        transaction = Transaction(montant, datetime.now(), "transfert", self.identifiant, compte_dest.identifiant)
        if transaction.montant > self.solde:
            raise ValueError("Fonds insuffisants pour le transfert.")
        self.solde -= transaction.montant
        compte_dest.solde += transaction.montant
        self.transactions.append(transaction)
        compte_dest.transactions.append(transaction)

    def resume_transactions(self):
        return self.transactions[-10:]

    def is_valid(self):
        total_transactions = sum(t.montant if t.type_transaction != "retrait" else -t.montant for t in self.transactions)
        retraits_valides = all(t.montant % 10 == 0 for t in self.transactions if t.type_transaction == "retrait")
        return total_transactions == self.solde and retraits_valides and self.solde >= 0