#!/usr/bin/env python3
"""
Test file for the blockchain basic functions.
"""
import unittest
from chain import Block, Chain


class Test(unittest.TestCase):
    """
    Test class for the basic blockchain operations.
    """

    def test(self):
        """
        Gerenal test.
        """

        # Creates a new chain
        chain = Chain()

        # Puts some blocks into the chain
        block_1 = Block("apple", "0")
        chain.add(block_1)
        block_1.mine()

        block_2 = Block("banana", block_1.hash)
        chain.add(block_2)
        block_2.mine()

        block_3 = Block("cat", block_2.hash)
        chain.add(block_3)

        # Check if the chain is "not valid" if the last block is not mined
        self.assertFalse(chain.is_valid)
        block_3.mine()

        # Checks if the chain is valid
        self.assertTrue(chain.is_valid)
