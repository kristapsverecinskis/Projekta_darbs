import sqlite3
from cryptography.fernet import Fernet

KEY_FILE = 'parole.key'

with open(KEY_FILE, 'rb') as atsl_fails:
    atslega = atsl_fails.read()

atshifrejums = Fernet(atslega)

con = sqlite3.connect('paroles.db')
c = con.cursor()

con.commit()

def shifret_paroli(parole, atshifrejums):
    shifreta_par = atshifrejums.encrypt(parole.encode())
    return shifreta_par

def atshifret(shifreta_parole, atshifrejums):
    atshifreta_par = atshifrejums.decrypt(shifreta_parole).decode()
    return atshifreta_par

def pievienot():
    majaslapa = input("Majaslapa: ")
    lietotajvards = input("Lietotajvards: ")
    parole = input("Parole: ")
    shifreta_parole = shifret_paroli(parole, atshifrejums)

    c.execute('''
        INSERT INTO user_data (Majaslapa, Lietotajvards, Shifreta_parole)
        VALUES (?, ?, ?)
    ''', (majaslapa, lietotajvards, shifreta_parole))

    con.commit()

def paradit():
    majaslapa = input("Majaslapas nosaukums: ")

    c.execute('''
        SELECT Lietotajvards, Shifreta_parole
        FROM user_data
        WHERE Majaslapa = ?
    ''', (majaslapa,))

    row = c.fetchone()

    if row:
        lietotajvards, shifreta_parole = row
        print(f"Lietotajvards: {lietotajvards}")
        atshifreta_parole = atshifret(shifreta_parole, atshifrejums)
        print(f"Parole: {atshifreta_parole}")
    else:
        quit()

def main():
    izv = input("1. jauns ieraksts\n2. paradit lietotajvardu ar paroli\n")
    if izv == '1':
        pievienot()
    elif izv == '2':
        paradit()
    else:
        quit()

if __name__ == "__main__":
    main()
