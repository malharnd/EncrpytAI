import phe as paillier
import json


def keygen():
    public_key, private_key = paillier.generate_paillier_keypair()
    # creating a dictionary to store keys
    keys = {}
    # n modulous is public key (p*q)
    keys['public_key'] = {'n': public_key.n}
    # p and q are private keys prime numbers
    keys['private_key'] = {'p': private_key.p, 'q': private_key.q}
    with open('keypair.txt', 'w') as file:
        json.dump(keys, file)

def retrivekeys():
    with open('keypair.txt', 'r') as file:
        keys = json.load(file)
    public_key = paillier.PaillierPublicKey(n=int(keys['public_key']['n']))
    private_key = paillier.PaillierPrivateKey(public_key=public_key, p=int(keys['private_key']['p']), q=int(keys['private_key']['q']))
    return public_key, private_key

def encrypted_data_str(public_key, data):
    encrypted_data_list = [public_key.encrypt(x) for x in data]
    encrypted_data = {}
    encrypted_data['public_key'] = {'n': public_key.n}
    encrypted_data['values'] = [(str(x.ciphertext()), x.exponent) for x in encrypted_data_list]
    serialdata =  json.dumps(encrypted_data)
    return serialdata


def read_result():
    with open('results.txt', 'r') as file:
        res = json.load(file)
        result = json.loads(res)
    return result

public_key, private_key = retrivekeys()
custreq = age,sex,bmi,children,smoker,region = [19,1,22,0,0,0]
encrypted_data_str = encrypted_data_str(public_key, custreq)
with open ('encrypted_data.txt', 'w') as file:
    json.dump(encrypted_data_str, file)
    
    
    
result_file =  read_result()
result_key = paillier.PaillierPublicKey(n=int(result_file['public_key']['n']))

result = paillier.EncryptedNumber(result_key, int(result_file['values'][0][0]), int(result_file['values'][0][1]))

if (result_key == public_key):
    print(private_key.decrypt(result))