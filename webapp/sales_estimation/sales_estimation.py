#Class Definition
#Imports
import pandas as pd
import numpy as np
import inflection
import pickle
import datetime
import math

class Sales_Estimation(object):
    def __init__(self):
        self.scaler_competition_distance = pickle.load (open('parameters/scaler_competition_distance.pkl', 'rb'))
        self.scaler_competition_time_month = pickle.load (open('parameters/scaler_competition_time_month.pkl', 'rb'))
        self.scaler_promo_time_week = pickle.load (open('parameters/scaler_promo_time_week.pkl', 'rb'))
        self.scaler_year = pickle.load (open('parameters/scaler_year.pkl', 'rb'))
        self.enc_store_type = pickle.load(open('parameters/enc_store_type.pkl', 'rb'))

    #Cleaning Data
    def data_clean(self, df):

        #Rename columns
        cols_old = ['Store', 'DayOfWeek', 'Date', 'Open', 'Promo',
                    'StateHoliday', 'SchoolHoliday', 'StoreType', 'Assortment',
                    'CompetitionDistance', 'CompetitionOpenSinceMonth',
                    'CompetitionOpenSinceYear', 'Promo2', 'Promo2SinceWeek',
                    'Promo2SinceYear', 'PromoInterval']
        snakecase = lambda x: inflection.underscore(x)
        cols_new = list(map(snakecase, cols_old))
        df.columns = cols_new

        #Changing date type
        df['date'] = pd.to_datetime(df['date'])

        #Replace NA's from dataset
        #competition_distance: null data will be 150000 (double of max distance on the dataset)
        df['competition_distance'] = df['competition_distance'].apply(lambda x: 150000 if math.isnan(x) else x)

        #competition_open_since_month: null data will be the same month of the date on the dataset
        df['competition_open_since_month'] = df.apply(lambda x: x['date'].month if math.isnan(x['competition_open_since_month']) else x['competition_open_since_month'], axis=1)

        #competition_open_since_year: null data will be the same year of the date on the dataset
        df['competition_open_since_year'] = df.apply(lambda x: x['date'].year if math.isnan(x['competition_open_since_year']) else x['competition_open_since_year'], axis=1)

        #promo2_since_week: null data will be the same week of the date on the dataset
        df['promo2_since_week'] = df.apply(lambda x: x['date'].week if math.isnan(x['promo2_since_week']) else x['promo2_since_week'], axis=1)

        #promo2_since_year: null data will be the same year of the date on the dataset
        df['promo2_since_year'] = df.apply(lambda x: x['date'].year if math.isnan(x['promo2_since_year']) else x['promo2_since_year'], axis=1)

        #promo_interval: null data will be the interval based on the month of the date on the dataset
        month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        df['promo_interval'].fillna(0, inplace=True)
        df['month'] = df['date'].dt.month.map(month_map)
        df['is_promo'] = df[['promo_interval', 'month']].apply(lambda x: 0 if x['promo_interval'] == 0 else 1 if x['month'] in x['promo_interval'].split(',') else 0, axis=1)

        #Adjusting data types after adjust NA's
        df['competition_open_since_month'] = df['competition_open_since_month'].astype('int64')
        df['competition_open_since_year'] = df['competition_open_since_year'].astype('int64')
        df['promo2_since_week'] = df['promo2_since_week'].astype('int64')
        df['promo2_since_year'] = df['promo2_since_year'].astype('int64')

        return df

    #Dataset Feature Engineering
    def feature_eng(df):
        
        #year
        df['year'] = df['date'].dt.year

        #month
        df['month'] = df['date'].dt.month

        #day
        df['day'] = df['date'].dt.day

        #week of year
        df['week_of_year'] = df['date'].dt.weekofyear

        #year week
        df['year_week'] = df['date'].dt.strftime('%Y-%W')

        #competition distance
        df['competition_since'] = df.apply(lambda x: datetime.datetime(year=x['competition_open_since_year'], month=x['competition_open_since_month'], day=1), axis=1)

        df['competition_time_month'] = ((df['date'] - df['competition_since'])/30).apply(lambda x: x.days).astype('int64')

        #promo since
        df['promo_since'] = df['promo2_since_year'].astype(str) + '-' + df['promo2_since_week'].astype(str)

        df['promo_since'] = df['promo_since'].apply(lambda x: datetime.datetime.strptime(x+'-1', '%Y-%W-%w') - datetime.timedelta(days=7))

        df['promo_time_week'] = ((df['date'] - df['promo_since'])/7).apply(lambda x: x.days).astype('int64')

        #assortment
        df['assortment'] = df['assortment'].apply(lambda x: 'basic' if x=='a' else 'extra' if x=='b' else 'extended')

        #state holiday
        df['state_holiday'] = df['state_holiday'].apply(lambda x: 'public_holiday' if x=='a' else 'easter_holiday' if x=='b' else 'christmas' if x=='c' else 'regular_day')

        return df

    #Data Filtering
    def data_filtering(df):

        #Filtering only Open Stores with at least One Sell
        cond = (df['open'] != 0)
        df = df[cond]

        #Filtering relevant columns for algoritms application
        cols_drop = ['open', 'promo_interval']
        df = df.drop(cols_drop, axis=1)

        return df

    #Data Preparation
    def data_prep(self, df):

        #Rescaling on Variables
        #competition_distance
        df['competition_distance'] = self.scaler_competition_distance.fit_transform(df[['competition_distance']].values)

        #competition_time_month
        df['competition_time_month'] = self.scaler_competition_time_month.fit_transform(df[['competition_time_month']].values)

        #promo_time_week
        df['promo_time_week'] = self.scaler_promo_time_week.fit_transform(df[['promo_time_week']].values)

        #year
        df['year'] = self.scaler_year.fit_transform(df[['year']].values)

        #Encoding
        #One Hot Encoding - state_holiday
        df = pd.get_dummies(df, prefix=['state_holiday'], columns=['state_holiday'])

        #Label Encoding - store_type
        df['store_type'] = self.enc_store_type.fit_transform(df['store_type'])

        #Ordinal Encoding - assortment
        assortment_dict = {'basic': 1, 'extra': 2, 'extended': 3}
        df['assortment'] = df['assortment'].map(assortment_dict)

        #Transformation - Ciclical Variables (Nature Transformation)
        #month
        df['month_sin'] = df['month'].apply(lambda x: np.sin(x*(2*np.pi/12)))
        df['month_cos'] = df['month'].apply(lambda x: np.cos(x*(2*np.pi/12)))
        
        #day
        df['day_sin'] = df['day'].apply(lambda x: np.sin(x*(2*np.pi/30)))
        df['day_cos'] = df['day'].apply(lambda x: np.cos(x*(2*np.pi/30)))
        
        #week_of_year
        df['week_of_year_sin'] = df['week_of_year'].apply(lambda x: np.sin(x*(2*np.pi/52)))
        df['week_of_year_cos'] = df['week_of_year'].apply(lambda x: np.cos(x*(2*np.pi/52)))
        
        
        #day_of_week
        df['day_of_week_sin'] = df['day_of_week'].apply(lambda x: np.sin(x*(2*np.pi/7)))
        df['day_of_week_cos'] = df['day_of_week'].apply(lambda x: np.cos(x*(2*np.pi/7)))

        #Selected Columns
        cols_sel = ['store',
                    'promo',
                    'store_type',
                    'assortment',
                    'competition_distance',
                    'competition_open_since_month',
                    'competition_open_since_year',
                    'promo2',
                    'promo2_since_week',
                    'promo2_since_year',
                    'competition_time_month',
                    'promo_time_week',
                    'month_sin',
                    'month_cos',
                    'day_sin',
                    'day_cos',
                    'week_of_year_sin',
                    'week_of_year_cos',
                    'day_of_week_sin',
                    'day_of_week_cos']

        return df [cols_sel]

    #Get Predictions
    def get_predict(self, model, original_data, test_data):

        #Prediction
        pred = model.predict(test_data)

        #Join prediction into original data
        original_data['prediction'] = np.expm1(pred)

        return original_data.to_json(orient='records', date_format='iso')