import os
import sys 
import pandas as pd

cwd = os.getcwd()
print("Curent Working Directory is: {0}".format(cwd)) 
os.chdir("C:\\Users\\djordje.subotic\\Desktop\\Izvestaj\\Test")
print("Curent Working Directory is: {0}".format(os.getcwd())) 

#Listing all files in directory 
print("Printing all files in current directory:")
print([i for i in os.listdir()])

katastar = "Sektor za katastar nepokretnosti.XLS"
pravni = "Sektor za pravne i opste poslove.XLS" 

#Loading Spreadsheets 
katastar_exel = pd.ExcelFile(katastar) 
print("Names Of Sheet in Excel File: ",katastar_exel.sheet_names) 

#Load sheets into Dataframe 
df1 = katastar_exel.parse('Sheet1') 
try:
	print(df1)

except(UnicodeDecodeError, e):
	print(e)
