import pandas as pd
class LoadAndFilterData():
    def __init__(self):
        #Loading the csv file into sales_data 
        self.sales_data=pd.read_csv("//Users//nuthanreddyvaddireddy//Downloads//SalesKaggle3 2.csv")
        print(self.sales_data)
    def removeData(self):
        #Removing the identified columns in the Task 1 and loading the data into new variable
        self.newdata=self.sales_data.drop(columns=['LowUserPrice','ReleaseYear','LowNetPrice','Order','MarketingType'])
        print(self.newdata)
        #Loading the updated data into new csv
        self.newdata.to_csv("modifited_data.csv",index=False)     
obj=LoadAndFilterData()
obj.removeData()

