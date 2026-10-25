import unittest
from main import evaluate
class RateTests(unittest.TestCase):
    def test_exact_floor(self): self.assertEqual(evaluate(30,0,0,0,60)["decision"],"CONSIDER")
    def test_under_floor(self): self.assertEqual(evaluate(10,0,0,0,60)["decision"],"BELOW_FLOOR")
    def test_invalid_minutes(self):
        with self.assertRaises(ValueError): evaluate(10,0,0,0,0)
    def test_costs_deducted(self): self.assertEqual(evaluate(50,5,2,3,60)["estimated_net"],40)
if __name__=="__main__": unittest.main()
