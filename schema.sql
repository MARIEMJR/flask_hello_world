CREATE TABLE IF NOT EXISTS park (
	"idpark" 	INTEGER PRIMARY KEY AUTOINCREMENT ,
	"nbreplaces"	INTEGER,
	"nbstockagence"	INTEGER
);

CREATE TABLE IF NOT EXISTS "formulaire" (
	"idformcontact"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"nom"	varchar(100),
	"prenom" varchar(100),
	"phone" varchar(50),
	"message" varchar(100)
);

CREATE TABLE IF NOT EXISTS "vehicule" (
	"idvehicule"	INTEGER,
	"immat"	varchar(20),
	"constructeur"	varchar(100),
	"modele"	varchar(100),
	"cylindree"	varchar(100),
	"nombreportes"	INTEGER,
	"moteur"	varchar(100),
	"anneepremmise"	date,
	PRIMARY KEY("idvehicule" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "client" (
	"idclient"	INTEGER,
	"nomclient"	varchar(100),
	"prenom"	varchar(100),
	"adresseclient"	varchar(250),
	"phone" varchar(15),
	"email" varchar(40),
	
	PRIMARY KEY("idclient" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "demandeloc" (
    "iddemandeloc" INTEGER PRIMARY KEY AUTOINCREMENT,
    "datedeprise" DATE,
    "datederestitution" DATE,
    "heure_debut" TIME,
    "heure_fin" TIME,
    "lieu_prise" VARCHAR(50),
    "lieu_retour" VARCHAR(50),
    "prix" FLOAT,
    "type" VARCHAR(10)
);
CREATE TABLE IF NOT EXISTS "agent" (
	"idagent"	INTEGER,
	"nom"	varchar(100),
	"prenom"	varchar(100),
	"qualification"	varchar(80),
	"refdemande"	INTEGER,
	FOREIGN KEY("refdemande") REFERENCES "demandeloc"("iddemandeloc"),
	PRIMARY KEY("idagent" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "agence" (
    "idagence" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nomagence" VARCHAR(100),
    "refpark" INTEGER,
    "refagent" INTEGER,
    FOREIGN KEY ("refagent") REFERENCES "agent" ("idagent"),
    FOREIGN KEY ("refpark") REFERENCES "park" ("idpark")
);
