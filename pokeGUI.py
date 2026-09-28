import tkinter as tk
import requests
from pokeAPI import get_pokemon, pokemon_types, pokemon_abilities, pokemon_stats
from PIL import Image, ImageTk
from io import BytesIO

window = tk.Tk()
window.title("PokéGUI")
window.geometry("700x700")
window.configure(bg="lightblue")


title_label = tk.Label(window, text="PokéGUI", font=("Arial", 50, "bold"), bg="lightblue")
title_label.pack()

pokemon_name = tk.Label(window, text="Who's That Pokémon?", font=("Arial", 30), bg="lightblue")
pokemon_name.pack()

search_frame = tk.Frame(window, bg="lightblue")
search_frame.pack(pady=10)
search_frame.columnconfigure(0, weight=1)

pokemon_entry = tk.Entry(search_frame, width=20)
pokemon_entry.grid(row=0, column=0, padx=5, sticky="we")

search_message = tk.Label(search_frame, text="Search for a Pokémon!", bg="lightblue")
search_message.grid(row=1, column=0)

results_frame = tk.Frame(window, bg="lightblue")
results_frame.pack()

pokemon_name_result = tk.Label(results_frame, text="", font=("Arial", 20, "bold"), bg="lightblue")
pokemon_name_result.pack()

pokemon_image = tk.Label(results_frame, bg="lightblue")
pokemon_image.pack()

info_frame = tk.Frame(results_frame, bg="lightblue")
info_frame.pack(pady=5)

type_result = tk.Label(info_frame, text="", bg="lightblue")
type_result.grid(row=0, column=0, columnspan=2)

ability_result = tk.Label(info_frame, text="", bg="lightblue")
ability_result.grid(row=1, column=0, columnspan=2)

height_result = tk.Label(info_frame, text="", bg="lightblue")
height_result.grid(row=2, column=0, padx=10, pady=10)

weight_result = tk.Label(info_frame, text="", bg="lightblue")
weight_result.grid(row=2, column=1, padx=10, pady=10)

stats_frame = tk.Frame(results_frame, bg="lightblue")
stats_frame.pack(pady=10)
stats_frame.columnconfigure(0, minsize=150)

bst_result = tk.Label(stats_frame, text="", font=("Arial", 10, "bold"), bg="lightblue", fg="red")
bst_result.grid(row=6, column=0, columnspan=2)

stat_name_list = []
stat_value_list = []

for index in range(6):
    stat_name_label = tk.Label(stats_frame, text="", bg="lightblue")
    stat_name_label.grid(row=index, column=0, sticky = "w")
    stat_name_list.append(stat_name_label)

    stat_value_label = tk.Label(stats_frame, text="", bg="lightblue")
    stat_value_label.grid(row=index, column=1, sticky = "e")
    stat_value_list.append(stat_value_label)


def search_pokemon():

    pokemon_search = pokemon_entry.get().strip().lower()

    data = get_pokemon(pokemon_search)

    if data is not None:

        image_url = data["sprites"]["front_default"]
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        photo = ImageTk.PhotoImage(image)

        search_message.config(text="")

        pokemon_name_result.config(text=data["name"].capitalize())

        types = pokemon_types(data)
        type_result.config(text=types)

        abilities = pokemon_abilities(data)
        ability_result.config(text=abilities)

        height = round(((data["height"] / 10) * 39.701), 1)
        height_result.config(text="Height: " + str(height) + " in.")

        weight = round((data["weight"] * 0.220462), 1)
        weight_result.config(text="Weight: " + str(weight) + " lbs")

        stats, stats_total = pokemon_stats(data)

        for index, stat in enumerate(stats):
            stat_name, stat_value = stat.split(":")

            stat_name_list[index].config(text=stat_name + ":")
            stat_value_list[index].config(text=stat_value)

        bst_result.config(text="Base Stat Total: " + str(stats_total))

        pokemon_image.config(image=photo)
        pokemon_image.image = photo

    else:

        search_message.config(text="Pokemon not found.")

        pokemon_name_result.config(text="Please enter a Valid Name")

        type_result.config(text="")
        ability_result.config(text="")
        height_result.config(text="")
        weight_result.config(text="")

        for stat_name_label in stat_name_list:
            stat_name_label.config(text="")

        for stat_value_label in stat_value_list:
            stat_value_label.config(text="")

        pokemon_image.config(image="")

        bst_result.config(text="")


search_button = tk.Button(
    search_frame,
    text="Search",
    command=search_pokemon,
    bg="lightblue",
    borderwidth=0,
    highlightthickness=0
)
search_button.grid(row=0, column=1, padx=5)

window.mainloop()