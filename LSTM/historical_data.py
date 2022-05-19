import os
import logging
import pandas as pd

class HistoricalData:

    def __init__(self):
        HistoricalData.Loaded_Data = None

    def get_files(self):
        logging.info("Loading files for historical data")
        historical_files = []
        for file in os.listdir("lstm/resources"):
            if file.endswith(".csv"):
                path = os.path.join("lstm/resources", file)
                logging.info(f"loading -> {path}")
                historical_files.append(path)
        return historical_files
        
    def load_historical_data_from_files(self):
        logging.info("Reading files for historical data")
        frames = []
        files = self.get_files()
        for file in files:
            logging.info(f"Reading files -> {file}")
            data_frame = pd.read_csv(file, index_col='Date',parse_dates=True,infer_datetime_format=True)
            frames.append(data_frame)
        result = pd.concat(frames)
        return result

    def get_historical_data(self):
        if HistoricalData.Loaded_Data == None:
            logging.info("Starting load process")
            HistoricalData.Loaded_Data = self.load_historical_data_from_files()
            return HistoricalData.Loaded_Data
        logging.info("Delivery already loaded data from memory")
        return HistoricalData.Loaded_Data 
