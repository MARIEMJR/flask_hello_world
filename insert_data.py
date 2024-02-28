import sqlite3

# Fonction pour créer une connexion à la base de données
def create_connection():
    return sqlite3.connect('database.db')

# Fonction pour exécuter une requête SQL
def execute_query(connection, query):
    with connection:
        return connection.execute(query).fetchall()

# Fonction pour insérer des données dans la table 'park'
def insert_park(connection):
    park_data = [
        (20, 20),
        (30, 20),
        (20, 10)
    ]
    query_insert = "INSERT INTO park (nbreplaces, nbstockagence) VALUES (?, ?)"
    query_select = "SELECT * FROM park where idpark=1"
    with connection:
        connection.executemany(query_insert, park_data)
        connection.commit()

    result = execute_query(connection, query_select)
    print("Données dans la table 'park':")
    print(result)

def insert_client(connection):
    client_data = [
            ('Hertz', 'top', 'Paris', '0654789621','hertz.top@yahoo.fr'),
            ('Martin', 'Marie', '456 Avenue des Fleurs', '0987654321', 'marie.martin@email.com'),
            ('Lefevre', 'Pierre', '789 Boulevard des Pièces', '0654321098', 'pierre.lefevre@email.com'),
            ('Dubois', 'Sophie', '987 Avenue de la Carrosserie', '0123456789', 'sophie.dubois@email.com'),
            ('Will', 'Smith', '20B Jardins Boieldieu, 92800 Puteaux', '0752513438', 'will.smith@gmail.com'),
            ('Renault', 'Nathalie', '321 Avenue des Batteries', '0876543210', 'nathalie.renault@email.com'),
            ('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris', '0763417536','thomas.lefevre@gmail.com'),
            ('Moreau', 'Isabelle', '654 Boulevard des Phares', '0987654321', 'isabelle.moreau@email.com'),
            ('Lambert', 'Nicole', '123 Avenue des Bougies', '0654321098', 'nicole.lambert@email.com')
            
    ]

    query_insert = "INSERT INTO client (nomclient, prenom, adresseclient, phone, email) VALUES (?, ?, ?, ?, ?)"
    query_select = "SELECT * FROM client where idclient=1"

    with connection:
        connection.executemany(query_insert, client_data)
        connection.commit()

    result = execute_query(connection, query_select)
    print("Données dans la table 'clients':")
    print(result)

# Fonction pour insérer des données dans la table 'vehicule'
def insert_vehicule(connection):
    vehicule_data = [
            ('AT-5-EE', 'Renault', 'Velsatis', '4', 5, 'Essence', '2021'),
            ('AA-229-AA', 'Renault', 'Clio', '4', 4, 'Essence', '2019'),
            ('AB-001-AA', 'BMW', 'serie1', '3', 4, 'Essence', '2020'),
            ('xx-775-yy', 'Mercedes', 'A1', '4', 4, 'Essence', '2021'),
            ('ML-998-ZE', 'Mercedes', 'AMG', '4', 4, 'Essence', '2023')
    ]

    query_insert = "INSERT INTO vehicule (immat, constructeur, modele, cylindree, nombreportes, moteur, anneepremmise) VALUES (?, ?, ?, ?, ?, ?, ?)"
    query_select = "SELECT * FROM vehicule where idvehicule=1"

    with connection:
        connection.executemany(query_insert, vehicule_data)
        connection.commit()

    result = execute_query(connection, query_select)
    print("Données dans la table 'vehicule':")
    print(result)

def insert_demandeloc(connection):
    demandeloc_data = [
            ('2024-01-01', '2024-01-05', '12:00', '18:00', 'Paris', 'Marseille', 'Voiture luxe'),
            ('2023-01-01', '2024-01-05', '8:30', '16:00', 'Paris', 'Lyon', 'Voiture classique'),
            ('2023-01-04', '2024-02-05', '8:30', '17:00', 'Paris', 'Grenoble', 'Voiture Entreprise')
    ]    
    
    query_insert = "INSERT INTO demandeloc (datedeprise, datederestitution, heure_debut, heure_fin, lieu_prise, lieu_retour, type ) VALUES (?, ?, ?, ?, ?, ?, ?)"
    query_select = "SELECT * FROM demandeloc where iddemandeloc=1"
    
    with connection:
        connection.executemany(query_insert, demandeloc_data)
        connection.commit()

    result = execute_query(connection, query_select)
    print("Données dans la table 'demande':")
    print(result)

def insert_agent(connection):
    agent_data = [
            ('Aliev', 'Ilham', 'Directeur', 1),
            ('Kohl', 'Eric', 'Technicien', 2),
            ('Jiri', 'Marcel', 'Technicien', 1),
            ('TUKA', 'Stephanie', 'Technicien', 2)
    ]
    
    query_insert = "INSERT INTO agent (nom, prenom, qualification, refdemande) VALUES (?, ?, ?, ?)"
    query_select = "SELECT * FROM agent where idagent=1 "

    with connection:
        connection.executemany(query_insert, agent_data)
        connection.commit()

    result = execute_query(connection, query_select)
    print("Données dans la table 'Agent':")
    print(result)

def insert_agence(connection):
    agence_data = [
           ('BRC-Top', 1, 1),
           ('BRC-Best Top', 2, 2),
           ('BRC-Latest Top', 2, 1)
    ]
    
    query_insert = "INSERT INTO agence (nomagence, refpark, refagent) VALUES (?, ?, ?)"
    query_select = "SELECT * FROM agence where idagence=1"

    with connection:
        connection.executemany(query_insert, agence_data)
        connection.commit()

    result = execute_query(connection, query_select)
    print("Données dans la table 'agence':")
    print(result)

def insert_formulaire(connection):
                                                                                                                                                                        
    formulaire_data = [                                                                                                                                                 

        ('Dupont', 'Emilie', '0687452196', "J'aimerais une voiture pour le week-end"),
                                                                                                                                                                        
        ('Merkel', 'Sarah', '0798452178', "J'aimerais être contacté par téléphone")

    ]


    query_insert = "INSERT INTO formulaire (nom, prenom, phone, message) VALUES (?, ?, ?, ?)"

    query_select = "SELECT * FROM formulaire"

                                                                                                                                                                        
    with connection:

        connection.executemany(query_insert, formulaire_data)

        connection.commit()
                                                                                                                                                                        

    cursor = connection.execute(query_select)

    result = cursor.fetchall()
                                                                                                                                                                        
    print("Données dans la table 'formulaire':")
                                                                                                                                                                        
    for row in result:
        print(row)
 

# Créer une connexion à la base de données
conn = create_connection()

# Insérer des données dans la table 'clients'
insert_client(conn)

# Insérer des données dans la table 'park'
insert_park(conn)

# Insérer des données dans la table 'agence'
insert_agence(conn)

# Insérer des données dans la table 'agent'
insert_agent(conn)

# Insérer des données dans la table 'vehicule'
insert_vehicule(conn)
# Insérer des données dans la table 'demandeloc'
insert_demandeloc(conn)
# Insérer des données dans la table 'agence'
insert_agence(conn)

insert_formulaire(conn)
# Fermer la connexion à la base de données
conn.close()

print("Données insérées avec succès.")
