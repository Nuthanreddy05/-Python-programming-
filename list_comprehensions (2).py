import pandas as pd
#creating a list_comprehensions class 
class list_comprehensions():
    def __init__(self):
        #loading the modifited data into data
        data=pd.read_csv("modifited_data.csv")
        #Defining the strengthfactor value
        StrengthFactor=334011
        #Gives the sku_numbers of the product which as the higher strengthfactor then the defined the strenghtfactor
        NEW_SKU_number= [NEW_SKU for NEW_SKU in data.loc[data["StrengthFactor"] >StrengthFactor,"SKU_number"]]
        print(NEW_SKU_number)
obj=list_comprehensions()
obj
