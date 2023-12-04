
max_life = 0
min_life = 10000
count = 0
year_total = 0
country_total = 0
country_count = 0

with open("C:/Users/eawes/OneDrive/Documents/Classes/Repository/CSE_110/Week_7&8/life_expectancy.csv") as info:
    for line in info:
        parts = line.split(",")
        country = parts[0].strip()
        country_code = parts[1].strip()
        year = parts[2]
        life_expectancy = float(parts[3].strip())

        if life_expectancy > max_life:
            max_life = life_expectancy
            max_country = country
            max_year = year
        
        if life_expectancy < min_life:
            min_life = life_expectancy
            min_country = country
            min_year = year

print(f'The overall max life expectancy is: {max_life} from {max_country} in {max_year}')
print(f'The overall min life expectancy is: {min_life} from {min_country} in {min_year}')

year_input = int(input('What Year would you like to find the average Life Expectancy for? '))
with open("C:/Users/eawes/OneDrive/Documents/Classes/Repository/CSE_110/Week_7&8/life_expectancy.csv") as info:
    for line in info:
        parts = line.split(",")
        country = parts[0].strip()
        country_code = parts[1].strip()
        year = int(parts[2])
        life_expectancy = float(parts[3].strip())
        
        if year == year_input:
            year_total += life_expectancy
            count += 1

if count > 0:
    year_average = year_total / count
    print(f'{year_average}')
else:
    print('No data found for given year.')

country_input = input('What Country would you like to find the average Life Expectancy for? ').capitalize()
with open("C:/Users/eawes/OneDrive/Documents/Classes/Repository/CSE_110/Week_7&8/life_expectancy.csv") as info:
    for line in info:
        parts = line.split(",")
        country = parts[0].strip()
        country_code = parts[1].strip()
        year = int(parts[2])
        life_expectancy = float(parts[3].strip())
        
        if country == country_input:
            country_total += life_expectancy
            country_count += 1

if country_count > 0:
    country_average = country_total / country_count
    print(f'The average life expectancy for {country_input} is {country_average}')
else:
    print('No data found for given country.')