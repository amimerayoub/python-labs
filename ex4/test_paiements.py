# test_paiements.py
import unittest
from paiements import CarteBancaire, PayPal, Crypto, traiter_paiements

class TestPaiements(unittest.TestCase):
    def test_carte_et_paypal_crypto(self):
        c = CarteBancaire(12.34, "4539 1488 0343 6467", "123")
        p = PayPal(5.0, "u@example.com", "tk")
        cr = Crypto(0.01, "wallet1", "BTC")

        self.assertIn("Paiement par CarteBancaire", c.payer())
        self.assertIn("Paiement via PayPal", p.payer())
        self.assertIn("Paiement en BTC", cr.payer())

    def test_traiter_paiements_retourne_confirmations(self):
        items = [
            CarteBancaire(1.0, "4539 1488 0343 6467", "111"),
            PayPal(2.0, "a@b.com", "t"),
        ]
        confs = traiter_paiements(items)
        self.assertEqual(len(confs), 2)
        self.assertTrue(all(isinstance(c, str) for c in confs))

    def test_montant_negative_raise(self):
        with self.assertRaises(ValueError):
            CarteBancaire(-1, "4539 1488 0343 6467", "123")
        with self.assertRaises(ValueError):
            PayPal(0, "a@b.com", "t")
        with self.assertRaises(ValueError):
            Crypto(0, "w", "BTC")

if __name__ == "__main__":
    unittest.main()
