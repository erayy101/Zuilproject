DROP TABLE IF EXISTS moderator;
DROP TABLE IF EXISTS bericht;

CREATE TABLE Moderator (
  id_mod            SERIAL NOT NULL, 
  "naam_moderator"  varchar(255) NOT NULL, 
  "email_moderator" varchar(255) NOT NULL, 
  datum             date NOT NULL, 
  PRIMARY KEY (ID_MOD));
CREATE TABLE bericht (
  id_bericht      SERIAL NOT NULL, 
  "naam_klant"    varchar(255), 
  datum           date NOT NULL, 
  tijd            time NOT NULL, 
  review          varchar(255) NOT NULL, 
  station         varchar(255) NOT NULL, 
  moderatorid_mod int4 NOT NULL, 
  PRIMARY KEY (ID_bericht));
  
CREATE TABLE station_service (
     station_city VARCHAR (50) PRIMARY KEY NOT NULL,
     country VARCHAR (2) NOT NULL,
     ov_bike BOOLEAN NOT NULL,
     elevator BOOLEAN NOT NULL,
     toilet BOOLEAN NOT NULL,
     park_and_ride BOOLEAN NOT NULL);
	 
INSERT INTO station_service (
    station_city, country, ov_bike, elevator, toilet, park_and_ride)
	
VALUES
    ('Arnhem', 'NL', true, false, true, false),
	('Amsterdam', 'NL', false, true, false, true),
	('Den Haag', 'NL', true, false, true, false),
	('Utrecht', 'NL', true, false, true, false);

