Cityes = {"New York": 8336697, "Los Angeles": 3979576, "Chicago": 2746388}
My_city = input("Enter a city name: ")
if My_city in Cityes:
    print(f"The population of {My_city} is {Cityes[My_city]}.")