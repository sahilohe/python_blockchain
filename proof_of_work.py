from blockchain import Blockchain
import hashlib,json

class PoW_Chain(Blockchain):
    def __init__(self):
        Blockchain.__init__(self) # inhetering all objects from the Blockchain class
   
        number_found = False 
        nonce = 0 
        while not number_found:
	        curr_hash = hashlib.sha256((str(self.chain) + str(nonce)).encode()).hexdigest()
	        nonce = nonce + 1

	        if curr_hash.startswith('00000'): #runs until the hash of the number starts with 5 zeros
                    print(curr_hash)
                    number_found = True

chain1 = PoW_Chain()

i = 0
#this will run after the number is found, kind of mining
while i < 4:
    chain1.createBlock({'amount': i + 50}) #just creates some blocks
    i = i + 1

json_data = json.dumps(chain1.chain,indent=4) # looks good in json format

if __name__ == '__main__':
    with open('chainData.dat', 'w') as file: #write the blockchain data to a file
        file.write(json_data)
    
