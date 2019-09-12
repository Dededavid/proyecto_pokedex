import pandas as pd
import requests
from IPython.display import Image

#quiero sacar la primera generación de Pokémon

def listaprigen():
    df = pd.read_csv(('../input/Pokemon.csv'), encoding = 'ISO-8859-1')

    filter1 = df['Generation'] == 1
    df_pk_one = df[filter1]
    return df_pk_one

#eliminando Pokémon Mega
def w_no_mega(df):
    df_mega=df.Name.str.contains("Mega")
    df_clean = df[~df_mega]
    return df_clean


#Pokémon más fuertes en sus campos
def masfuerte(habilidad,df_clean):
    pd.DataFrame(df_clean,columns=['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed'])
    stats = df_clean[habilidad].max()
    return stats

def pokemondestacado(habilidad,df_clean):
    try:
        pokemon = masfuerte(habilidad,df_clean)
        name_dataframe = df_clean[df_clean[habilidad] == pokemon]
    except KeyError:
        print ('Recuerda escribir correctamente la información')
    return name_dataframe


#¿qué pokémon es X número?
def getPokemon(pokeId):
  
    if pokeId <= 151:
        url = "https://pokeapi.co/api/v2/pokemon/{}".format(pokeId)
        response = requests.get(url)
        data = response.json()

        #display(Image(data["sprites"]["front_default"]))
        #display(Image(data["sprites"]["back_default"]))
        print("Este es: ",(data["name"]).upper())

        list_abilities = []
        for i in data['abilities']:
            list_abilities.append(i["ability"]['name'] )
        print ("Habilidad especial:", " & ".join(list_abilities))
            

        list_types= []
        for i in data['types']:
            list_types.append(i['type']['name'])
        print ("Es un Pokémon de tipo: "," & ".join(list_types))
  
    else:
        return("El pokémon que estás buscando no está en nuestra Pokédex de primera generación")
