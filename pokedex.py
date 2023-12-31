import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from playsound import playsound
import threading

fenetre = tk.Tk()
fenetre.title("Pokedex v0.1")
fenetre.geometry("1140x600")
fenetre.config(bg="red")
fenetre.rowconfigure([i for i in range(4)], minsize=50, weight=1)
fenetre.columnconfigure([i for i in range(3)], minsize=50, weight=1)

# music settings

# def play_music():
#     playsound('Son/pokemontheme.mp3', False)
    
# def play_music():
#     while fenetre.mainloop() is True:
#         playsound('Son/pokemontheme.mp3', False)
#         threading.Thread(target=playsound, args=("Son/pokemontheme.mp3",)).start()
#     else:
#         playsound('Son/pokemontheme.mp3', False)
#         threading.Thread(target=playsound, args=("Son/pokemontheme.mp3",)).daemon()

# Pokemon name

pokemon_name_frame = tk.Frame(fenetre, bg="red", borderwidth=5, relief="raised")
pokemon_name_frame.grid(row=0, column=0)
pokemon_name = tk.Label(pokemon_name_frame, text="Nom du Pokemon", bg="white", background="#330000", fg="#ffcccc", font="Garamond 25 bold")
pokemon_name.pack()

# pokemon image and types

pokemon_image_frame = tk.Frame(fenetre, bg="red", borderwidth=4, relief="sunken")
pokemon_image_frame.grid(row=1, column=0)

pokemon_types_frame = tk.Label(pokemon_image_frame, text="Type du pokemon", bg="white", background="#330000", fg="#ffcccc", font="Garamond 14 bold", relief="sunken")
pokemon_types_frame.grid(row=0, column=1)
pokemon_number = tk.Label(pokemon_image_frame, text="Nombre du pokémon", bg="#ffcccc", fg="#7a0000", font="Garamond 12 bold")
pokemon_number.grid(row=1, column=1)
pokemon_stats_title = tk.Label(pokemon_image_frame, text="Stats :", bg="#ffcccc", fg="#7a0000", font="Garamond 12 bold")
pokemon_stats_title.grid(row=2, column=0)

# pokemon stats

pokemon_stats_frame = tk.Frame(fenetre, bg="red", borderwidth=3, relief="sunken")
pokemon_stats_frame.grid(row=2)

