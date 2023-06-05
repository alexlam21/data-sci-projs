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
