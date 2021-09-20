import datetime, json, hashlib

class Block:
    def __init__(self,index, previousHash, data):
        self.index = index
        self.previousHash = previousHash
        self.data = data
        self.timestamp = str(datetime.now())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        encode_block = str([self.index, self.previousHash, self.timestamp, json.dumps(self.data)]).encode()
        return hashlib.sha256(encode_block).hexdigest()

    def returnValues(self):
        values = {
            'index': self.index,
            'timestamp': self.timestamp,
            'previousHash': self.previousHash,
            'data': self.data,
            'hash': self.hash
        }
        return values

class BlockChain:
    def __init__(self):
        self.chain = [self.genesisBlock()]

    def genesisBlock(self):
        return Block(1,'0xx', {'amount': 10}).returnValues()

    def latestBlock(self):
        return self.chain[-1]

    def mineBlock(self, data):
        number_found = False 
        nonce = 0 
        while not number_found:
	        curr_hash = hashlib.sha256((str(self.chain) + str(nonce)).encode()).hexdigest()
	        nonce = nonce + 1
	        if curr_hash.startswith('00000'): #runs until the hash of the number starts with 5 zeros
                    #print(f'{curr_hash}, {nonce}\n')
                    number_found = True

        self.data = data

        newBlock =  Block(len(self.chain) + 1,self.latestBlock().get('hash'),self.data).returnValues()
        self.chain.append(newBlock)
        return newBlock

chain1 = BlockChain()
i = 0
for i in range(4):
    chain1.mineBlock({'amount': i + 44})
    json_data = json.dumps(chain1.chain, indent=4)
    with open('chainData.dat', 'w') as filename:
        filename.write(json_data)
    i += 1
