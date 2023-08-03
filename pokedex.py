import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

fenetre = tk.Tk()
fenetre.title("Pokedex v0.1")
fenetre.geometry("1140x600")
fenetre.config(bg="red")
fenetre.rowconfigure([i for i in range(4)], minsize=50, weight=1)
fenetre.columnconfigure([i for i in range(3)], minsize=50, weight=1)

# Pokemon name

pokemon_name_frame = tk.Frame(fenetre, bg="red", borderwidth=5, relief="sunken")
pokemon_name_frame.grid(row=0, column=0)
pokemon_name = tk.Label(pokemon_name_frame, text="Nom du Pokemon", bg="white", background="#330000", fg="#ffcccc", font="Garamond 20 bold")
pokemon_name.pack()

# pokemon image and types

pokemon_image_frame = tk.Frame(fenetre, bg="red", borderwidth=4, relief="sunken")
pokemon_image_frame.grid(row=1, column=0)

pokemon_types_frame = tk.Label(pokemon_image_frame, text="Type du pokemon", bg="red", borderwidth=5, relief="sunken")
pokemon_types_frame.grid(row=0, column=1)
pokemon_number = tk.Label(pokemon_image_frame, text="Nombre du pokémon", bg="white", fg="#ffcccc", font="Garamond 12 bold")
pokemon_number.grid(row=1, column=1)
pokemon_stats_title = tk.Label(pokemon_image_frame, text="Stats :", bg="white", fg="#ffcccc", font="Garamond 12 bold")
pokemon_stats_title.grid(row=2, column=1)

# pokemon stats

pokemon_stats_frame = tk.Frame(fenetre, bg="red", borderwidth=3)
pokemon_stats_frame.grid(row=2, column=0)