pokemon_stats_hptitle = tk.Label(pokemon_stats_frame, text="HP :", bg="#ffcccc", fg="#7a0000")
pokemon_stats_hptitle.grid(row=0, column=0)
pokemon_stats_hp = tk.Label(pokemon_stats_frame, text="HP: 110", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_hp.grid(row=0, column=1)

pokemon_stats_atacktitle = tk.Label(pokemon_stats_frame, text="Attack :", bg="#ffcccc", fg="#7a0000")
pokemon_stats_atacktitle.grid(row=1, column=0)
pokemon_stats_attack = tk.Label(pokemon_stats_frame, text="Attack: 52", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_attack.grid(row=1, column=1)

pokemon_stats_defensetitle = tk.Label(pokemon_stats_frame, text="Defense :", bg="#ffcccc", fg="#7a0000")
pokemon_stats_defensetitle.grid(row=2, column=0)
pokemon_stats_defense = tk.Label(pokemon_stats_frame, text="Defense: 52", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_defense.grid(row=2, column=1)

pokemon_stats_spatacktitle = tk.Label(pokemon_stats_frame, text="Sp. Attack :", bg="#ffcccc", fg="#7a0000")
pokemon_stats_spatacktitle.grid(row=3, column=0)
pokemon_stats_spattack = tk.Label(pokemon_stats_frame, text="Sp. Attack: 52", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_spattack.grid(row=3, column=1)

pokemon_stats_spdefensetitle = tk.Label(pokemon_stats_frame, text="Sp. Defense :", bg="#ffcccc", fg="#7a0000")
pokemon_stats_spdefensetitle.grid(row=4, column=0)
pokemon_stats_spdefense = tk.Label(pokemon_stats_frame, text="Sp. Defense: 85", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_spdefense.grid(row=4, column=1)

pokemon_stats_speedtitle = tk.Label(pokemon_stats_frame, text="Speed :", bg="#ffcccc", fg="#7a0000")
pokemon_stats_speedtitle.grid(row=5, column=0)
pokemon_stats_speed = tk.Label(pokemon_stats_frame, text="Speed: 52", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12")
pokemon_stats_speed.grid(row=5, column=1)

pokemon_stats_totaltitle = tk.Label(pokemon_stats_frame, text="Total :", bg="#ffcccc", fg="#7a0000")
pokemon_stats_totaltitle.grid(row=6, column=0)
pokemon_stats_total = tk.Label(pokemon_stats_frame, text="Total: 1150", bg="white", background="#330000", fg="#ffcccc", font="Garamond 12 bold")
pokemon_stats_total.grid(row=6, column=1)

# Configuration des boutons

bouton_frame = tk.Frame(fenetre, bg="red", borderwidth=5, relief="raised")
bouton_frame.grid(row=3, column=0)

def create_buttons(i):
    left_bouton = tk.Button(bouton_frame, text="<- Back", command=lambda:afficher_pokemon(i - 1), font = ("Garamond 16"), relief="raised", bg="#43B14B")
    left_bouton.grid(row=0, column=0)

    right_bouton = tk.Button(bouton_frame, text="Next ->", command=lambda:afficher_pokemon(i + 1), font = ("Garamond 16"), relief="raised", bg="#43B14B")
    right_bouton.grid(row=0, column=1)

# Search frame

search_frame = tk.Frame(fenetre, bg="red", borderwidth=5, relief="raised")
search_frame.grid(row=0, column=1, rowspan=3)

search_label = tk.Label(search_frame, text="Search a Pokemon", bg="white", background="#330000", fg="#ffcccc", font="Garamond 20 bold")
search_label.grid(row=0, column=0, columnspan=2)

#Efface l'insert en cliquant dans le champ de saisie
def temp_text(e):
    search_label1.delete(0, "end") # Suppression du contenu actuel de la zone de saisie de recherche par nom
    search_label2.delete(0, "end") # Suppression du contenu actuel de la zone de saisie de recherche par numéro

search_label1 = tk.Entry(search_frame, text="Search by name", bg="white")
search_label1.insert(0, "Search by name") # Insérer le texte par défaut dans la zone de saisie
search_label1.grid(row=1, column=0) 

search_label2 = tk.Entry(search_frame, text="Search by number", bg="white")
search_label2.insert(0, "Search by number") # Insérer le texte par défaut dans la zone de saisie
search_label2.grid(row=2, column=0)

# Associer la fonction temp_text à l'événement FocusIn (suppression automatique du texte pour l'utilisateur) pour les deux zones de saisie
search_label1.bind("<FocusIn>", temp_text)
search_label2.bind("<FocusIn>", temp_text)


# Add pokemon frame

add_frame = tk.Frame(fenetre, bg="#e60000", borderwidth=4, relief="raised")
add_frame.config(height=1000)
add_frame.grid(row=1, column=2, rowspan=3)

add_label = tk.Label(add_frame, text="Add a Pokemon", bg="white", background="#330000", fg="#ffcccc", font="Garamond 20 bold")
add_label.grid(row=0, column=0, columnspan=2)

add_entry_name = tk.Entry(add_frame, text="Enter the name", bg="white", fg="black")
add_entry_name.grid(row=1, column=0, padx=3, pady=5)
add_label_name = tk.Label(add_frame, text="Enter the name", bg="#ffcccc", fg="#7a0000")
add_label_name.grid(row=1, column=1, pady=5)

add_entry_number = tk.Entry(add_frame, text="Enter the number", bg="white", fg="black")
add_entry_number.grid(row=2, column=0, pady=5)
add_label_number = tk.Label(add_frame, text="Enter the number", bg="#ffcccc", fg="#7a0000")
add_label_number.grid(row=2, column=1, pady=5)

add_entry_type = tk.Entry(add_frame, text="Enter the type", bg="white", fg="black")
add_entry_type.grid(row=3, column=0, pady=5)
add_label_type = tk.Label(add_frame, text="Enter the type", bg="#ffcccc", fg="#7a0000")
add_label_type.grid(row=3, column=1, pady=5)

add_entry_hp = tk.Entry(add_frame, text="Enter the HP", bg="white", fg="black")
add_entry_hp.grid(row=4, column=0, pady=5)
add_label_hp = tk.Label(add_frame, text="Enter the HP", bg="#ffcccc", fg="#7a0000")
add_label_hp.grid(row=4, column=1, pady=5)

add_entry_attack = tk.Entry(add_frame, text="Enter the Attack", bg="white", fg="black")
add_entry_attack.grid(row=5, column=0, pady=5)
add_label_attack = tk.Label(add_frame, text="Enter the attack", bg="#ffcccc", fg="#7a0000")
add_label_attack.grid(row=5, column=1, pady=5)

add_entry_defense = tk.Entry(add_frame, text="Enter the Defense", bg="white", fg="black")
add_entry_defense.grid(row=6, column=0, pady=5)
add_label_defense = tk.Label(add_frame, text="Enter the defense", bg="#ffcccc", fg="#7a0000")
add_label_defense.grid(row=6, column=1, pady=5)

add_entry_spattack = tk.Entry(add_frame, text="Enter the Sp. Attack", bg="white", fg="black")
add_entry_spattack.grid(row=7, column=0, pady=5)
add_label_spattack = tk.Label(add_frame, text="Enter the special attack", bg="#ffcccc", fg="#7a0000")
add_label_spattack.grid(row=7, column=1, pady=5)

add_entry_spdefense = tk.Entry(add_frame, text="Enter the Sp. Defense", bg="white", fg="black")
add_entry_spdefense.grid(row=8, column=0, pady=5)
add_label_spdefense = tk.Label(add_frame, text="Enter the sp. defense", bg="#ffcccc", fg="#7a0000")
add_label_spdefense.grid(row=8, column=1, pady=5)

add_entry_speed = tk.Entry(add_frame, text="Enter the Speed", bg="white", fg="black")
add_entry_speed.grid(row=9, column=0, pady=5)
add_label_speed = tk.Label(add_frame, text="Enter the speed", bg="#ffcccc", fg="#7a0000")
add_label_speed.grid(row=9, column=1, pady=5)

add_entry_total = tk.Entry(add_frame, text="Enter the Total", bg="white", fg="black")
add_entry_total.grid(row=10, column=0, pady=5)
add_label_total = tk.Label(add_frame, text="Enter the total", bg="#ffcccc", fg="#7a0000")
add_label_total.grid(row=10, column=1, pady=5)

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
        "Image": ['Images/psykokwak.png', '#E1A31C']
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
        "Image": ['Images/miaouss.png', '#FEEDBC']
    },
    {
        "Name": "snorlax",
        "Stats": {'HP': 160, 'Attack': 110, 'Defense': 65, 'Sp. Attack': 65, 'Sp. Defense': 110, 'Speed': 30, 'Total': 540},
        "Type": ['Normal'],
        "National Number": '0143',
        "Image": ['Images/ronflex.png', '#00606A']
    }
]
# Initialisation des variables de recherche globales
name_to_search = ""
number_to_search = ""

# récupération des textes des widgets entry en minuscules
name_to_search = add_entry_name.get().lower()
number_to_search = add_entry_number.get().lower()

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

    i = max(0, min(i, len(pokedex) - 1))

    # récupération de la liste des pokemons
    pokelist = [value for value in pokedex[0].items()]

    if move == 'forward':
        try:
            i = (i + 1) % len(pokedex)
            # i = pokedex[i + 1]["Name"] if i + 1 < len(pokedex) else pokedex[0]["Name"]
            afficher_pokemon(i)
        except IndexError:
            i = len(pokedex) -1 #si erreur c'est que retour à celui d'avant
            # i = pokelist[0] #si erreur c'est que retour à 0
    elif move == 'backward':
        try:
            i = (i - 1) % len(pokedex)
            # i = pokedex[i - 1]["Name"] if i - 1 >= 0 else pokedex[len(pokedex) - 1]["Name"]
            afficher_pokemon(i)
        except IndexError:
            i = 0
            # i = pokelist[len(pokedex) - 1] #si erreur c'est que retour à celui d'avant
    create_buttons(i)

def search_by_name():
    global name_to_search
    name_to_search = search_label1.get().lower()
    # name_to_search = name  
    
    for i, pokemon in enumerate(pokedex):
        if pokemon["Name"].lower() == name_to_search:
            afficher_pokemon(i)
            return
        
    messagebox.showwarning("Error", "The pokemon is not in the list! Add the pokemon to the list!")

    
def search_by_number():
    global number_to_search
    number_to_search = search_label2.get()
    # number_to_search = number

    for i, pokemon in enumerate(pokedex):
        if pokemon["National Number"] == number_to_search:
            afficher_pokemon(i)
            return
    messagebox.showinfo("Error", "The pokemon is not in the list! Add the pokemon to the list!")

recherche_bouton1 = tk.Button(search_frame, text = "Search by name", font = "OCR 12", bg="#ffcccc", fg="#7a0000", relief="raised", command=search_by_name)
recherche_bouton1.grid(row=1, column=1, padx=3, pady=5)

recherche_bouton2 = tk.Button(search_frame, text = "Search by number", font="OCR 12", bg="#ffcccc", fg="#7a0000", relief="raised",command=search_by_number)
recherche_bouton2.grid(row=2, column=1, padx=5, pady=5)

def add_pokemon():
    global pokedex
    new_pokemon = {
        "Name": add_entry_name.get(),
        "Stats": {
            'HP': int(add_entry_hp.get()),
            'Attack': int(add_entry_attack.get()),
            'Defense': int(add_entry_defense.get()),
            'Sp. Attack': int(add_entry_spattack.get()),
            'Sp. Defense': int(add_entry_spdefense.get()),
            'Speed': int(add_entry_speed.get()),
            'Total': int(add_entry_total.get())
        },
        "Type": [add_entry_type.get()],
        "National Number": add_entry_number.get(),
        "Image": ['Images/placeholder.png', '#FFFFFF']
    }

    # add a new pokemon
    pokedex.append(new_pokemon)
    messagebox.showinfo("Success", "The pokemon has been added!")

    add_entry_name.delete(0, "end")
    add_entry_number.delete(0, "end")
    add_entry_type.delete(0, "end")
    add_entry_hp.delete(0, "end")
    add_entry_attack.delete(0, "end")
    add_entry_defense.delete(0, "end")
    add_entry_spattack.delete(0, "end")
    add_entry_spdefense.delete(0, "end")
    add_entry_speed.delete(0, "end")
    add_entry_total.delete(0, "end")

add_bouton = tk.Button(add_frame, text = "Add the pokemon", font = "Garamond 14", command=add_pokemon, relief="raised", bg="#43B14B")
add_bouton.grid(row=11, column=0, columnspan=2)

# play_music()
# threading.Thread(target=playsound, args=("Son/pokemontheme.mp3",)).start()
afficher_pokemon(len(pokedex) - 1)
fenetre.mainloop()