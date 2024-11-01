import os
import pandas as pd

def load_and_clean_data(file_path, file_name):
    os.chdir(file_path)
    
    #load the data
    data = pd.read_csv(file_name)
    
    #wrangle data
    data['PreferredPaymentMode'].replace({'CC': 'Credit Card', 'COD': 'Cash on Delivery'}, inplace=True)
    data['PreferedOrderCat'].replace({'Mobile': 'Mobile Phone'}, inplace=True)
    data['PreferredLoginDevice'].replace({'Phone': 'Mobile Phone'}, inplace=True)
    
    #change col types
    data['CustomerID'] = data['CustomerID'].astype(str)
    data['Churn'] = data['Churn'].astype(str)
    data['CityTier'] = data['CityTier'].astype(str)
    
    return data

#path= "/Users/theomunozp/Desktop/Personalisation"
#file_name= "dohtem_ecommerce_customers.csv"
# ata= load_and_clean_data(path, file_name)
