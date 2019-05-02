#!/usr/bin/python3
# -*-coding:utf-8 -*
import time

print(time.time()) # Date depuis le temps 0 de l'informatique  le 1er janvier 1970 à 00:00:00 en secondes.
# cela permet de faire des calculs simple de date.
debut = time.time()
print("temps t1: ", debut)
time.sleep(5) # pause de 5 secondes
fin = time.time()
print("temps t2 (aprés 5 secondes): ", fin)
print("Soustraction de Timestamp", fin - debut)

print("utilisation de la méthode localtime: ", time.localtime()) # localtime crée un objet représentant le temps.
"""
tm_year: l'année sous la forme d'un entier ;

tm_mon: le numéro du mois (entre 1 et 12) ;

tm_mday: le numéro du jour du mois (entre 1 et 31, variant d'un mois et d'une année à l'autre) ;

tm_hour: l'heure du jour (entre 0 et 23) ;

tm_min: le nombre de minutes (entre 0 et 59) ;

tm_sec: le nombre de secondes (entre 0 et 61, même si on n'utilisera ici que les valeurs de 0 à 59, c'est bien suffisant) ;

tm_wday: un entier représentant le jour de la semaine (entre 0 et 6, 0 correspond par défaut au lundi) ;

tm_yday: le jour de l'année, entre 1 et 366 ;

tm_isdst: un entier représentant le changement d'heure local."""

# par défaut, sans arguments on part de time.time(), en arguments on peut entrer des secondes.
print("Utilisation de localtime à l'instant t: ", time.localtime(time.time()))

# cette structure d'objet permet de récupérer le timestamp voulu. On utilise time.mktime
temps = time.time() # obtenir le timestamp courant
print("À nouveau le timestamp courant: ", temps)
ts_temps = time.localtime(temps) # le transposer en une structure de temps interprétable
print("Utilisation de localtime sur le timestamp: ", ts_temps)
print("Utilisation de mktime pour revenir au timestamp: ", time.mktime(ts_temps)) # à l'inverse on le transpose en TimeStamp

# Mettre le temps en pause
input("temps de pause de 3,5 sec. Appuyez sur une «entrée».")
time.sleep(3.5)
print("Temps écoulé…")

# Formater un temps
# Si la valeur en seconde du temps n'est pas précisée alors la fonction prend le localtime.
"""
%A: Nom du jour de la semaine

%B: Nom du mois

%d: Jour du mois (de 01 à 31)

%H: Heure (de 00 à 23)

%M: Minute (entre 00 et 59)

%S: Seconde (de 00 à 59)

%Y: Année"""
print("Afficher l'année en cours: {}".format(time.strftime('%Y')))
print("date courante: {}".format(time.strftime("%A %d %B %Y %H:%M:%S")))

# La fonction time est trés complète: https://docs.python.org/fr/3/library/time.html

# ##### DATE ############
# Le module datetime permet de travailler les dates via un objet

import datetime
date = datetime.date(2012, 12, 25) # datetime.date(2012, 12, 25)
print("Affichage de la date en utilisant datetime.date: ", date) # 2012-12-25

aujourhui = datetime.date.today()
print("Afficher juste la date courante en utilisant la méthode today(): ", aujourhui)
print("Autre façon en partant du timestamp pour arriver au même résultat: ", datetime.date.fromtimestamp(time.time())) # équivalent à date.today

# déterminer une date à partir d'une date de référence: timedelta
today = datetime.date.today() # datetime.date(2019, 4, 30)
print("Aujourd'hui: {}".format(today)) # Aujourd'hui: 2019-04-30 (print sur cet objet applique ce format)
yesterday = today - datetime.timedelta(1) # par défaut jour.
print("Hier: {}".format(yesterday))
# dans l'argument de timedelta on peut préciser timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# tous les paramètres sont optionnels.

# exemple d'utilistation de timedelta 
# Seuls les jours, les secondes et les microsecondes sont stockés en interne.
minutes = datetime.timedelta(minutes= 15) # datetime.timedelta(0, 900)
print("utilisation de timedelta de datetime:")
print("15 minutes c'est : ", minutes)
heure = minutes * 4 # datetime.timedelta(0, 3600)
print("En multipliant par 4 on doit obtenir 1 heure: ", heure) #  1:00:00

#### HEURES ######
maintenant = datetime.datetime.now()
print("maintenant il est : ", maintenant)
creer_time = datetime.datetime(1973, 10, 28, 23, 0, 12, 359000)
print("Génération d'un objet datetime: ", creer_time)

# Formater une date str F time
maintenant_france = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')
print("À la française: ", maintenant_france)

# Parser une date str P time
une_date = datetime.datetime.strptime('02/05/2019 19:33:02.267798', '%d/%m/%Y %H:%M:%S.%f')
print("Parser une date du type 02/05/2019 19:33:02.267798 donne: ", une_date)

