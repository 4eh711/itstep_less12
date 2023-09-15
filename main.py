from bs4 import BeautifulSoup
import requests
import sqlite3

url = 'https://www.bbc.com/ukrainian/features-66330880'

response  = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    bs = soup.find_all('h2')
    bs = bs[:10]
    for i in bs:
        title=i.text
        print (title)


        connection = sqlite3.connect('final.sl3')
        cur = connection.cursor()
        #cur.execute('DROP TABLE dom_zavd ;')
        #cur.execute('CREATE TABLE dom_zavd (reiting_film TEXT);')
        #cur.execute("INSERT INTO dom_zavd (reiting_film) VALUES (?)", (title,))
        #cur.execute("UPDATE dom_zavd SET reiting_film='Таксі' WHERE rowid = 1;")
        #cur.execute("DELETE FROM dom_zavd WHERE rowid=2;")
        cur.execute("SELECT rowid, reiting_film FROM dom_zavd;")

        res = cur.fetchall()
        print(res)

        connection.commit()
        connection.close()
