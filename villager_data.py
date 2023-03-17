"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    the_file = open(filename)

    for line in the_file:
        line = line.strip()
        villager_data = line.split("|")
        species.add(villager_data[1])

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    the_file = open(filename)
    
    villagers = []


    for line in the_file:
        line = line.strip()
        villager_data = line.split("|")
        if villager_data[1] == search_string or search_string == "All":
            villagers.append(villager_data[0])
        #print(villager_data)

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    the_file = open(filename)
    
    fit_villagers = []
    nat_villagers = []
    edu_villagers = []
    mus_villagers = []
    fash_villagers = []
    play_villagers = []

    for line in the_file:
        line = line.strip()
        villager_data = line.split("|")

        if villager_data[3] == "Fitness":
            fit_villagers.append(villager_data[0])

        elif villager_data[3] == "Nature":
            nat_villagers.append(villager_data[0])

        elif villager_data[3] == "Education":
            edu_villagers.append(villager_data[0])

        elif villager_data[3] == "Music":
            mus_villagers.append(villager_data[0])

        elif villager_data[3] == "Fashion":
            fash_villagers.append(villager_data[0])

        elif villager_data[3] == "Play":
            play_villagers.append(villager_data[0])

    fit_villagers.sort()
    nat_villagers.sort()
    edu_villagers.sort()
    mus_villagers.sort()
    fash_villagers.sort()
    play_villagers.sort()

    return [fit_villagers, nat_villagers, edu_villagers, mus_villagers, fash_villagers, play_villagers]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    the_file = open(filename)

    for line in the_file:
        line = line.strip()
        villager_data = line.split("|")
        all_data.append(tuple(villager_data))

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.
    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    the_file = open(filename)

    for line in the_file:
        line = line.strip()
        villager_data = line.split("|")
        if villager_data[0] == villager_name:
            return villager_data[4]
        #else:            continue
    
    return None


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """


    the_file = open(filename)

    like_villagers = set()

    for line in the_file:
        line.strip()
        villager_data = line.split("|")
        if villager_data[0] == villager_name:
            personality = villager_data[2]
            break

   
    the_file = open(filename)

    for line in the_file:
        line.strip()
        villager_data = line.split("|")
        if villager_data[2] == personality:
            like_villagers.add(villager_data[0])


  
    return like_villagers
