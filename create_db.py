import sqlite3
from pathlib import Path

def create_db():
    db_path = Path("database.db")
    schema_path = Path("schema.sql")

    # Vérifier si la base de données existe déjà
    if db_path.exists():
        print("La base de données existe déjà.")
        return

    # Lire le schéma SQL depuis le fichier
    with schema_path.open(mode="r") as schema_file:
        schema = schema_file.read()

    # Se connecter à la base de données et exécuter le schéma
    try:
        conn = sqlite3.connect(str(db_path))  # Utiliser str(db_path) pour obtenir la chaîne du chemin d'accès
        cursor = conn.cursor()
        cursor.executescript(schema)
        conn.commit()
        print("Base de données créée avec succès.")
    except sqlite3.Error as e:
        print(f"Erreur lors de la création de la base de données : {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_db() 
