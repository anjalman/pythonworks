from json import load

f=open("D:\\pythonworks\\Datasets\\countries.json",encoding="utf-8")

data=load(f)

# print number of countries

# print(len(data))

all_country_name=[country.get("name") for country in data]

# print(all_country_name)

all_region=[country.get("region") for country in data]

# print(set(all_region))

all_region_count={region:all_region.count(region) for region in all_region}

# print(all_region_count)

max_region_count=max(all_region_count,key=lambda k:all_region_count.get(k))

# print(max_region_count,all_region_count.get(max_region_count))

# capital of specific country

capital_of_counteries=[country.get("capital") for country in data if country.get("name")=="India"]

# print(capital_of_counteries)

# most border in country

country_borders_count={country.get("name"):len(country.get("borders",[])) for country in data }

# print(country_borders_count)

max_border_count=max(data,key=lambda country: len(country.get("borders",[]))).get("name")

# print(max_border_count)

max_border_count=max(country_borders_count,key=lambda k:country_borders_count.get(k))

# print(max_border_count)

# most population country

most_population_country=max(data,key=lambda country:country.get("population")).get("name")

# print(most_population_country)

alpha_3code= [country.get("borders")for country in data if country.get("name")=="China"][0]

for code in alpha_3code:

    for country in data:

        if country.get("alpha3Code")==code:

            print(country.get("name"))




