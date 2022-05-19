import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix

class Plot:

    def plot_confusion_matrix(self, y_test, y_predict):
        y_predict = y_predict.argmax(1)
        class_hate = pd.DataFrame(confusion_matrix(y_test[:,0], y_predict==0))
        class_offensive = pd.DataFrame(confusion_matrix(y_test[:,1], y_predict==1))
        class_neither = pd.DataFrame(confusion_matrix(y_test[:,2], y_predict==2))

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5))
        sn.set(font_scale=1.5)
        sn.heatmap(class_hate, cmap="cool", annot=True, fmt='g', ax=ax1, cbar=False)
        sn.heatmap(class_offensive, cmap="Greens", annot=True, fmt='g', ax=ax2, cbar=False)
        sn.heatmap(class_neither, cmap="YlGnBu", annot=True, fmt='g', ax=ax3, cbar=False)

        # ax1.set_ylabel('True')
        # ax2.set_ylabel('True')
        # ax3.set_ylabel('True')
        # ax1.set_xlabel('Predicted')
        # ax2.set_xlabel('Predicted')
        # ax3.set_xlabel('Predicted')
        # ax1.set_title('Hate')
        # ax2.set_title('Offensive')
        # ax3.set_title('Neither')

        plt.tight_layout()
        plt.show(block=True)

    def plot_line(self, y_test, y_predicted):
        plt.plot(y_predicted, label = "predicted values")
        plt.plot(y_test, label = "actual values")
        plt.title('prediction analysis')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.legend()
        plt.show()