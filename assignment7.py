#exercise7.1
seasons= ( "winter","spring", "summer", "autumn")

month = int(input("Enter number (1 to 12) corresponding to months: "))

if month in [12,1,2]:
    print(seasons[0])
elif month in [3,4,5]:
    print(seasons[1])
elif month in [6,7,8]:
    print(seasons[2])
elif month in [9,10,11]:
    print(seasons[3])
else:
    print("Please enter valid month number(1-12).")

#exercise:7.2
names = set()
while True:
    name = input("Enter Name: ")
    if(name == ""):
        break
    if name in names:
        print("Existing Name.")
    else:
        print("New name.")
        names.add(name)

print("\nThe names are: ")
for name in names:

#exercise:7.3
airports = {
    "EFHK": "Helsinki-Vantaa",
    "EFTU": "Turku Airport",
    "EFTP": "Tampere-Pirkkala",
    "EFOU": "Oulu Airport",
    "EFRO": "Rovaniemi Airport",
    "EFKU": "Kuopio Airport",
    "EFVA": "Vaasa Airport"
}

while True:
    decision = input(
        "Enter a new airport, fetch the information of an existing airport or quit. Type 'new' for new airport, 'fetch' for fetching details and 'quit' for quiting: ").lower()
    if decision == "new":
        code = input("Enter the ICAO code of the airport: ").upper()
        name = input("Enter the name of the airport: ")

        if code in airports:
            print("Airport already exists.")
        else:
            airports[code] = name
            print("Airport successfully added.")

    elif decision == "fetch":
        code = input("Enter the ICAO code of the airport: ").upper()
        if code in airports:
            print(airports[code])
        else:
            print("Airport not found.")

    elif decision == "quit":
        print("Program Ended!")
        break
    else:
        print("Invalid option. Use: new, fetch, or quit.")