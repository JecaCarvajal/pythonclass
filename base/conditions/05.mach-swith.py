#Otra condicion es swith pero en python se llama mach (smell bad) 
#Ejemplo con if 
#Pattern Matching
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print(f"{day} is a weekend.")
elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print(f"{day} is a weekday.")
else: 
    print("That's not valid day of the week.")

day = "Saturday"

match day: 
    case "Saturday" | "Sunday":
        print(f"{day} is a weekend.")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day} is a weekday.")
    case _:
        print("That's not valid day of the week.")

config = {"type": "database", "name": "PostgreSQL", "version": 13 }

#Pattern Matching
match config:
    case {"type": "database", "name": name, "version": version }:
        print(f"Database {name} (Version {version})")
    case {"type":"cache", "name": name}:
        print(f"Cache system {name}")
    case _:
        print("Unknown configuration.")  


point = (5,4)

match point:
    case (x,y) if x == y:
        print(f"Point is on diagnal at {x} ")
    case (x,y) if x > 0 and y > 0:
        print(f"Point {point} is in the first quedrant")
    case (x,y):
        print(f"Point {point} is somewhere else") 


        
