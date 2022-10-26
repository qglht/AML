import pandas as pd
from typing import Tuple


class Data:
    """Class to digest the data and do the preprocessing steps"""

    def __init__(self, x_train: str, y_train: str) -> None:
        """digest the x_train and y_train csv files

        Args:
            x_train (str): path of the file
            y_train (str): path of the file
        """
        self.x_train_path = x_train
        self.y_train_path = y_train
        self.x_train, self.y_train = self.digest_file()

    def digest_file(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """digest file to pd.DataFrame

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: digested files
        """
        return (pd.read_csv(self.x_train_path), pd.read_csv(self.y_train_path))

    def pipeline(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """All the pipeline to digest the data

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]
        """
        return self.x_train, self.y_train
