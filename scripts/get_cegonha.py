#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

# Faz a chamada da API e mostra a resposta
r = requests.get('http://cegonha.locaweb.com.br/machines/')
print ("Status code", r.status_code)

# Armazena a resposta da API em uma variável
response_dict = r.json()

# Processa o resultado
print (response_dict.keys())
