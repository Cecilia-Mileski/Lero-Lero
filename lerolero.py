#!/usr/bin/python3
"""Gerador de lero-lero.

Gera frases de efeito sem significado real."""

import random

parte1 = ["oi"]
parte2 = ["olá"]
parte3 = ["hello"]

lingua = int(input("Escolha a língua: 1- português, 2- ingles\n"))

if lingua == 2:
    parte1 = []
    parte2 = []
    parte3 = []

print (random.choice(parte1), random.choice(parte2), random.choice(parte3))
