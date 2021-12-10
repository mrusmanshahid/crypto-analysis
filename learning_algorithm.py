from historical_data import HistoricalData
import numpy
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


class LearningAlgorithm:

    def __init__(self):
        pass

    def get_dataset(self):
        # load the dataset
        dataframe = HistoricalData().get_historical_data()
        dataset = dataframe.values
        #dataset = dataset.astype('float32')
        return dataset

    def split_data(self,dataset):
        # split into train and test sets
        train_size = int(len(dataset) * 0.67)
        test_size = len(dataset) - train_size
        train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
        print(len(train), len(test))
        return train,test

    def normalize_data(self,dataset):
        # normalize the dataset
        scaler = MinMaxScaler(feature_range=(0, 1))
        dataset = scaler.fit_transform(dataset)
        return dataset

    def model_training(self):
        # fix random seed for reproducibility
        numpy.random.seed(7)
        dataset = self.get_dataset()
        #dataset = self.normalize_data(dataset)
        train, test = self.split_data(dataset)

if __name__ == "__main__":
    LearningAlgorithm().model_training()
