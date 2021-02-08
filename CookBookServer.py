#Importerar toolbox Flask som är en Web server
from flask import Flask
from flask import render_template
import CookBook

#app är ett "web server objekt" av klassen Flask
app = Flask(__name__)

""" @app.route('/')
def home():
    print(2)
    return('')
 """
@app.route('/')
def home():
    ReceptNamn=CookBook.FetchRecepieNames()
    return render_template('index_start_page.html', title='Recept Startsida', recepie_name=ReceptNamn)

@app.route('/<int:index>')
def ReceptIndex(index):
    Recept= CookBook.FetchRecepie(index-1)
    print( Recept.Name)
    return render_template('index_recepie_page.html',
     title='Recept', 
     Name= Recept.Name, 
     Ingredients=Recept.Ingredients, 
     HowTo=Recept.HowTo,
     Region=Recept.Region,
     Keyword=Recept.Type)

