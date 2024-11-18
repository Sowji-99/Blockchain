import hashlib
import datetime

# Block class definition
class Block:
    def __init__(self, previous_hash, product_id, location, timestamp):
        self.previous_hash = previous_hash  # Store previous block's hash
        self.data = {"ProductID": product_id, "Location": location}  # Store product details
        self.timestamp = timestamp
        self.hash = self.calculate_hash()  # Calculate the block's hash

    def calculate_hash(self):
        # Combine the relevant attributes to calculate the hash
        return hashlib.sha256(f"{self.previous_hash}{self.timestamp}{self.data}".encode()).hexdigest()

    @staticmethod
    def create_genesis_block():
        # Genesis block has no previous block, so use a predefined hash
        return Block("0" * 64, "P000", "Start", datetime.datetime.now())


# Initialize the blockchain
block_chain = []

# Create the Genesis Block
block_chain.append(Block.create_genesis_block())

# Define 10 products with random examples
products = [
    {"ProductID": "P001", "Location": "Factory", "ProductName": "Smartphone"},
    {"ProductID": "P002", "Location": "Factory", "ProductName": "Laptop"},
    {"ProductID": "P003", "Location": "Warehouse", "ProductName": "Washing Machine"},
    {"ProductID": "P004", "Location": "Factory", "ProductName": "Refrigerator"},
    {"ProductID": "P005", "Location": "Assembly Unit", "ProductName": "Television"},
    {"ProductID": "P006", "Location": "Testing Center", "ProductName": "Headphones"},
    {"ProductID": "P007", "Location": "Factory", "ProductName": "Air Conditioner"},
    {"ProductID": "P008", "Location": "Warehouse", "ProductName": "Electric Scooter"},
    {"ProductID": "P009", "Location": "Factory", "ProductName": "Microwave Oven"},
    {"ProductID": "P010", "Location": "Assembly Unit", "ProductName": "Gaming Console"},
]

# Add each product to the blockchain
for product in products:
    previous_block = block_chain[-1]  # Get the last block in the chain
    timestamp = datetime.datetime.now()  # Get current timestamp
    new_block = Block(
        previous_block.hash,  # Pass the previous block's hash as the 'previous_hash'
        product["ProductID"], 
        product["Location"],
        timestamp
    )
    block_chain.append(new_block)

# Print the details of the blockchain
print("Blockchain Details:")
for i, block in enumerate(block_chain):
    print(f"Block #{i}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"ProductID: {block.data['ProductID']}")
    print(f"Location: {block.data['Location']}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Hash: {block.hash}")
    print("-" * 40)

# Optional: Validation Function to Check Blockchain Integrity
def validate_blockchain(block_chain):
    for i in range(1, len(block_chain)):
        current_block = block_chain[i]
        previous_block = block_chain[i - 1]
        # Check if the hash of the previous block matches the stored previous_hash
        if current_block.previous_hash != previous_block.hash:
            return False
        # Check if the block's hash is valid
        if current_block.hash != current_block.calculate_hash():
            return False
    return True

# Validate the Blockchain
is_valid = validate_blockchain(block_chain)
print(f"Blockchain Valid: {is_valid}")
