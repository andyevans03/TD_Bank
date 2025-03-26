import unittest
from Transaction import Transaction
from Compte import Compte
from datetime import datetime

class TestUnitaireCompte(unittest.TestCase):
    
    def setUp(self):
        self.compte1 = Compte("Andy","CO1Andy",2000)
        self.compte2= Compte("RAMAROLAHY","CO1RAMAROLAHY", 1000)

    def test_deposer(self):
        self.compte1.deposer(300)
        self.assertEqual(self.compte1.solde, 2300)

    def test_retirer_valide(self):
        self.compte2.retirer(100)
        self.assertEqual(self.compte2.solde, 900)

    def test_retirer_invalide(self):
        with self.assertRaises(ValueError):
            self.compte1.retirer(105) 
        
        with self.assertRaises(ValueError):
            self.compte1.retirer(3000)  
            self.compte2.retirer(1500)

    def test_transferer(self):
        self.compte1.transferer(100, self.compte2)
        self.assertEqual(self.compte1.solde, 1900)
        self.assertEqual(self.compte2.solde, 1100)

    
    def test_is_valid(self):
        
        self.compte1.deposer(500)
        self.compte1.retirer(100)
        self.assertTrue(self.compte1.is_valid())
        
    
        self.compte1.solde = 400
        self.assertFalse(self.compte1.is_valid())