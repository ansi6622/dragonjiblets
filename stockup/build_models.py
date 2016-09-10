import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import cPickle as pickle


if __name__=='__main__':
    df = pd.read_csv('stock_data.csv')

    models = {}
    for symbol in df["symbol"].unique():
        # pandas trimming and labeling things, date was in format models couldnt read.
        X = df.loc[df['symbol'] == symbol].drop(['symbol', 'close', "date"], axis=1).values
        y = df.loc[df['symbol'] == symbol, "close"].values

        model = RandomForestRegressor(n_estimators=750)
        model.fit(X, y)

        models[symbol] = model

    with open('models.pkl', 'w') as f:
        pickle.dump(models, f)
