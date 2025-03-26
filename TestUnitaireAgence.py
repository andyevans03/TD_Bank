import unittest
from Agence import Agence
from Compte import Compte
from datetime import datetime

class TestAgence(unittest.TestCase):

    def setUp(self):
        self.agence = Agence()
        self.compte1 = Compte("Alice", "C0133", 1000)
        self.compte2 = Compte("Bob", "C022", 500)
        self.agence.ajouter_compte(self.compte1)
        self.agence.ajouter_compte(self.compte2)

    def test_ajouter_compte(self):
        compte3 = Compte("Andy", "C0122", 300)
        self.agence.ajouter_compte(compte3)
        self.assertEqual(len(self.agence.comptes), 3)

    def test_ajouter_compte_identifiant_unique(self):
        compte3 = Compte("Alice", "C0133", 300)
        with self.assertRaises(ValueError):
            self.agence.ajouter_compte(compte3)

    def test_transaction_at_date(self):
        self.compte1.deposer(200)
        self.compte1.retirer(100)
        transactions = self.agence.transaction_at_date(datetime.now())
        self.assertEqual(len(transactions), 2)
       
   