import psycopg2

# Connect aan datamodel
conn = psycopg2.connect(
    host="localhost",
    database="CorrectZuilproject",
    user="postgres",
    password="123123")

# invoeren van naam en email Moderator
print('Hallo Moderator,')
naam = input('wat is uw naam?:')
email = input('wat is uw email?:')

# opent de CSV bestand en leest het
with open('Zuil1.csv', "r") as file:
    data = file.readlines()

# moderator kan het bericht goed of afkeuren.
for a in data:
    print(a)
    moderator = input('goed (y) slecht (n):')
    # als het is goedgekeurd, dan haalt hij de informatie uit de csv bestand.
    if moderator == 'y':
        print('het bericht is goedgekeurd.')

        b = a.split(',')
        naam = b[0]
        station = b[1]
        review = b[2]
        datum = b[4]
        tijd = b[3]
        moderatorid_mod = 1111
        naam_moderator = naam
        email_moderator = email
        #  word doorgevoerd naar de data base.
        cursor = conn.cursor()
        qr1 = 'Insert INTO bericht (naam_klant, station, review, datum, tijd, moderatorid_mod) VALUES (%s,%s,%s,%s,%s,%s)'
        data1 = [naam, station, review, datum, tijd, moderatorid_mod]
        cursor.execute(qr1,data1)
        qr2 = "Insert INTO moderator(naam_moderator, email_moderator, datum) VALUES (%s, %s, %s)"
        data2 = [naam_moderator, email_moderator, datum]
        cursor.execute(qr2, data2)
        conn.commit()


    else:
        print("Het bericht is afgekeurd.")

print('Er zijn geen berichten meer.')
f = open('Zuil1.csv',"w")
f.close()






