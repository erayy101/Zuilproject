import csv
import random
from datetime import datetime
import time

print('Welcome bij station zuil.')
#  het invoeren van tijd en datum
tijd = time.strftime('%H:%M')
print(tijd)
datum = time.strftime('%m-%d-%Y')
print(datum)

# naam van de persoon die review zet of anoniem
naam = input('wat is ur naam?:') or ('anoniem')
print(f'uw naam is: {naam}')

# kiest een random station uit
station = random.choice(['Amsterdam', 'Arnhem', 'Utrecht','Denhaag'])
print(f'station:' + station)

# hier kan je review invoeren, max 140 karakters,
review = input('\n''voer uw review in, maximaal 140 karakters:')
if len(review) > 140:
    print('uw review is te lang, probeer opnieuw.')
    print('voer uw review in, maximaal 140 karakters:')
    exit()
else:
    print('\n' f' uw naam: {naam}, uw review: {review} ')
    print('bedankt voor uw review, tot de volgende keer maar weer.')


# het totale bestand naam station review tijd en datum in CSV bestand
alles = (f'{naam},{station},{review},{tijd},{datum}\n')
infile = open('Zuil1.csv','a')
infile.write(alles)


