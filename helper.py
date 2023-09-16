import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import hashlib
from xgboost import XGBClassifier
import pickle as pc
from numpy import ndarray




loaded_model = pc.load(open('trained_model.sav','rb'))


# Making prediction system

input_data = (2,    5337.77,41720.00,36382.23,41898.0,40348.79)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)



if (prediction[0] == 0):
    print('The Transaction is Not Fraud')
else:
    print('The transaction is Fraud')