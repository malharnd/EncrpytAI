from model import Linmodel
from phe import paillier
import json

def clientdata():
    with open('encrypted_data.txt', 'r') as file:
        encrypted_data_str = json.load(file)
        data = json.loads(encrypted_data_str)
        return data


def computedata():
    data = clientdata()
    coef_we  = Linmodel().getCoef()
    pub_key = data['public_key']
    public_key = paillier.PaillierPublicKey(n=int(pub_key['n']))
    enc_nums_rec = []  

    for x in data['values']:
        value1 = int(x[0])
        value2 = int(x[1])  
        
        encrypted_num = paillier.EncryptedNumber(public_key, value1, value2)
        enc_nums_rec.append(encrypted_num)
    results = 0  # Initialize results to zero

    for i in range(len(coef_we)):
        results += coef_we[i] * enc_nums_rec[i]
    return results, public_key


def serializedata():
    results, public_key = computedata()
    serialized_results = {}
    serialized_results['public_key'] = {'n': public_key.n}
    serialized_results['values'] = [(str(results.ciphertext()), results.exponent)]
    serialdata =  json.dumps(serialized_results)
    print('This is the result: ', serialdata)
    return serialdata


def main():
    result = serializedata()
    with open('results.txt', 'w') as file:
        json.dump(result, file)
        
if __name__ == '__main__':
    main()