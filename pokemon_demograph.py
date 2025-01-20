from typing import NamedTuple, List, Optional
import csv
import matplotlib.pyplot as pyplot

##################
# Data Definitions
Type2Checker = Optional[str]

#interp. there is no Type 2 for a pokemon (none), or there is a Type 2 of str

T2C_0 = None
T2C_1 = "poison"
T2C_2 = "fire"
T2C_3 = "flying"

@typecheck
#Template based on optional
def fn_for_type_2_checker(t: Type2Checker) -> ...:
    if t == None:
        return ...
    else:
        return ...(t)


      
    

PokemonStats = NamedTuple("PokemonStats", [("against_bug", float),                                           
                                           ("against_dark", float),
                                           ("against_dragon", float), 
                                           ("against_electric", float),
                                           ("against_fairy", float),
                                           ("against_fight", float),
                                           ("against_fire", float),
                                           ("against_flying", float),
                                           ("against_ghost", float),
                                           ("against_grass", float),
                                           ("against_ground", float),
                                           ("against_ice", float),
                                           ("against_normal", float),
                                           ("against_poison", float),
                                           ("against_psychic", float),
                                           ("against_rock", float),
                                           ("against_steel", float),
                                           ("against_water", float),                                           
                                           ("defense", int),
                                           ("name", str),
                                           ("type1", str),
                                           ("type2", Type2Checker)])
                                           
#interpr. PokemonStats including all the values against each of the 18 types of pokemon in float,
#the defense value in int, name in str, the Type1 in str
#and the Type 2 in the built in data type Type2Checker which is used to check if there is a type 2
#or not.


PS1 = PokemonStats(2.0,1.0,1.0,0.5,0.5,1.0,1.0,0.5,2.0,2.0, 1.0, 1.0, 0.5, 0.5, 2.0, 1.0, 2.0, 0.5, 78, "Charmander", "fire", "ghost")
PS2 = PokemonStats(1,2,1,1,0.5,1,2,0.5,2,0.5, 1, 1, 0.5, 1, 0.5, 1, 2, 0.5, 78, "Pidgey", "flying", None)
PS3 = PokemonStats(1.0,1.0,1.0,0.5,0.5,0.5,2.0,2.0,1.0,0.25,1.0,2.0,1.0,1.0,2.0,1.0,1.0,0.5, 49, "Bulbasaur", "grass", "poison")
PS4 = PokemonStats(0.5,1.0,1.0,1.0,0.5,1.0,0.5,1.0,1.0,0.5,2.0,0.5,1.0,1.0,1.0,2.0,0.5,2.0, 58, "Charmeleon","fire", None)
PS5 = PokemonStats(0.5,1.0,1.0,1.0,0.5,1.0,0.5,1.0,1.0,0.5,2.0,0.5,1.0,1.0,1.0,2.0,0.5,2.0, 58, "Rivoflavin","fire", "flying")
PS6 = PokemonStats(0.5,1.0,1.0,1.0,0.5,1.0,0.5,1.0,1.0,0.5,2.0,0.5,1.0,1.0,1.0,2.0,0.5,2.0, 58, "Charmeleon","fire", "poison")



@typecheck
#Template based on Compounds and reference rule
def fn_for_pokemon_stats(ps: PokemonStats) -> ...:
    return ...(ps.against_bug,
               ps.against_dark,
               ps.against_dragon,
               ps.against_electric,
               ps.against_fairy,
               ps.against_fight,
               ps.against_fire,
               ps.against_flying,
               ps.against_ghost,
               ps.against_grass,
               ps.against_ground,
               ps.against_ice,
               ps.against_normal,
               ps.against_poison,
               ps.against_psychic,
               ps.against_rock,
               ps.against_steel,
               ps.against_water,
               ps.defense,
               ps.name,
               ps.type1,
               fn_for_type_2_checker(ps.type2))
    
                                


# List[PokemonStats]
# interp. a list of PokemonStats

LOPS0 = []
LOPS1 = [PS3, PS4]

@typecheck
def fn_for_lops(loc: List[PokemonStats]) -> ...: #Template based on arbitrary-sized
    # description of the accumulator
    acc = ...      # type: ...
    for s in lops:
        acc = ...(s, acc)

    return ...(acc)

