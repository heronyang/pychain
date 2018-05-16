"""
Implementation of the simple and basic block chain objects.
"""
import hashlib
from datetime import datetime

DIFFICULTY = 4


class Block():
    """
    Block stores its own payload, the timestamp of creation, and the hash of
    the previous block. The hash of a block is calculated by considering all
    the properties.
    """

    def __init__(self, payload, prev_hash):

        if not isinstance(payload, str):
            raise Exception("Payload should be in a string")

        self.payload = payload
        self.prev_hash = prev_hash
        self.time_stamp = datetime.now()
        self.nonce = 0

    @property
    def hash(self):
        """
        Returns the hash of this block by concatenating the payload, previous
        hash, and the timestamp, then encoding into utf-8, hashing with
        SHA-256.
        """
        return hashlib.sha256((
            self.payload +
            self.prev_hash +
            str(self.time_stamp) +
            str(self.nonce)
        ).encode("utf-8")).hexdigest()

    def mine(self):
        """
        Mine this block by finding a nouce that lets the first few bytes of
        hash matches our target.
        """
        target = "0" * DIFFICULTY
        while self.hash[:DIFFICULTY] != target:
            self.nonce += 1

    def __hash__(self):
        return int(self.hash, 16)

    def __repr__(self):
        return "<Block %s>" % hash(self)


class Chain():
    """
    Chain contains a list of Blocks and provides functionalities to operate on
    the chain.
    """

    def __init__(self):
        self.blocks = []

    def add(self, block):
        """
        Adds a new block into this chain.
        """
        self.blocks.append(block)

    @property
    def is_valid(self):
        """
        Checks if the chain is valid by looking up whether the hashs are
        matched between blocks.
        """
        for i in range(1, len(self.blocks)):
            curr_block = self.blocks[i]
            prev_block = self.blocks[i-1]
            # Checks if the chain is linked correctly
            if curr_block.prev_hash != prev_block.hash:
                return False
            # Checks if this chain had been mined successfully
            if curr_block.hash[:DIFFICULTY] != "0" * DIFFICULTY:
                return False
        return True
