import imp
from historical_data import HistoricalData
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.layers import LSTM,Dense,Dropout
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.callbacks import EarlyStopping
from plot import Plot
import numpy as np
import matplotlib.pyplot as plt

class NeuralNetwork:

    def __init__(self):
        pass

    def get_transformed_data_by_symbol(self, symbol):
        data = HistoricalData().get_historical_data()
        data = data.loc[data['Symbol'] == symbol]
        y = data['Close'].values
        del data['Close']
        del data['Name']
        del data['Symbol']
        x = data
        scaler = StandardScaler()
        x = scaler.fit_transform(x)
        y = scaler.fit_transform(y.reshape(-1,1))
        x, y = self.lstm_data_transform(x, y, num_steps=7)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
        return x_train,y_train,x_test,y_test

    def get_transformed_data(self):
        data = HistoricalData().get_historical_data()
        y = data['Close'].values
        del data['Close']
        del data['Name']
        del data['Symbol']
        x = data
        scaler = StandardScaler()
        x = scaler.fit_transform(x)
        y = scaler.fit_transform(y.reshape(-1,1))
        x, y = self.lstm_data_transform(x, y, num_steps=7)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
        return x_train,y_train,x_test,y_test

    def model_training(self,x_train,y_train):
        # training set        
        print(x_train.shape)
        print(y_train.shape)
        model = Sequential()
        model.add(LSTM(units=96, return_sequences=True, input_shape=(7, 6)))
        model.add(Dropout(0.2))
        model.add(LSTM(units=96,return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(units=96,return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(units=96))
        model.add(Dropout(0.2))
        model.add(Dense(units=1))
        model.compile(loss='mean_squared_error', optimizer='adam')
        model.fit(x_train, y_train, epochs=50, batch_size=32)
        filename = './lstm_neural_network.h5'
        model.save(filename)

    def model_prediction(self, filename, x_test):
        model = keras.models.load_model(filename)
        predictions = model.predict(x_test)
        return predictions

    def lstm_data_transform(self,x_data, y_data, num_steps=7):
        # Prepare the list for the transformed data
        X, y = list(), list()
        # Loop of the entire data set
        for i in range(x_data.shape[0]):
            # compute a new (sliding window) index
            end_ix = i + num_steps
            # if index is larger than the size of the dataset, we stop
            if end_ix >= x_data.shape[0]:
                break
            # Get a sequence of data for x
            seq_X = x_data[i:end_ix]
            # Get only the last element of the sequency for y
            seq_y = y_data[end_ix]
            # Append the list with sequencies
            X.append(seq_X)
            y.append(seq_y)
        # Make final arrays
        x_array = np.array(X)
        y_array = np.array(y)
        return x_array, y_array

    def build_lstm(self):
        x_train, y_train, x_test, y_test = neural_network.get_transformed_data()
        self.model_training(x_train, y_train)

    def predict_by_coin(self, coin):
        x_train, y_train, x_test, y_test = self.get_transformed_data_by_symbol(coin)
        y_predicted = self.model_prediction('lstm/lstm_neural_network.h5',x_test)
        return y_predicted, y_test

if __name__ == "__main__":
    neural_network = NeuralNetwork()
    predicted, actual = neural_network.predict_by_coin('ETH')
    Plot().plot_line(actual,predicted)
