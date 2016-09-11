import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import cPickle as pickle

def build_models(filename, modelname):
    df = pd.read_csv(filename)

    models = {}
    for symbol in df["symbol"].unique():
        # pandas trimming and labeling things, date was in format models couldnt read.
        X = df.loc[df['symbol'] == symbol].drop(['symbol', 'close', "date"], axis=1).values
        y = df.loc[df['symbol'] == symbol, "close"].values

        print 'Building model for {}'.format(symbol)
        print X.shape
        model = RandomForestRegressor(n_estimators=750)
        model.fit(X, y)

        models[symbol] = model

    with open(modelname, 'w') as f:
        pickle.dump(models, f)
