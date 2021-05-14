import datetime, json, hashlib
#Define the blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.genesisBlock()]

    def genesisBlock(self):
        gBlock = {
            'index' : 0,
            'timestamp' : str(datetime.datetime.now()),
            'previousHash': "0xx",
            'data': {'amount ': 500}
                              
        }
        gBlock_hash = self.calcHash(gBlock)
        gBlock.update({'hash': gBlock_hash})
        return gBlock

    def mineBlock(self, data):

        number_found = False 
        nonce = 0 
        while not number_found:
	        curr_hash = hashlib.sha256((str(self.chain) + str(nonce)).encode()).hexdigest()
	        nonce = nonce + 1

	        if curr_hash.startswith('0000'): #runs until the hash of the number starts with 4 zeros
                    #print(curr_hash)
                    number_found = True
        
        block = {

        'index' : self.chain[-1].get('index') + 1,
        'timestamp' : str(datetime.datetime.now()),
        'previousHash' : self.chain[-1].get('hash'),
        'data' : data,
    }

        block_hash = self.calcHash(block)
        block.update({'hash' : block_hash})

        self.chain.append(block)
        return block

    def calcHash(self,block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

chain1 = Blockchain()

def mineBlock():
    print('Mining Blocks\n')
    i = 0

    while i < 4:
        chain1.mineBlock({'amount': i + 40})
        i += 1

    return "Done\n"

if __name__ == '__main__':
    mineBlock()
    json_data = json.dumps(chain1.chain, indent=4)
    print(json_data)
#write the output to a file named 'chainData.dat'
    with open('chainData.dat', 'w') as chainData:
        chainData.write(json_data)
