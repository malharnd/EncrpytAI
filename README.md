# EncrpytAI
A demonstration of Paillier homomorphic encryption for secure computations


## Overview
This project demonstrates the implementation of homomorphic encryption to perform linear regression on sensitive data while preserving data privacy and security. The system comprises three primary components: the client, the server, and the model.

## Components

### Client
- **Key Generation:** The client is responsible for generating a Paillier key pair, consisting of a public key and a private key. These keys are essential for encryption and decryption operations. The keys are saved to a file named 'keypair.txt'.
- **Data Encryption:** The client encrypts a set of input data, including age, sex, BMI, children, smoker, and region, using the Paillier public key. The encrypted data is stored in 'encrypted_data.txt'.
- **Result Retrieval:** The client reads the encrypted result from 'results.txt' and decrypts it using the Paillier private key.
- **Usage:** The client's main function orchestrates the entire process, from key generation to decryption and result retrieval.

### Server
- **Data Processing:** The server reads the encrypted data from 'encrypted_data.txt'.
- **Computation:** It performs linear regression on the encrypted data using coefficients obtained from the model. The server ensures that all computations are performed on encrypted data.
- **Result Storage:** The server saves the encrypted result in 'results.txt'.
- **Usage:** The server's main function initiates the computation on encrypted data and stores the result.

### Model
- **Model Training:** The model trains a linear regression model on the preprocessed data to obtain coefficients.
- **Coefficient Retrieval:** The coefficients from the model are used by the server for computation.
- **Usage:** The model's main function trains the model and returns the coefficients.

## How to Use
1. Execute the `Linmodel` class in the `model.py` file to train the linear regression model and obtain coefficients.
2. Run the `keygen` function in the client to generate Paillier keys and save them to 'keypair.txt'.
3. Execute the `main` function in the server to perform computations on encrypted data and save the result in 'results.txt'.
4. Run the `main` function in the client to decrypt and display the result.

## Requirements
- Python 3.x
- Libraries: phe, pandas, numpy, scikit-learn

## Dataset
- The project uses the 'insurance_preprocessed.csv' dataset for linear regression. This dataset has been preprocessed to ensure compatibility with the model.

## Result
- The client decrypts and displays the linear regression result, including Root Mean Square Error (RMSE), R-squared (R²), and accuracy metrics.

## Security
- **Data Privacy:** Homomorphic encryption ensures that sensitive data remains encrypted throughout the computation, preserving privacy.
- **Security Measures:** Implement proper security measures to protect the Paillier private key and sensitive data files ('keypair.txt' and 'encrypted_data.txt').


