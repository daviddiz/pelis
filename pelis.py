#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
#note that we have to import the Psycopg2 extras library!
import psycopg2.extras
import psycopg2.extensions
import glob
import os
import csv

csv.register_dialect('nuevo_dialecto', delimiter=',')
pelis_path = '/media/10D8-132E/Peliculas'

csv_pelis = open('pelis.csv', 'wb')
writer_pelis = csv.writer(csv_pelis, dialect='nuevo_dialecto')

cont=0
types = ('*.avi', '*.mpg')
dir = os.listdir(pelis_path)
for director in dir:
	director_path = os.path.join(pelis_path, director)
	os.chdir(director_path)
	
	files_grabbed = []
	for files in types:
		files_grabbed.extend(glob.glob(files))
	
	for peli in files_grabbed:
		row = []
		cont+=1
		row.append(cont)
		row.append(director)
		row.append(peli)
		writer_pelis.writerow(row)

# host1= 'localhost'
# port1=5432
# dbname1 = 'pelis'
# username1 = 'openerp'
# pwd1 = 'VTR_5893'
# 
# connector = psycopg2.connect('host=%s port=%s dbname=%s user=%s password=%s'%(host1,port1,dbname1,username1,pwd1))
# cursor = connector.cursor()

#d1 = cursor.execute("""DROP TABLE directores;""")
#connector.commit()

#d2 = cursor.execute("""DROP TABLE peliculas;""")
#connector.commit()

# d3 = cursor.execute("""CREATE TABLE directores
#  			(
#  			  id serial NOT NULL,
#  			  nombre character varying(75) NOT NULL,
#  			  CONSTRAINT directores_pkey PRIMARY KEY (id),
#  			  CONSTRAINT directores_nombre_uniq UNIQUE (nombre)
#  			)
#  			WITH (
#  			  OIDS=FALSE
#  			);
#  			ALTER TABLE directores OWNER TO openerp;""")
# connector.commit()
# 
# d4 = cursor.execute("""CREATE TABLE peliculas
#  			(
#  			  id serial NOT NULL,
#  			  nombre character varying(100) NOT NULL,
#  			  director_id integer,
#  			  CONSTRAINT peliculas_director_id_fkey FOREIGN KEY (director_id)
#  			      REFERENCES directores (id) MATCH SIMPLE
#  			      ON UPDATE NO ACTION ON DELETE SET NULL,
#  			  CONSTRAINT peliculas_pkey PRIMARY KEY (id)
#  			)
#  			WITH (
#  			  OIDS=FALSE
#  			);
#  			ALTER TABLE peliculas OWNER TO openerp;""")
# connector.commit()


# 	cursor.execute("""INSERT INTO peliculas (nombre) VALUES (%s);""",(peli,))
# 	nueva_peli = cursor.fetchone()
# 	connector.commit()

#import os
#ficheros = os.listdir('../Peliculas/aaa sin ver')
#print ficheros
