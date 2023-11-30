
max_life = 0
min_life = 10000

with open('life-expectancy.csv') as info:
    for line in info:
        parts = line.split(",")
        country = parts[0].strip()
        country_code = parts[1].strip()
        year = int(parts[2])
        life_expectany = float(parts[3].strip())

        if life_expectany > max_life:
            max_life = life_expectany
            max_country = country
            max_year = year
        
        if life_expectany < min_life:
            min_life = life_expectany
            min_country = country
            min_year = year

        print(f'The overall max life expectancy is: {max_life} from {max_country} in {max_year}')
        print(f'The overall min life expectancy is: {min_life} from {min_country} in {min_year}')

    