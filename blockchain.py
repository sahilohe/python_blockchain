import datetime, json, hashlib
#Define the blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.genesisBlock()]

    def genesisBlock(self):
        gBlock = {
            'index' : 0,
            'hash' : self.calcHash(str({
                'index': 0, 
                'timstamp': datetime.datetime.now(), 
                'previousHash': '0xx',
                'data': {'amount ': 500}
                
            }))               
        }
        #self.chain.append(gBlock)
        return gBlock

    def createBlock(self, data):

        block = { 'index' : self.chain[-1].get('index') + 1,
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

# Let's test the blockchain
blockchain1 = Blockchain()
i = 0

while i < 10: # let's write 10 blocks 
    blockchain1.createBlock({'amount': i + 50}) # writing random blocks to the chain, incrementing the amount each time to + 1
    i = i + 1

json_data = json.dumps(blockchain1.chain,indent=4) # looks good in json format
#print(json_data) 

#write the output to a file named 'chainData.dat'
with open('chainData.dat', 'w') as chainData:
    chainData.write(json_data)
