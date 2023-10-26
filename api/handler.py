#API Handler
#Imports
import pandas as pd
import pickle
from flask import Flask, request, Response
from sales_estimation.sales_estimation import Sales_Estimation

#Loading Model
model = pickle.load(open('D:/Data Science/Projetos/Regressão Linear - Estimativa de Vendas/models/xgb_model.pkl', 'rb'))

#Initialize API
app = Flask (__name__)

@app.route('/sales_estimation/predict', methods=['POST'])
def sales_predict():
    test_json = request.get_json()

    #If is data
    if test_json:
        #Unique Sample
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0])

        #Multiple Sample
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        #Instance of Main Class
        pipeline = Sales_Estimation()

        #Data Cleaning
        df1 = pipeline.data_clean(test_raw)

        #Feature Engineering
        df2 = pipeline.feature_eng(df1)

        #Data Filtering
        df3 = pipeline.data_filtering(df2)
        
        #Data Preparation
        df4 = pipeline.data_prep(df3)

        #Prediction
        df_response = pipeline.get_prediction(model, test_raw, df4)

        return df_response

    else:
        return Response('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run('0.0.0.0')