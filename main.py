# Part 1: Ask for today's temperature
temperature = int(input("Enter today's temperature in Celsius"))

# Part 2: Decide between a jacket and a t-shirt
if temperature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a", outfit)
else:
    outfit = "t=shirt"
    print("It is warm today.")
    print("Wear a", outfit)
    
# Part 3: Ask whether it is raining
is_raining = input("Is it raining today? (yes/no):  ")

# Part 4: Add an umbrella reminder only if it is raining
if is_raining == "yes":
    print("Bring an umbrella!")

# Part 5: Ask for the wind speed
wind_speed = int(input("Enter the wind speed in km/h:   "))

# Part 6: Decide whether a windbreaker is needed
if wind_speed > 30:
    needs_wind_speed = "yes"
    print("It is windy today.")
    print("Wear a windbreaker over your", outfit)
else:
    needs_windbreaker = "no"
    print("It is very calm today.")
    print("No windbreaker needed over your", outfit)
    
# Part 7: Ask whether there are puddles on the ground
has_puddles = input("Are there puddles on the ground? (yes/no): ")

# Part 8: Decide between boots and sneakers
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry")
