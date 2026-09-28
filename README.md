# PokéGUI

PokéGUI is a Python desktop application using [PokéAPI](https://pokeapi.co/) 
Search for Pokémon and display information about them through a graphical user interface built with Tkinter.

## Features

* Search for Pokémon by name
* Display Pokémon sprite
* Display Pokémon types
* Display Pokémon abilities(includes hidden abilities if exists)
* Display height in inches and weight in pounds
* Display individual base stats
* Calculate and display the Base Stat Total (BST)
* Handles invalid Pokémon names

## Built With

* Python
* Tkinter
* Requests
* Pillow (PIL)
* PokéAPI

### `pokeGUI.py`

Tkinter graphical user interface handling the user input; displays Pokémon information features, and updates the GUI based on the Pokémon searched.

### `pokeAPI.py`

Contains functions responsible for requesting and processing Pokémon data from the PokéAPI.(Can use as seperate program but with Command Line Input instead)

## How Does It Work?

User enters Pokémon's name into search bar and clicks the **Search** button.

The application then:

1. Sends Pokémon name to the PokéAPI.
2. Receives Pokémon's information as JSON data.
3. Extracts information such as its name, type, abilities, height, weight, and stats.
4. Retrieves Pokémon's sprite.
5. Displays information in Tkinter GUI.

## Installation

Clone the repository:

```bash
git clone https://github.com/AndrewChan7889/PokeGUI.git
```

Install the required packages:

```bash
pip install requests pillow
```

Run the application:

```bash
python pokeGUI.py
```

## What I Learned


* New python modules such as Pillow and Tkinter and importing functions from another file
* Dictionaries and JSON data
* Lists and loops
* Functions and return values
* Exception handling
* HTTP requests and APIs
* Tkinter widgets and frames
* Tkinter `pack()` and `grid()` geometry managers
* Updating GUI widgets with `.config()`
* Displaying images in Tkinter
* Organizing a Python project into multiple files


