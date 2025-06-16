import csv
import pandas as pd
#creating a Datamanger class
class DataManager:
    def __init__(self):
        #loading the modifited data into preprocceseddata
        self.preprocceseddata=pd.read_csv("modifited_data.csv")
    def formatted(self):
        #Creating a empty list
        data=[]
        #opening the 'modified_data.csv' file in read mode using a with statement
        with open('modifited_data.csv','r') as pr:
            ## Create a CSV reader
            reader=csv.reader(pr)
            # Read the first row to get the column headers (keys)
            keys=next(reader)
            for row in reader:
                #Adding the keys and row to data
                data.append(dict(zip(keys,row)))
        #Calculating the maximum length of each column
        leng_SKU_number=max(len(sku["SKU_number"])for sku in data)
        leng_File_Type=max(len(FT["File_Type"])for FT in data)
        leng_SoldCount=max(len(SC["SoldCount"])for SC in data)
        leng_SoldFlag=max(len(SF["SoldFlag"])for SF in data)
        leng_ReleaseNumber=max(len(RN["ReleaseNumber"])for RN in data)
        leng_New_Release_Flag=max(len(NR["New_Release_Flag"])for NR in data)
        leng_StrengthFactor=max(len(SF["StrengthFactor"])for SF in data)
        leng_PriceReg=max(len(PR["PriceReg"])for PR in data)
        leng_ItemCount=max(len(IC["ItemCount"])for IC in data)
        #Printing the formatted header between each column
        print("{:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}}".format("SKU_number",leng_SKU_number,
        "File_Type",leng_File_Type,"SoldCount",leng_SoldCount,"SoldFlag",leng_SoldFlag,"ReleaseNumber",leng_ReleaseNumber,
        "New_Release_Flag",leng_New_Release_Flag,"StrengthFactor",leng_StrengthFactor,"PriceReg",leng_PriceReg,
        "ItemCount",leng_ItemCount))
        #Printing the separator line between the columns headings and the values of the columns
        print("."*(leng_SKU_number+leng_File_Type+leng_SoldCount+leng_SoldFlag+leng_ReleaseNumber+leng_New_Release_Flag+leng_StrengthFactor+leng_PriceReg+leng_ItemCount+71))
        for d in data[:12]:
            print("{:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}} ".
            format(d["SKU_number"],leng_SKU_number,d["File_Type"],leng_File_Type,d["SoldCount"],
            leng_SoldCount,d["SoldFlag"],leng_SoldFlag,d["ReleaseNumber"],leng_ReleaseNumber,d["New_Release_Flag"],
            leng_New_Release_Flag,d["StrengthFactor"],leng_StrengthFactor,d["PriceReg"],leng_PriceReg,d["ItemCount"],leng_ItemCount))
    def sort(self,column):
        #Sorting the data as per column value
        return self.preprocceseddata.sort_values(by=column,inplace=True)

    def Filter(self,condition):
        #Filtering the data as per the condition
        return self.preprocceseddata[condition]
    def newdata():
        return class_manager_f
obj=DataManager()
obj.formatted()
# sorting the data in ascending order as per the number of items in the column
print("The sortted data according to itemcount:")
print(obj.sort("ItemCount"))
#Filtering the data which as the slodflag as zero
print("The Filtered data with soldFlag=0:")
condition=obj.preprocceseddata['SoldFlag']==0
print(obj.Filter(condition))
Class_manager_f=[obj.sort("ItemCount"),obj.Filter(condition)]  
print(Class_manager_f)