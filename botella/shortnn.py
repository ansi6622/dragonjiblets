import numpy as np
import pandas as pd
from string import replace
from sklearn.feature_selection import SelectKBest
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
from sklearn.cross_validation import train_test_split
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(0)

#X_data = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
#y_data = np.array([[0,1,0,0]]).T
#n_iter = 100000

def basic_nn(X, y, n_iter):
    weights0 = 2*np.random.random((X.shape[1],42)) - 1
    weights1 = 2*np.random.random((42,1)) - 1
    y = y.reshape((3333,1))
    for j in range(n_iter):
        layer_1 = 1/(1+np.exp(-(np.dot(X,weights0))))
        layer_2 = 1/(1+np.exp(-(np.dot(layer_1,weights1))))
        layer_2_delta = (y - layer_2)*(layer_2*(1-layer_2))
        layer_1_delta = layer_2_delta.dot(weights1.T) * (layer_1 * (1-layer_1))
        weights1 += layer_1.T.dot(layer_2_delta)
        weights0 += X.T.dot(layer_1_delta)
    return layer_2


def load_data():
    true_values = ['yes','True.']
    false_values = ['no','False.']
    df = pd.read_csv('../data/churn.csv', true_values=true_values, false_values=false_values)
    df.drop(['State', 'Area Code', 'Phone'], axis=1, inplace=True)
    cols = df.columns.values
    cols = [replace(col.lower(), ' ','') for col in cols]
    cols[1], cols[-1] = 'intlplan', 'churn'
    df.columns = cols
    y = df.pop('churn').values
    df = (df - df.mean()) / df.std()
    return df, y


def keras_base_implementation(l1_nodes, l2_nodes, dropout):
    model = Sequential()
    model.add(Dense(l1_nodes, input_dim = 8, init='uniform', activation='tanh'))
    model.add(Dropout(dropout))
    model.add(Dense(l2_nodes, init='uniform', activation='tanh'))
    model.add(Dropout(dropout))
    model.add(Dense(l2_nodes, init='uniform', activation='tanh'))
    model.add(Dropout(dropout))
    model.add(Dense(l2_nodes, init='uniform', activation='tanh'))
    model.add(Dropout(dropout))
    model.add(Dense(2, init='uniform', activation='softmax'))
    #sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='mean_squared_error', optimizer="RMSprop")
    return model


def run_model(n1, n2, dropout):
    model = keras_base_implementation(n1, n2, dropout)
    start = time.clock()
    model_fit = model.fit(X_train, y_train, batch_size = 32, nb_epoch =10, show_accuracy = True)
    end = time.clock()
    return end - start, model_fit.history['acc'][-1], model_fit.history['loss'][-1]


def test_some_models():
    #num_hidden = [2,4,8,16,32,64,128]
    num_hidden = [32,64,128,256,512,1024]
    dropouts = [0, .2, .5]
    out_arr = np.zeros((len(num_hidden), len(dropouts)))
    time, final_acc, final_loss = out_arr.copy(), out_arr.copy(), out_arr.copy()
    for i in num_hidden:
        for d in dropouts:
            print i, d
            t, fa, fl = run_model(i, i, d)
            print t, fa, fl
            print num_hidden.index(i), dropouts.index(d)
            final_acc[num_hidden.index(i), dropouts.index(d)] = fa
            final_loss[num_hidden.index(i), dropouts.index(d)] = fl
            time[num_hidden.index(i), dropouts.index(d)] = t
    return time, final_acc, final_loss


def plot3d():
    '''all results from tanh, 4 layers. varying num nodes in each hidden
    layer and the dropout.'''
    times = np.array([[   0.670462,    0.826069,    0.894389], [   0.988138,    1.212797,    1.188198], [   2.516869,    2.991904,    2.885996],[   8.502693,    9.847152,   10.162426],[  31.388873,   32.783898,   32.863152],[ 123.216075,  126.547908,  126.318045]])
    fls = np.array([[ 0.09712401,  0.10034673,  0.126922  ],[ 0.09810443,  0.09818595,  0.11199282],[ 0.09753599,  0.09841711,  0.10206522],[ 0.09798478,  0.09886444,  0.10079864],[ 0.09850065,  0.09787692,  0.10022551],[ 0.097476  ,  0.09837884,  0.09798813]])
    fas = np.array([[ 0.89435774,  0.87795118,  0.8527411 ],[ 0.88835534,  0.8887555 ,  0.85394158],[ 0.89195678,  0.88835534,  0.86514606],[ 0.88795518,  0.8927571 ,  0.87955182],[ 0.8907563 ,  0.89195678,  0.88715486],[ 0.89395758,  0.89195678,  0.8927571 ]])
    fig = plt.figure()
    #times, fas, fls = test_some_models()
    # above if you wanted to do this but different
    ax = fig.add_subplot(111, projection='3d')
    num_hidden = [32,64,128,256,512,1024]
    c = np.array(6*['b','g','r']).reshape(6,3)
    s = np.array(3*num_hidden).reshape((3,6)).T
    dropouts = [0, .2, .5]
    plt.xlabel('time (s)')
    plt.ylabel('accuracy')
    ax.set_zlabel('loss', rotation = 90)
    #plt.zlabel('loss')
    ax.scatter(times, fas, fls, c = c,   s = s)
    plt.show()


if __name__=='__main__':
    df, y = load_data()
    model = SelectKBest(k = 8).fit(df.values, y)
    X = df.iloc[:,np.argsort(model.pvalues_)[:8]].values
    #neural_prediction = basic_nn(X, y, n_iter = 1000)
    #print accuracy_score(y, neural_prediction)
    y = pd.get_dummies(y).values
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    #y_train, y_test = y_train.reshape((len(y_train), 1)), y_test.reshape((len(y_test), 1))

    #model = keras_base_implementation(64, 64)
    #model_fit = model.fit(X_train, y_train, batch_size=32, nb_epoch=10, show_accuracy = True)
