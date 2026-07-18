# Part 1: Ask for today's temperature
temperature = int(input("Enter today's temperature in Celsius: "))

# Part 2: Decide between a jacket and a t-shirt
if temperature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a", outfit)
else:
    outfit = "t-shirt" # Fixed your t=shirt typo here
    print("It is warm today.")
    print("Wear a", outfit)
    
# Part 3: Ask whether it is raining
is_raining = input("Is it raining today? (yes/no): ")

# Part 4: Add an umbrella reminder only if it is raining
if is_raining == "yes":
    print("Bring an umbrella!")

# Part 5: Ask for the wind speed
wind_speed = int(input("Enter the wind speed in km/h: "))

# Part 6: Decide whether a windbreaker is needed
if wind_speed > 30:
    needs_windbreaker = "yes" # Fixed your variable name here
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
    print("The ground is dry.")

# Part 9: Ask for homework time
homework_hours = float(input("How many hours of homework do you have today?: "))

# Part 10: Decide whether homework must be the priority
if homework_hours > 2:
    print("Priority: You have a lot of homework!")
    print("Do your assignments first.")
else:
    print("Priority: Your homework load is light or finished!")
    print("You can move on to your free time.")

# Part 11: Ask for free time
free_hours = float(input("How many hours of free time do you have today?: "))

# Part 12: Decide on the activity scale based on free time
if free_hours >= 3:
    print("Activity Option: You have plenty of free time today!")
    print("You can plan a major activity or hang out with friends.")
else:
    print("Activity Option: Your free time is limited today.")
    print("Stick to a quick hobby or a short rest.")
