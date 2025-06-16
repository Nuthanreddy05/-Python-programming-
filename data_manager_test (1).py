#importing the Datamanager class from Data_manager
from data_manager import DataManager
obj=DataManager()
# sorting the data in ascending order as per the number of items in the column
print(obj.sort("ItemCount"))
obj.formatted()
#Filtering the data which as the slodflag as zero
condition=obj.preprocceseddata['SoldFlag']==0
print(obj.Filter(condition))
Class_manager_f=[obj.sort("ItemCount"),obj.Filter(condition)]  
print(Class_manager_f)
