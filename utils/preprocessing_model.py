import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
import pickle
from xgboost import XGBRegressor


class ModellingData:
    def __init__(self):
        """
        load our x (target price) and y (feature for the model).
        create the model and fit it with our train set.
        use self.model() to use it
        """
        self.load_file()
        self.make_pipeline()
        self.split_df()
        self.preprocessor(self.numerical_features,self.categorical_features)
        self.model()
        self.fit_model()

    def load_file(self, file_name="./Data8.csv"):
        """
        load data drom csv and define x and y (price target)
        :param file_name: name of the csv with data set ( Data8 if None)
        :return: None
        """
        self.df = pd.read_csv(file_name, sep=",")
        self.X = self.df.drop("Price", axis=1)
        self.y = self.df["Price"]

    def make_pipeline(self):
        self.numerical_features = ['Locality', 'Number of rooms', 'Area', 'Terrace Area', 'Garden Area',
                                   'Surface of the land']
        self.categorical_features = [
                                    'Type of property','Fully equipped kitchen', 'Furnished', 'Open fire',
                                    'Number of facades','Swimming pool', 'State of the building', 'Province', 'Region'
                                     ]
        self.numerical_pipeline = make_pipeline(SimpleImputer(), StandardScaler())
        self.categorical_pipeline = make_pipeline(SimpleImputer(strategy="most_frequent"),
                                                  OneHotEncoder())

    def split_df(self):
        """
        split data set with train and test data (80/20)
        :return: x and y train and test dataset
        """
        self.X_train, self.X_test, self.y_train, self.y_test = \
            train_test_split(self.X, self.y, test_size=0.2, random_state=42)

    def preprocessor(self, numerical_features, categorical_features):
        """
        normalize the data to be train into the ml model with the numerical pipeline(standard scaler)
        and our categorical pipeline (most frequent, one hot encoder)
        :param numerical_features: all column with int feature than can't be categorised
        :param categorical_features: all column with categorical feature
        :return: preprocess data that ara normalized with a make_column_transformer
        """
        self.preprocessor = make_column_transformer((self.numerical_pipeline, numerical_features),
                                                    (self.categorical_pipeline, categorical_features))
        return self.preprocessor

    def model(self):
        """
        create the model with XGBregressor and preprocess data
        :return: model
        """
        self.model = make_pipeline(self.preprocessor, XGBRegressor())
        return self.model

    def fit_model(self):
        """
        fit model with train data
        :return: None
        """
        self.model.fit(self.X_train, self.y_train)

    def prediction(self, value):
        """
        predict price by parameter value
        :param value: df with x param for predict price
        :return: predicted price
        """
        return self.model.predict(value)

    def save_model(self, file_name):
        """
        Save model into pickle file
        :param file_name: name to give to the file
        :return: None
        """
        pickle.dump(self.model, open(file_name, "wb"))

    def load_model(self, model_file_name):
        """
        load model that have been saved by saved model
        :param model_file_name:
        :return: None
        """
        loaded_model = pickle.load(open(model_file_name, "rb"))
        return loaded_model

    def prediction_saved_model(self, model_name, value):
        """
        predict price of a house with a saved model, for x parameter
        :param model_name: name of the model saved
        :param value: x feature on the same form than a X_train(df with same column)
        :return: prediction of price with there parameter
        """
        loaded_model = pickle.load(open(model_name, "rb"))
        return loaded_model.predict(value)
