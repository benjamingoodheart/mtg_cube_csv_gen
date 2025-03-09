# MTG Cube Template CSV Generator

Basically I wanted an easy way to get every card in a given magic set and put it into a csv that I could then use to keep track of which cards I still need to get to make a cube. So, I wrote it myself.

## Pre-reqs:

Make sure you have [python3](https://www.python.org/downloads/) installed.

## Installation

### Via Download

download the source file from the tab above and unzip. Then, open the directory in a terminal application.

In the terminal run the following commands

```bash
python3 -m venv venv
source venv/bin/activate
pip -r install requirements.txt
```

### via git

```bash
git clone https://github.com/benjamingoodheart/mtg_cube_csv_gen 
cd mtg_cube_csv_gen
python3 -m venv venv
source venv/bin/activate
pip -r install requirements.txt
```

## Running the program

To run the program, make sure the virtual enviroment is active. If you're following the directions for the first time, it should be. If you're running the program subsequent times, it may not be. If it's not run the following command:

```bash
source venv/bin/activate
```

To run the program run the following command in the root of the project directory (`/mtg_cube_csv_gen`):

```bash
python3 app.py <set_code>
```

where `<set_code>` is a three letter identifying code for the given MTG set. Currently, this program can only take one set at a time. An example to generate a .csv containing all the cards for the Onslaught set (whose set code is ONS) would be as follows:

```bash
python3 app.py ons
```
you will see the following messages pointing you to the output .csv.

```bash
>>> gathering cards in set: ons
>>> writing to ./out/ons_cards.csv
>>> complete!
```

Voilà! There you go. Now you can easily begin tracking which cards you have in any given set.

### Notes

* The .csv contains default values for cards corresponding to their rarity, where commons are assigned a desired quantity of 4, uncommons a desired quantity of 3, rares and mythics a desired quantity of 1.

* this is built using the [scryfall api](https://scryfall.com/docs/api). big shout out to scryfall for the generous resource!

#### Tests

* I wrote the tests rather quickly, and I will probably improve them in the future. In the meantime you can make sure everything works by running the following command while the virtual environment is active:

``` bash
python3 tests.py 
```