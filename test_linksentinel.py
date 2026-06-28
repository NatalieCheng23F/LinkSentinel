# test_linksentinel.py
"""
Tests for LinkSentinel module.
"""

import unittest
from linksentinel import LinkSentinel

class TestLinkSentinel(unittest.TestCase):
    """Test cases for LinkSentinel class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LinkSentinel()
        self.assertIsInstance(instance, LinkSentinel)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LinkSentinel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
