from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session

from flask import render_template

from flask import json

from urllib.request import urlopen

import sqlite3


app = Flask(__name__)


@app.route('/')

def hello_world():

    return render_template('hello.html')


@app.route('/consultation/')

def ReadBDD():

    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM client;')

    data = cursor.fetchall()

    conn.close()

    return render_template('read_data.html', data=data)

@app.route('/c_ajouter_client', methods=['GET', 'POST'])
def ajouter_client():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        adresse = request.form['adresse']
        phone = request.form['phone']
        
        # Insérer les données dans la base de données (ici, je suppose que tu as une table 'clients')
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        if conn is not None:
            cursor.execute("INSERT INTO client (nom, prenom, adresse, phone, email) VALUES (?, ?, ?, ?, ?);", (nom, prenom, adresse, phone, email ))
            conn.commit()
            conn.close()
            return redirect('/consultation/')
        else:
            return 'Erreur de connexion à la base de données'

        
    return render_template('ajouter_client.html')                                   
                                                                                     

                                                                                     
@app.route('/t_chercher_client', methods=['GET', 'POST'])                            
                                                                                     
def chercher_client():                                                               
                                                                                     
    data = []  # Define data as an empty list                                        
                                                                                     
    if request.method == 'POST':                                                     
                                                                                     
        # Récupérer les données du formulaire                                        
                                                                                     
        nom = request.form['nom']                                                    
                                                                                     
                                                                                     
        # ici, je suppose que tu as une table 'clients'                              
                                                                                     
        conn = sqlite3.connect('database.db')                                        
                                                                                     
        cursor = conn.cursor()                                                       
                                                                                     
        if conn is not None:                                                         
                                                                                     
            cursor.execute('SELECT * FROM clients WHERE nom LIKE ?', ('%' + nom + '%',))                                                                                  
                                                                                     
            data = cursor.fetchall()                                                 
                                                                                     
            conn.close()                                                             
                                                                                     
            # Rendre le template HTML et transmettre les données                     
                                                                                     
            return render_template('read_data.html', data=data)                      
                                                                                     
        else:                                                                        
                                                                                     
            return 'Erreur de connexion à la base de données'                        
                                                                                     

                                                                                     
    # Rendre le template HTML et transmettre les données                             
                                                                                     
    return render_template('search_data.html', data=data)                            
                                                                                     
                                                                                     
if __name__ == "__main__":                                                           
                                                                                     
  app.run(debug=True)  
