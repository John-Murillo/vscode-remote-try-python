#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import subprocess; import sys

# Install the required packages
subprocess.check_call([sys.executable, "-m", "pip", "install", "prettytable"])

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("Vamos a jugar!")

import random
from prettytable import PrettyTable

# Crear la tabla para el puntaje
score_table = PrettyTable()
score_table.field_names = ["Jugador", "Partidas Ganadas", "Partidas Perdidas"]

# Inicializar puntajes
score_jugador1 = {"ganadas": 0, "perdidas": 0}
score_jugador2 = {"ganadas": 0, "perdidas": 0}

while True:
    print("Jugador 1: 1=Piedra, 2=Papel, 3=Tijera")
    a = int(input("Ingrese la opción: "))
    print(f"Jugador 1 eligió: {a}")

    # Elección aleatoria para el Jugador 2 (computadora)
    b = random.randint(1, 3)
    print(f"Jugador 2 (Computadora) eligió: {b}")

    if a == b:
        print("Empate")
    elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        print("Gana Jugador 1")
        score_jugador1["ganadas"] += 1
        score_jugador2["perdidas"] += 1
    else:
        print("Gana Jugador 2 (Computadora)")
        score_jugador1["perdidas"] += 1
        score_jugador2["ganadas"] += 1

    # Imprimir la tabla del puntaje
    score_table.add_row(["Jugador 1", score_jugador1["ganadas"], score_jugador1["perdidas"]])
    score_table.add_row(["Jugador 2", score_jugador2["ganadas"], score_jugador2["perdidas"]])
    print(score_table)

    print("¿Desea jugar de nuevo?")
    print("1. Si")
    print("2. No")
    c = int(input("Opción: "))

    if c == 1:
        print("Juguemos de nuevo")
    elif c == 2:
        print("Gracias por jugar")
        break
    else:
        print("Opción no válida")
        break