pokemon_stats_hp = tk.Label(pokemon_stats_frame, text="HP: 110", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_hp.grid(row=0, column=0)

pokemon_stats_attack = tk.Label(pokemon_stats_frame, text="Attack: 52", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_attack.grid(row=1, column=0)

pokemon_stats_defense = tk.Label(pokemon_stats_frame, text="Defense: 52", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_defense.grid(row=2, column=0)

pokemon_stats_spattack = tk.Label(pokemon_stats_frame, text="Sp. Attack: 52", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_spattack.grid(row=3, column=0)

pokemon_stats_spdefense = tk.Label(pokemon_stats_frame, text="Sp. Defense: 85", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_spdefense.grid(row=4, column=0)

pokemon_stats_speed = tk.Label(pokemon_stats_frame, text="Speed: 52", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_speed.grid(row=5, column=0)

pokemon_stats_total = tk.Label(pokemon_stats_frame, text="Total: 1150", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12 bold")
pokemon_stats_total.grid(row=6, column=0)

# Configuration des boutons

bouton_frame = tk.Frame(fenetre, bg="white", borderwidth=5, relief="raised")
bouton_frame.grid(row=3, column=0)

# Search frame

search_frame = tk.Frame(fenetre, bg="red", borderwidth=5, relief="raised")
search_frame.grid(row=0, column=1, rowspan=3)

search_label = tk.Label(search_frame, text="Search a Pokemon", bg="white", font = ("Garamond 14 bold"))
search_label.grid(row=0, column=0, columnspan=2)

#Efface l'insert en cliquant dans le champ de saisie
def temp_text(e):
    search_label1.delete(0, "end")
    search_label2.delete(0, "end")

search_label1 = tk.Entry(search_frame, text="Search by name", bg="white")
search_label1.insert(0, "Search by name")
search_label1.grid(row=1, column=0)

search_label2 = tk.Entry(search_frame, text="Search by number", bg="white")
search_label2.insert(0, "Search by number")
search_label2.grid(row=2, column=0)

search_label1.bind("<FocusIn>", temp_text)
search_label2.bind("<FocusIn>", temp_text)


# Add pokemon frame

add_frame = tk.Frame(fenetre, bg="#e60000", borderwidth=4, relief="sunken")
add_frame.grid(row=1, column=2)

add_label = tk.Label(add_frame, text="Add a Pokemon", bg="white", font = ("Garamond 14 bold"))
add_label.grid(row=0, column=0, columnspan=2)

add_label_name = tk.Entry(add_frame, text="Enter the name", bg="white", fg="black")
add_label_name.grid(row=1, column=0)
add_label_name1 = tk.Label(add_frame, text="Enter the name", bg="white", fg="black")
add_label_name1.grid(row=1, column=1)

add_label_number = tk.Entry(add_frame, text="Enter the number", bg="white", fg="black")
add_label_number.grid(row=2, column=0)
add_label_number1 = tk.Label(add_frame, text="Enter the number", bg="white", fg="black")
add_label_number1.grid(row=2, column=1)

add_label_type = tk.Entry(add_frame, text="Enter the type", bg="white", fg="black")
add_label_type.grid(row=3, column=0)
add_label_type1 = tk.Label(add_frame, text="Enter the type", bg="white", fg="black")
add_label_type1.grid(row=3, column=1)

add_label_hp = tk.Entry(add_frame, text="Enter the HP", bg="white", fg="black")
add_label_hp.grid(row=4, column=0)
add_label_hp1 = tk.Label(add_frame, text="Enter the HP", bg="white", fg="black")
add_label_hp1.grid(row=4, column=1)

add_label_attack = tk.Entry(add_frame, text="Enter the Attack", bg="white", fg="black")
add_label_attack.grid(row=5, column=0)
add_label_attack1 = tk.Label(add_frame, text="Enter the attack", bg="white", fg="black")
add_label_attack1.grid(row=5, column=1)

add_label_defense = tk.Entry(add_frame, text="Enter the Defense", bg="white", fg="black")
add_label_defense.grid(row=6, column=0)
add_label_defense1 = tk.Label(add_frame, text="Enter the defense", bg="white", fg="black")
add_label_defense1.grid(row=6, column=1)

add_label_spattack = tk.Entry(add_frame, text="Enter the Sp. Attack", bg="white", fg="black")
add_label_spattack.grid(row=7, column=0)
add_label_spattack1 = tk.Label(add_frame, text="Enter the special attack", bg="white", fg="black")
add_label_spattack1.grid(row=7, column=1)

add_label_spdefense = tk.Entry(add_frame, text="Enter the Sp. Defense", bg="white", fg="black")
add_label_spdefense.grid(row=8, column=0)
add_label_spdefense1 = tk.Label(add_frame, text="Enter the sp. defense", bg="white", fg="black")
add_label_spdefense1.grid(row=8, column=1)

add_label_speed = tk.Entry(add_frame, text="Enter the Speed", bg="white", fg="black")
add_label_speed.grid(row=9, column=0)
add_label_speed1 = tk.Label(add_frame, text="Enter the speed", bg="white", fg="black")
add_label_speed1.grid(row=9, column=1)

add_label_total = tk.Entry(add_frame, text="Enter the Total", bg="white", fg="black")
add_label_total.grid(row=10, column=0)
add_label_total1 = tk.Label(add_frame, text="Enter the total", bg="white", fg="black")
add_label_total1.grid(row=10, column=1)

pokedex = [
    {
        "Name": "bulbasaur",
        "Stats": {'HP': 45, 'Attack': 49, 'Defense': 49, 'Sp. Attack': 65, 'Sp. Defense': 65, 'Speed': 45, 'Total': 318},
        "Type": ['Grass', 'Poison'],
        "National Number": '0001',
        "Image": ['Images/bulbizar.png', '#49B0D0']
    },
    {
        "Name": "pikachu",
        "Stats": {'HP': 35, 'Attack': 55, 'Defense': 40, 'Sp. Attack': 50, 'Sp. Defense': 50, 'Speed': 90, 'Total': 320},
        "Type": ['Electric'],
        "National Number": '0025',
        "Image": ['Images/pikachu.png', '#FFF135']
    },
    {
        "Name": "charmander",
        "Stats": {'HP': 39, 'Attack': 52, 'Defense': 43, 'Sp. Attack': 60, 'Sp. Defense': 50, 'Speed': 65, 'Total': 309},
        "Type": ['Fire'],
        "National Number": '0004',
        "Image": ['Images/salameche.png', '#ED8A8B']
    },
    {
        "Name": "psyduck",
        "Stats": {'HP': 50, 'Attack': 52, 'Defense': 48, 'Sp. Attack': 65, 'Sp. Defense': 50, 'Speed': 55, 'Total': 320},
        "Type": ['Water'],
        "National Number": '0054',
        "Image": ['Images/psykokwak.png', '#A9A9A9']
    },
    {
        "Name": "jigglypuff",
        "Stats": {'HP': 115, 'Attack': 45, 'Defense': 20, 'Sp. Attack': 45, 'Sp. Defense': 25, 'Speed': 20, 'Total': 270},
        "Type": ['Normal', 'Fairy'],
        "National Number": '0039',
        "Image": ['Images/Rondoudou.png', '#E6E6FA']
    },
    {
        "Name": "meowth",
        "Stats": {'HP': 40, 'Attack': 45, 'Defense': 35, 'Sp. Attack': 40, 'Sp. Defense': 40, 'Speed': 90, 'Total': 290},
        "Type": ['Normal'],
        "National Number": '0052',
        "Image": ['Images/miaouss.png', '#E6E6E6']
    },
    {
        "Name": "snorlax",
        "Stats": {'HP': 160, 'Attack': 110, 'Defense': 65, 'Sp. Attack': 65, 'Sp. Defense': 110, 'Speed': 30, 'Total': 540},
        "Type": ['Normal'],
        "National Number": '0143',
        "Image": ['Images/ronflex.png', '#E6E6E6']
    }
]
# Initialisation des variables de recherche globales
name_to_search = ""
number_to_search = ""

# texte des widgets entry
name_to_search = add_label_name.get().lower()
number_to_search = add_label_number.get().lower()

def afficher_pokemon(i, move = None):
    print(i)
    global pokemon_image
    # , name_to_search, number_to_search

    # if name_to_search:
    #     for index, pokemon in enumerate(pokedex):
    #         if pokemon["Name"].lower() == name_to_search:
    #             i = index
    #             break
    
    # if number_to_search:
    #     for index, pokemon in enumerate(pokedex):
    #         if pokemon["National Number"] == number_to_search:
    #             i = index
    #             break
    # else:
    #     i = 0

    # if move == 'forward':
    #     i = (i + 1) % len(pokedex)
    # elif move == 'backward':
    #     i = (i - 1) % len(pokedex)

    pokemon_image_frame['bg'] = pokedex[i]['Image'][1]
    pokemon_name.config(text=pokedex[i]["Name"])
    pokemon_number.config(text=pokedex[i]["National Number"])
    pokemon_types_frame.config(text=', '.join(pokedex[i]["Type"]))
    pokemon_stats_frame['bg'] = pokedex[i]['Image'][1]

    #Open image file

    image = pokedex[i]['Image'][0]
    pokemon_image = Image.open(image)
    pokemon_image = pokemon_image.resize((150, 150))
    pokemon_image = ImageTk.PhotoImage(pokemon_image)

    #afficher qu'une seule image à la fois :
    # for widget in pokemon_image_frame.winfo_children():
    #     widget.destroy()

    pokemon_image_label = tk.Label(pokemon_image_frame, image=pokemon_image, bg="white")
    pokemon_image_label.image = pokemon_image
    pokemon_image_label.grid(row=0, column=0)

    #loading stats

    pokemon_stats_hp['text'] = pokedex[i]['Stats']['HP']
    pokemon_stats_attack['text'] = pokedex[i]['Stats']['Attack']
    pokemon_stats_defense['text'] = pokedex[i]['Stats']['Defense']
    pokemon_stats_spattack['text'] = pokedex[i]['Stats']['Sp. Attack']
    pokemon_stats_spdefense['text'] = pokedex[i]['Stats']['Sp. Defense']
    pokemon_stats_speed['text'] = pokedex[i]['Stats']['Speed']
    pokemon_stats_total['text'] = pokedex[i]['Stats']['Total']

    # récupération de la liste des pokemons
    pokelist = [value for value in pokedex[0].items()]

    if move == 'forward':
        try:
            i = pokedex[i + 1]["Name"] if i + 1 < len(pokedex) else pokedex[0]["Name"]
            afficher_pokemon(i)
        except IndexError:
            i = pokelist[0] #si erreur c'est que retour à 0
    elif move == 'backward':
        try:
            i = pokedex[i - 1]["Name"] if i - 1 >= 0 else pokedex[len(pokedex) - 1]["Name"]
            afficher_pokemon(i)
        except IndexError:
            i = pokelist[len(pokedex) - 1] #si erreur c'est que retour à celui d'avant

    left_bouton = tk.Button(bouton_frame, text="Back", command=lambda:afficher_pokemon(i, move = 'backward'), font = ("Garamond 16"))
    left_bouton.grid(row=0, column=0)

    right_bouton = tk.Button(bouton_frame, text="Next", command=lambda:afficher_pokemon(i, move = 'forward'), font = ("Garamond 16"))
    right_bouton.grid(row=0, column=1)

def search_by_name():
    global name_to_search
    name_to_search = search_label1.get().lower()
    # name_to_search = name  
    
    for i, pokemon in enumerate(pokedex):
        if pokemon["Name"].lower() == name_to_search:
            afficher_pokemon(i)
            return
        
    messagebox.showinfo("Error", "The pokemon is not in the list! Add the pokemon to the list!")

    
def search_by_number():
    global number_to_search
    number_to_search = search_label2.get()
    # number_to_search = number

    for i, pokemon in enumerate(pokedex):
        if pokemon["National Number"] == number_to_search:
            afficher_pokemon(i)
            return
    messagebox.showinfo("Error", "The pokemon is not in the list! Add the pokemon to the list!")

recherche_bouton1 = tk.Button(search_frame, text = "Search by name", font = ("Helvetica 12"), command=search_by_name)
recherche_bouton1.grid(row=1, column=1)

recherche_bouton2 = tk.Button(search_frame, text = "Search by number", font=("Helvetica 12"), command=search_by_number)
recherche_bouton2.grid(row=2, column=1)

def add_pokemon():
    global pokedex
    new_pokemon = {
        "Name": add_label_name.get(),
        "Stats": {
            'HP': int(add_label_hp.get()),
            'Attack': int(add_label_attack.get()),
            'Defense': int(add_label_defense.get()),
            'Sp. Attack': int(add_label_spattack.get()),
            'Sp. Defense': int(add_label_spdefense.get()),
            'Speed': int(add_label_speed.get()),
            'Total': int(add_label_total.get())
        },
        "Type": [add_label_type.get()],
        "National Number": add_label_number.get(),
        "Image": ['Images/placeholder.png', '#FFFFFF']
    }

    # add a new pokemon
    pokedex.append(new_pokemon)
    messagebox.showinfo("Success", "The pokemon has been added!")

    add_label_name.delete(0, "end")
    add_label_number.delete(0, "end")
    add_label_type.delete(0, "end")
    add_label_hp.delete(0, "end")
    add_label_attack.delete(0, "end")
    add_label_defense.delete(0, "end")
    add_label_spattack.delete(0, "end")
    add_label_spdefense.delete(0, "end")
    add_label_speed.delete(0, "end")
    add_label_total.delete(0, "end")

add_bouton = tk.Button(add_frame, text = "Add the pokemon", font = ("Garamond 12"), command=add_pokemon)
add_bouton.grid(row=11, column=0, columnspan=2)

afficher_pokemon(len(pokedex) - 1)
fenetre.mainloop()