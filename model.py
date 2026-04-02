import datetime
from utils import create_hash

class Block:
def **init**(self, index, data, previous_hash):
self.index = index
self.timestamp = str(datetime.datetime.now())
self.data = data
self.previous_hash = previous_hash
self.hash = self.generate_hash()

```
def generate_hash(self):
    """
    Generate hash for the block
    """
    block_data = (
        str(self.index)
        + self.timestamp
        + self.data
        + self.previous_hash
    )
    return create_hash(block_data)
```

class Blockchain:
def **init**(self):
self.chain = [self.create_genesis_block()]

```
def create_genesis_block(self):
    """
    Create the first block in blockchain
    """
    return Block(0, "Genesis Block", "0")

def add_block(self, data):
    """
    Add a new block to blockchain
    """
    prev_block = self.chain[-1]
    new_block = Block(
        index=len(self.chain),
        data=data,
        previous_hash=prev_block.hash
    )
    self.chain.append(new_block)

def get_chain(self):
    """
    Return full blockchain
    """
    return self.chain
```
