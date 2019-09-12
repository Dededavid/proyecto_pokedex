#Sacando la primera generación de Pokémon 

from funciones import listaprigen, w_no_mega, pokemondestacado, getPokemon



def main():
    df_clean = w_no_mega(listaprigen())
    #Obteniendo el pokémon más destacado de su campo
    habilidad = input('''
        Inserta el campo en el que desees conocer al pokemón más destacado: 
        Recuerda que éstos son los valores que puedes consultar: 
        HP     Attack      Defense     Sp. Atk     Sp. Def     Speed
        ''')
    print(pokemondestacado(habilidad,df_clean))

    #Obteniendo los datos del pokémon según su número
    npokemon = input('''

    Ahora introduce el número del Pokémon que desees consultar para extraer su información exclusiva:

    ''')
    print(getPokemon(int(npokemon)))


if __name__ == '__main__': 
    main()