#Helper Functions
@typecheck
def parse_type(t: Type2Checker) -> Optional[str]:
    """
    returns None if there is no type 2 or the type in strings if there is 
    a second type
    """
    #return "" #stub
    
    #Template
    if t == "":
        return None
    else:
        return t
    
start_testing()

expect(parse_type("ghost"), "ghost")
expect(parse_type(""), None)
expect(parse_type("flying"), "flying")

summary()

@typecheck
def type_2_exists(t: Type2Checker) -> bool:
    """
    returns True if a second type of the pokemon exist 
    """
    
    #return True #stub
    
    if t == None:
        return False
    else:
        return True
    
    
start_testing()

expect(type_2_exists(T2C_0), False)
expect(type_2_exists(T2C_1), True)
expect(type_2_exists(T2C_2), True)

summary()

@typecheck
def modified_defense(ps: PokemonStats) -> float:
    """
    returns the modified defense of the pokemon
    """
    
    #return 0.0 #stub
    
    all_against_multiplier = ps.against_bug+ps.against_dark+ps.against_dragon+ps.against_electric+ps.against_fairy+ps.against_fight+ps.against_fire+ps.against_flying+ps.against_ghost+ps.against_grass+ps.against_ice+ps.against_normal+ps.against_poison+ps.against_psychic+ps.against_rock+ps.against_steel+ps.against_water
    mod_def = ps.defense/all_against_multiplier
    return mod_def

start_testing()

expect(modified_defense(PS1), 4.105263)

summary()

# Functions

@typecheck
def main(filename: str) -> None:
    """
    Reads the file from given filename and creates a bar chart showing the modified defense of 
    dual fire type pokemons
    """
    # Template from HtDAP, based on function composition 
    return plot_bar_chart((read(filename))) 
    
    

@typecheck
def read(filename: str) -> List[PokemonStats]:
    """    
    reads information from the specified file and returns returns all the pokemon
    stats in a list
    """
    #return []  #stub
    # Template from HtDAP
    # lops contains the result so far
    lops = [] # type: List[PokemonStats]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            # you may not need to store all the rows, and you may need
            # to convert some of the strings to other types
            ps = PokemonStats(parse_float(row[1]),
                              parse_float(row[2]),
                              parse_float(row[3]),
                              parse_float(row[4]),
                              parse_float(row[5]),
                              parse_float(row[6]),
                              parse_float(row[7]),
                              parse_float(row[8]),
                              parse_float(row[9]),
                              parse_float(row[10]),
                              parse_float(row[11]),
                              parse_float(row[12]),
                              parse_float(row[13]),
                              parse_float(row[14]),
                              parse_float(row[15]),
                              parse_float(row[16]),
                              parse_float(row[17]),
                              parse_float(row[18]),
                              parse_int(row[25]),
                              row[30],
                              row[36],
                              parse_type(row[37]))
                         
            lops.append(ps)
    
    return lops


@typecheck
def plot_bar_chart(lops: List[PokemonStats]) -> None:
    """
    creates a bar chart showing the modified defense of dual fire type pokemons 
    and returns None
    """
    
    #return None #stub
    # Template based on Visualisation
    
    #list of pokemon names
    pokemon = []
    
    #list of modified defense
    modified_def = []
    
    for ps in lops:
        if type_2_exists(ps.type2) and ps.type1 == "fire":
            pokemon.append(ps.name)
            mod_def = modified_defense(ps)
            modified_def.append(mod_def)
            
    fig, ax = pyplot.subplots(1,1)
    ax.bar(pokemon, modified_def, color = "orange", width = 0.8)
    ax.set_xlim(-1, len(pokemon))
    
    
    pyplot.xticks(pokemon, rotation = 'vertical')
    
    pyplot.xlabel("Pokemon")
    pyplot.ylabel("Modified Defense")
    pyplot.title("Dual Fire Type Pokemon Defense")
    
    
    #show the plot
    pyplot.show()
    
    return None
    
    



start_testing()

# Examples and tests for main
expect(main("pokemonstat5.csv"), None)
expect(main("pokemonstat4.csv"), None)



#Examples for plot_bar_chart
expect(plot_bar_chart([PS1, PS4, PS5]), None)
expect(plot_bar_chart([PS1, PS2]), None)





#Examples and tests for read
expect(read("pokemonstat1.csv"), [PS3])
expect(read("pokemonstat2.csv"), LOPS1)


summary()

# Final Graph/Chart
main("pokemon_stats.csv")