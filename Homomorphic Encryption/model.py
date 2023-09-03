import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class Linmodel:
    def __init__(self):
        pass
    
    def results(self):
        # Read the data
        df = pd.read_csv('insurance_preprocessed.csv')
        y = df['charges']
        X = df.drop(['charges'], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
        # Train the model
        reg = LinearRegression().fit(X_train, y_train)
        y_pred = reg.predict(X_test)
        RMSE =  np.sqrt(mean_squared_error(y_test, y_pred))
        R = r2_score(y_test, y_pred)
        return reg, y_pred, RMSE, R


    def getCoef(self):
        return self.results()[0].coef_
    
    
def main():
    coef = Linmodel().getCoef()
    print(coef)
    return coef

if __name__ == '__main__':
    main()
