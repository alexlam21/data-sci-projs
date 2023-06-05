# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M',
          '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M',
          '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded',
          '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B',
          '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
          '91.6B', '25.1B']

# 1
def getNumericalValues(damages_list, conversion_dict):
    numerical_damages = []
    for amount in damages_list:
        if amount[-1] == 'd':
            numerical_damages.append(amount)
        else:
            cost = float(amount[:-1])
            multiplier = conversion[amount[-1]]
            numerical_amount = cost * multiplier
            numerical_damages.append(numerical_amount)
    return numerical_damages
# Update Recorded Damages
conversion = {"M": 1000000,
             "B": 1000000000}

# test function by updating damages
updated_damages = getNumericalValues(damages, conversion)

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 2
def createDictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dictionary = {}
    num_of_hurricanes = len(names)
    for i in range(num_of_hurricanes):
        dictionary[names[i]] = {"Name": names[i], 
                                "Month": months[i], 
                                "Year": years[i], 
                                "Max Sustained Wind": max_sustained_winds[i], 
                                "Areas Affected": areas_affected[i], 
                                "Damage": damages[i], 
                                "Deaths": deaths[i]}
    return dictionary
# Create a Table
hurricanes = createDictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
# Create and view the hurricanes dictionary
print(hurricanes)

# 3
# Organizing by Year
# def yearlyHurricaneDict(hurricaneDict, years):
#     hurricanes_by_year = {}
#     keys = list(hurricaneDict.keys())
   
#     for year in years:
#         hurricanes_by_year[year] = []             #This was my first attempt and gives correct output
#     counter = 0                                   #albeit not as elegant. A better solution uses only a dict.
#     for year in years:
#         hurricanes_by_year[year].append(hurricanes[keys[counter]])
#         counter += 1
        
#     return hurricanes_by_year

def createYearlyDictionary(hurricanes_by_name):
    hurricanes_by_year = {}
    for hurricane_name in hurricanes_by_name:
        current_year = hurricanes_by_name[hurricane_name]["Year"]
        hurricane_dictionary = hurricanes_by_name[hurricane_name]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [hurricane_dictionary]
        else:
            hurricanes_by_year[current_year].append(hurricane_dictionary)
    return hurricanes_by_year
# create a new dictionary of hurricanes with year and key
hurricanes_by_year = createYearlyDictionary(hurricanes)

print(hurricanes_by_year[1932])

# 4
# Counting Damaged Areas
def createAreaCountDictionary(hurricanes):
    areaDict = {}
    for cane in hurricanes:
        for area in hurricanes[cane]['Areas Affected']:
            if area not in areaDict:
                areaDict[area] = 1
            else:
                areaDict[area] += 1
    return areaDict


# create dictionary of areas to store the number of hurricanes involved in
affected_area_count = createAreaCountDictionary(hurricanes)

# 5
# Calculating Maximum Hurricane Count
def getMaxHurricaneAreaCount(areaDict):
    current_max = 0
    current_area = ""
    for area in areaDict:
        if areaDict[area] > current_max:
            current_area = area
            current_max = areaDict[area]
    return current_area, current_max
# find most frequently affected area and the number of hurricanes involved in
area, amount_struck = getMaxHurricaneAreaCount(affected_area_count)

print("{area_name} has been struck {amount} times by hurricanes! The largest amount of any other area!".format(area_name = area, amount = amount_struck))

# 6
# Calculating the Deadliest Hurricane
def getDeadliestHurricane(hurricanes):
    hurricane_name = ""
    max_deaths = 0
    for cane in hurricanes:
        if hurricanes[cane]["Deaths"] > max_deaths:
            max_deaths = hurricanes[cane]["Deaths"]
            hurricane_name = hurricanes[cane]["Name"]
    return hurricane_name, max_deaths
# find highest mortality hurricane and the number of deaths
hurricane_name, mortality = getDeadliestHurricane(hurricanes)
print("Hurricane {hurricane_name} was the deadliest hurricane. {amount_dead} individuals died".format(hurricane_name = hurricane_name, amount_dead = mortality))

# 7
# Rating Hurricanes by Mortality
def createMortalityDict(hurricanes):
    mortalityDict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for cane in hurricanes:
        if hurricanes[cane]["Deaths"] == 0:
            mortalityDict[0].append(hurricanes[cane])
        elif hurricanes[cane]["Deaths"] > 0 and hurricanes[cane]["Deaths"] <= 100:
            mortalityDict[1].append(hurricanes[cane])
        elif hurricanes[cane]["Deaths"] > 100 and hurricanes[cane]["Deaths"] <= 500:
            mortalityDict[2].append(hurricanes[cane])
        elif hurricanes[cane]["Deaths"] > 500 and hurricanes[cane]["Deaths"] <= 1000:
            mortalityDict[3].append(hurricanes[cane])
        elif hurricanes[cane]["Deaths"] > 1000 and hurricanes[cane]["Deaths"] <= 10000:
            mortalityDict[4].append(hurricanes[cane])
        else:
            mortalityDict[5].append(hurricanes[cane])
    return mortalityDict
# categorize hurricanes in new dictionary with mortality severity as key
mortality_scale = createMortalityDict(hurricanes)
print(mortality_scale[5])

# 8
# Calculating Hurricane Maximum Damage
def getCostliestHurricane(hurricanes):
    max_cost = 0
    hurricane_name = ""
    for cane in hurricanes:
        if hurricanes[cane]["Damage"] == 'Damages not recorded':
            continue
        else:
            if hurricanes[cane]["Damage"] > max_cost:
                max_cost = hurricanes[cane]["Damage"]
                hurricane_name = hurricanes[cane]["Name"]
    return hurricane_name, max_cost
# find highest damage inducing hurricane and its total cost
name, damage = getCostliestHurricane(hurricanes)
print("Hurricane {hurricane_name} was the most destructive hurricane. Costing ${amount} in damages!".format(hurricane_name = name, amount = damage))

# 9
# Rating Hurricanes by Damage
def categorize_by_damage(hurricanes):
    """Categorize hurricanes by damage and return a dictionary."""
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    hurricanes_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for cane in hurricanes:
        total_damage = hurricanes[cane]['Damage']
        if total_damage == "Damages not recorded":
            hurricanes_by_damage[0].append(hurricanes[cane])
        elif total_damage == damage_scale[0]:
            hurricanes_by_damage[0].append(hurricanes[cane])
        elif total_damage > damage_scale[0] and total_damage <= damage_scale[1]:
            hurricanes_by_damage[1].append(hurricanes[cane])
        elif total_damage > damage_scale[1] and total_damage <= damage_scale[2]:
            hurricanes_by_damage[2].append(hurricanes[cane])
        elif total_damage > damage_scale[2] and total_damage <= damage_scale[3]:
            hurricanes_by_damage[3].append(hurricanes[cane])
        elif total_damage > damage_scale[3] and total_damage <= damage_scale[4]:
            hurricanes_by_damage[4].append(hurricanes[cane])
        elif total_damage > damage_scale[4]:
            hurricanes_by_damage[5].append(hurricanes[cane])
    return hurricanes_by_damage

# categorize hurricanes in new dictionary with damage severity as key
hurricanes_by_damage = categorize_by_damage(hurricanes)
print(hurricanes_by_damage[5])
