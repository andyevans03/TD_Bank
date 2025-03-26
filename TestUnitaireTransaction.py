import unittest
from datetime import datetime
from Transaction import Transaction
from Compte import Compte

class TestUnitaireTransaction(unittest.TestCase):

     def test_transferer_meme_compte(self):
        with self.assertRaises(ValueError):
            Transaction(20, datetime.now(), "transfert", "IDC11", "IDC11")
    
     def test_transferer_montant_negatif(self):
        with self.assertRaises(ValueError):
            Transaction(-100, datetime.now(), "transfert", "C002", "C001")