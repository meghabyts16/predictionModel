class UserPredictor:
    def ___init___(self): 
        self.model = None

    def fit(self, users, logs, train_y):
        badges = {'gold':3, 'silver':2, 'bronze':1} 
        users['badge'] = users['badge'].replace(badges)

        times = get_train_fit_times(users,logs)

        users['total_seconds'] = users['user_id'].map(times)

        users = users.set_index('user_id')
        train_y = train_y.set_index('user_id')
        df = pd.merge(users, train_y, on='user_id')
        train, test = train_test_split(df, test_size=0.2, random_state = 250) 
        xcols = ['past_purchase_amt', 'age', 'badge', 'total_seconds']
        ycol = 'y'
        model = LogisticRegression()
        self.model = model.fit(train[xcols], train[ycol])
        return self.model

    def predict(self, test_users, test_logs):
        test_times = get_test_fit_times(test_users, test_logs) 
        test_users['total_seconds'] = test_users['user_id'].map(test_times) 
        badges = {'gold': 3, 'silver': 2, 'bronze': 1}
        test_users['badge'] = test_users['badge'].replace(badges) 
        test_users = test_users.set_index('user_id')
        test_df = test_users
        xcols = ['past_purchase_amt', 'age', 'badge', 'total_seconds'] 
        return self.model.predict(test_df[xcols])
        
    def get_test_fit_times(test_users, test_logs):
        times = {}
        start = test_users.at[0, 'user_id']
        user_length = len(test_users)
        end = test_users.at[user_length - 1, 'user_id'] 
        for user in range(start, end + 1):
            curr_df = test_logs[test_logs['user_id'] == user] 
            sec = 0
            for time in curr_df ['seconds']:
                sec += int(time)
            times[user] = sec
        return times