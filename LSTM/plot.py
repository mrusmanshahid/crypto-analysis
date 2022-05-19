import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix

class Plot:

    def plot_line(self, y_test, y_predicted):
        plt.plot(y_predicted, label = "predicted values")
        plt.plot(y_test, label = "actual values")
        plt.title('prediction analysis')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()
        plt.show()
    
    def save_fig(self, y_test, y_predicted, title):
        fig = plt.figure(figsize=(30, 6))
        plt.plot(y_predicted, label = f"Predicted values for {title}")
        plt.plot(y_test, label = f"Actual values for {title}")
        plt.title(f'Prediction analysis for {title}')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()     
        fig.savefig(f'lstm/outputs/{title}.png', dpi=fig.dpi)
