
import pandas as pd #Importera toolbox för att hantera Excel filer

def FetchRecepieNames():
    "Hämta receptnamnen"

    #Läser in xls fil
    CookBook = pd.read_excel('CookBookDB.xlsx') 
    recepieList=CookBook['Name'].tolist()
    return recepieList
   # print(recepieList)

def FetchRecepie(Index):
    "Hämta recept"

    CookBook = pd.read_excel('CookBookDB.xlsx') 
    CookBook['Ingredients'] = CookBook['Ingredients'].str.replace('\n', ' <br> ')
    CookBook['HowTo'] = CookBook['HowTo'].str.replace('\n', ' <br> ')
    Namn =CookBook.iloc[Index]
    return Namn

#Recept= FetchRecepie(2)
#print( Recept.Name)
#print(Recept.Ingredients)