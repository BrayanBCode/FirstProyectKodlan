meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "TOP DIF": "Diferencia de toplaner (League of leguens)"
}


loop = True

while loop:
    print("Ingrese una palabra que no conozcas - X para salir")

    word = input().upper()

    if word == "X":
        print("Diccioanrio cerrado")
        break

    if word in meme_dict.keys():
        print(word, ":", meme_dict[word])
    else:
        print("no esta en el diccionario")
    
    