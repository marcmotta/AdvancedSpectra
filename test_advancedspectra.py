# test_advancedspectra.py
"""
Tests for AdvancedSpectra module.
"""

import unittest
from advancedspectra import AdvancedSpectra

class TestAdvancedSpectra(unittest.TestCase):
    """Test cases for AdvancedSpectra class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AdvancedSpectra()
        self.assertIsInstance(instance, AdvancedSpectra)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AdvancedSpectra()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
