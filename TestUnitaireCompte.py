import unittest
from Transaction import Transaction
from Compte import Compte
from datetime import datetime

class TestUnitaireCompte(unittest.TestCase):
    
    def setUp(self):
        self.compte1 = Compte("Andy","CO1Andy",2000)
        self.compte2= Compte("RAMAROLAHY","CO1RAMAROLAHY", 1000)

    def test_deposer(self):
        self.compte1.deposer(200)
        self.assertEqual(self.compte1.solde, 1200)

    def test_retirer_valide(self):
        self.compte1.retirer(100)
        self.assertEqual(self.compte1.solde, 1100)

    def test_retirer_invalide(self):
        with self.assertRaises(ValueError):
            self.compte1.retirer(105)  # Retrait invalide (pas une somme ronde)
        
        with self.assertRaises(ValueError):
            self.compte1.retirer(2000)  # Fonds insuffisants

    def test_transferer(self):
        self.compte1.transferer(200, self.compte2)
        self.assertEqual(self.compte1.solde, 900)
        self.assertEqual(self.compte2.solde, 700)

    def test_is_valid(self):
        # Vérifier que le compte est valide après des opérations
        self.compte1.deposer(500)
        self.compte1.retirer(100)
        self.assertTrue(self.compte1.is_valid())
        
        # Vérifier que le compte est invalide si le solde ne correspond pas à la somme des transactions
        self.compte1.solde = 100  # Solde incorrect
        self.assertFalse(self.compte1.is_valid())