import streamlit as st
import hashlib
import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.create_hash()

    def create_hash(self):
        block_string = str(self.index) + self.timestamp + self.data + self.previous_hash
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

if "blockchain" not in st.session_state:
    st.session_state.blockchain = Blockchain()

st.title("🔗 Blockchain Data Sharing System")

data = st.text_input("Enter Data to Store in Blockchain")

if st.button("Add Block"):
    if data:
        st.session_state.blockchain.add_block(data)
        st.success("Block Added Successfully!")
    else:
        st.warning("Please enter some data")

st.subheader("📦 Blockchain Data")

for block in st.session_state.blockchain.chain:
    st.write(f"**Index:** {block.index}")
    st.write(f"**Timestamp:** {block.timestamp}")
    st.write(f"**Data:** {block.data}")
    st.write(f"**Hash:** {block.hash}")
    st.write(f"**Previous Hash:** {block.previous_hash}")
    st.markdown("---")