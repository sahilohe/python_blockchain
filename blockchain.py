import datetime, json, hashlib

class Blockchain:

    def __init__(self):
        self.chain = []
        self.createBlock({'amount': 50})

    def createBlock(self, data):

        block = { 'index' : len(self.chain) + 1,
                  'timestamp' : str(datetime.datetime.now()),
                  'previousHash' : self.calcHash(len(self.chain) - 1),
                  'data' : data,
                  'hash' : self.calcHash(len(self.chain))
        }

        self.chain.append(block)
        return block

    def calcHash(self,block):
        encodedBlock = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()

chain1 = Blockchain()
i = 0

while i < 5:
    chain1.createBlock({'amount': i + 50})
    i = i + 1

json_data = json.dumps(chain1.chain,indent=4)
#print(json_data)
with open('chainData.txt', 'w') as fileWrite:
    fileWrite.write(json_data)
