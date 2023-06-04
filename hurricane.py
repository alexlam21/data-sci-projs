damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']
conversion = {"M": 1000000,
              "B": 1000000000}

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
