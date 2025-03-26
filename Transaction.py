class Transaction:
    def __init__(self, montant, date, type_transaction, compte_id, compte_dest_id=None):
        if montant < 0:
            raise ValueError("Le montant ne peut pas être négatif.")
        if type_transaction == "transfert" and compte_id == compte_dest_id:
            raise ValueError("Le transfert ne peut pas être effectué vers le même compte.")
        
        self.montant = montant
        self.date = date
        self.type_transaction = type_transaction
        self.compte_id = compte_id
        self.compte_dest_id = compte_dest_id