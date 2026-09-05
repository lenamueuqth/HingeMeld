# test_hingemeld.py
"""
Tests for HingeMeld module.
"""

import unittest
from hingemeld import HingeMeld

class TestHingeMeld(unittest.TestCase):
    """Test cases for HingeMeld class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HingeMeld()
        self.assertIsInstance(instance, HingeMeld)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HingeMeld()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
