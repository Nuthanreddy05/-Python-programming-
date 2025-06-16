import pandas as pd
from data_manager import DataManager
import json
from product import Product
import pickle
class SaveAndLoadData:
    def __init__(self,Class_manager_f):
        #loading the sorted and filterred data 
        self.data=pd.read_csv("Class_manager_f.csv")
    def Convertdftodict(self,newfile):
        #converting dataframe into list of dictionary 
        newdata=self.data.to_dict(orient="records")
        #converting the list of dictionary into json
        with open(newfile, 'w') as f:
            json.dump(newdata,f,indent=4)
object1= SaveAndLoadData('Class_manager_f.csv')
object1.Convertdftodict('filtered_sorted_data.json')
pr=Product
#save the product objects to a file using pickle
with open("Product.pk1",'wb') as file:
    pickle.dump(Product,file)
#loading the python objects from the file
with open('Product.pk1','rb') as file:
    loaded_Product=pickle.load(file)
