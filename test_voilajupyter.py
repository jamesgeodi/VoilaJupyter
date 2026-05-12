# test_voilajupyter.py
"""
Tests for VoilaJupyter module.
"""

import unittest
from voilajupyter import VoilaJupyter

class TestVoilaJupyter(unittest.TestCase):
    """Test cases for VoilaJupyter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VoilaJupyter()
        self.assertIsInstance(instance, VoilaJupyter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VoilaJupyter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
