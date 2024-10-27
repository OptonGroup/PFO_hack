"""
Machine Learning Model Ensemble

This module defines a Model class that combines multiple machine learning models
for making predictions. It currently uses LightGBM, CatBoost and XGBoost models.

Dependencies:
- pandas
- lightgbm
- catboost
- xgboost

The Model class loads pre-trained models and provides a method to generate
predictions based on input features.

Usage:
    model = Model()
    predictions = model.get_ans(input_data)

Note: Ensure all dependencies are installed and the model files are in the correct location.
"""


import pandas as pd
import lightgbm as lgb
import catboost as cb
# import xgboost as xgb

class Model():
    """
    A class that combines multiple machine learning models for predictions.

    This class loads pre-trained LightGBM, CatBoost and XGBoost models,
    and provides a method to generate predictions using an ensemble approach.

    Attributes:
        catboost_model (cb.CatBoostRegressor): Loaded CatBoost model
        lightgbm_model (lgb.Booster): Loaded LightGBM model
        xgboost_model (xgb.XGBRegressor): Loaded XGBoost model
    """
    
    def __init__(self):
        self.catboost_model = cb.CatBoostRegressor()

        self.catboost_model.load_model('best_catboost_model.cbm')

        self.lightgbm_model = lgb.LGBMRegressor()
        self.lightgbm_model = lgb.Booster(model_file='lgbr_base.txt')

        # self.xgboost_model = xgb.XGBRegressor()
        # self.xgboost_model.load_model('best_xgboost_model.json')


    def get_ans(self, info):
        """
        Generate predictions using the ensemble of models.

        This method takes input features, uses them to generate predictions from
        each loaded model, and then averages these predictions.

        Args:
            info (dict or pandas.DataFrame): Input features for prediction.
                                             Must contain columns: 'T', 'B', 'C1', 'C2', 'C3', 'M1', 'M2', 'M3'

        Returns:
            numpy.ndarray: Array of predictions, clipped to a maximum of 1 and scaled to percentage (0-100).

        Note:
            The method currently averages predictions from LightGBM and CatBoost models.
            XGBoost predictions are commented out.
        """
        x = pd.DataFrame(info)[['T', 'B', 'C1', 'C2', 'C3', 'M1', 'M2', 'M3']]
        # pred = ( self.lightgbm_model.predict(x) + self.catboost_model.predict(x) + self.xgboost_model.predict(x)) / 3
        pred = ( self.lightgbm_model.predict(x) + self.catboost_model.predict(x)) / 2
        return pred.clip(max=1)*100