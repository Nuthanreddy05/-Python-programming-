# creating a product class 
class Product:
    #Initialize attributes using the individual values
    def __init__(self,File_type,SKU_number,SoldFlag,SoldCount,ReleaseNumber,New_Release_Flag,StrengthFactor,PriceReg,ItemCount):
        self.File_type=File_type
        self.SKU_number=SKU_number
        self.SoldFlag=SoldFlag
        self.SoldCount=SoldCount
        self.ReleaseNumber=ReleaseNumber
        self.New_Release_Flag=New_Release_Flag
        self.StrengthFactor=StrengthFactor
        self.PriceReg=PriceReg
        self.ItemCount=ItemCount
    #Initialize attributes using the individual values of the csv file
    def __init__(self, csv_lin):
    #By Split(',') we split the data into values from csv
        values = csv_lin.split(',')
    #Initialize attributes using individual values
        self.File_type=values[0]
        self.SKU_number=values[1]
        self.SoldFlag=values[2]
        self.SoldCount=values[3]
        self.ReleaseNumber=values[4]
        self.New_Release_Flag=values[5]
        self.StrengthFactor=values[6]
        self.PriceReg=values[7]
        self.ItemCount=values[8]
#Taking a csv line as a example       
csv_lin="Active,3016759,0.0,0.0,2,1,4323581.0,0.0,26"
pr=Product(csv_lin)
print(pr.File_type)
print(pr.SKU_number)
print(pr.SoldFlag)
print(pr.SoldCount)
print(pr.ReleaseNumber)
print(pr.New_Release_Flag)
print(pr.StrengthFactor)
print(pr.PriceReg)
print(pr.ItemCount)




