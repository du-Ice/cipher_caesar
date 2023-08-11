#!/usr/bin/env python

import string

# Definindo o alfabeto
alfabeto = string.ascii_lowercase

# Imprimindo um cabeçalho decorativo
print('\n========================================================\n\
================CIPHER CAESAR by du_Ice=================\n\
========================================================\n')
# Loop principal
while True:
    
    # Loop principal que permite ao usuário escolher a operação
    try:
        # Solicitando ao usuário que escolha entre criptografar, descriptografar ou sair
        choice = input('[E]ncrypt [D]ecrypt [Q]uit: ').lower()

        # Se o usuário escolher 'E' (criptografar)
        if 'e' == choice:
            # Solicitando o texto a ser codificado
            enc = input('\nDigite para codificar: ').lower()
        
            # Solicitando o deslocamento desejado
            shift = int(input('Qual o deslocamento desejado? '))
        
            # Definindo a função para codificar usando a Cifra de César
            def cod_cesar():
                unicoded = []
                for c in enc:
                    unicoded.append(ord(c))
                    res = []
                for i in unicoded:
                    indice = int((i+shift)-97)
                    if indice <= 25:
                        res.append(alfabeto[indice])
                    else:
                        res.append(alfabeto[(indice)-len(alfabeto)])
                return ''.join(res)

            # Imprimindo o resultado da codificação
            print(f'\nencrypt: {cod_cesar()}\n')
                
        # Se o usuário escolher 'D' (descriptografar)
        elif 'd' == choice:
            # Solicitando o texto a ser decodificado
            dec = input('\nDigite para decodificar: ').lower()

            # Solicitando o deslocamento desejado
            shift = int(input('Qual o deslocamento desejado? '))
        
            # Definindo a função para decodificar usando a Cifra de César
            def decod_cesar():
                unicoded = []
                for c in dec:
                    unicoded.append(ord(c))
                    res = []
                for i in unicoded:
                    indice = int((i-shift)-97)
                    if indice <= 25:
                        res.append(alfabeto[indice])
                    else:
                        res.append(alfabeto[(indice)-len(alfabeto)])
                return ''.join(res)

            # Imprimindo o resultado da decodificação
            print(f'\ndecrypt: {decod_cesar()}\n')
            
        
        # Se o usuário escolher 'Q' (sair)
        elif 'q' == choice:
            print('\n===========================\n\
Obrigado e até a próxima...\n\
===========================\n')
            break
        
        # Se o usuário inserir uma opção inválida
        else:
            print('\n=======================================\n\
Fora do padrão, escolha uma das opções!\n\
=======================================\n')

    except ValueError:
        print('\nValores não permitido\n')
    except UnboundLocalError:
        print('\nPreencha todos os campos\n')
    except IndexError:
        print('\nDeslocamento fora do alcance escolha no maximo 30\n')
