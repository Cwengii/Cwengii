import unittest

from cash_register import change

class TestCashRegister(unittest.TestCase):
    
    def test_change(self):
        self.assertEqual(change(1000,1000), [ ])
        
    def test_bills(self):
         self.assertEqual(change(5000,1000), [("R50", 1)])
    
    def test_mixed_change(self):
         self.assertEqual(change(1250,2000), [ ("R5", 1), ("5c", 1)])
         
    def test_mixed_coin_change(self):
        self.assertEqual(change(85,100), [("10c", 1 ), ("5c", 1)])
        
    def test_amount_paid(self):
        self.assertEqual(change(2000, 1500), TestCashRegister)
        
if __name__ == '_main_':
    unittest.main()