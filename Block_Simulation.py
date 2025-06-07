import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previousHash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previousHash) + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mineBlock(self, difficulty):
        # Add simple Proof-of-Work (PoW) - hash must start with '0'*difficulty
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculateHash()
        print(f"Block {self.index} mined: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 3  # Adjust difficulty here

    def createGenesisBlock(self):
        return Block(0, time.ctime(), "Genesis Block", "0")

    def getLatestBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)

    def displayChain(self):
        for block in self.chain:
            print("\n----- Block -----")
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previousHash}")
            print(f"Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")

# === Main Execution ===
myBlockchain = Blockchain()
myBlockchain.addBlock(Block(1, time.ctime(), "Block 1 Data"))
myBlockchain.addBlock(Block(2, time.ctime(), "Block 2 Data"))

myBlockchain.displayChain()
