import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn. linear_model import LinearRegression, LogisticRegression
def get_train_fit_times(users, logs): times = {}
for user in range(len(users)):
curr_df = logs[logs['user_id'] == user] sec = 0
for time in curr_df['seconds']:
            sec += int(time)
        times[user] = sec
return times
def get_test_fit_times(test_users, test_logs): times = {}
    start = test_users.at[0, 'user_id']
    user_length = len(test_users)
    end = test_users.at[user_length-1, 'user_id']
for user in range(start, end+1):
curr_df = test_logs[test_logs['user_id'] == user] sec = 0
for time in curr_df['seconds']:
            sec += int(time)
        times[user] = sec
return times
