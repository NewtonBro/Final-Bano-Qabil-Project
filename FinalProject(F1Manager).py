#Unooficial Text-based Formula One Manager game made by Bano Qabil 4.0 4:00 to 6:00 batch students of the 'Fardan, Arhum, Siddique and Muhammad Abeer' Group.

# All Classes for objects that will be required are written in the beginning: 
class Team: #this class has all attributes for teams that will be objects
    def __init__(self, name, budget, car_power, driver1, driver2):
        self.name = name
        self.budget = budget
        self.car_power = car_power
        self.drivers = [driver1, driver2]
        self.points = 0
        self.current_race = 1

class Driver: #Same thing but for drivers
    def __init__(self, name, cost, skill):
        self.name = name
        self.cost = cost
        self.skill = skill
        self.points = 0

class CarPart: #There's a marketplace I made and you can get upgrades from there, each upgrade is an object of this class
    def __init__(self, name, power_boost, cost):
        self.name = name
        self.power_boost = power_boost
        self.cost = cost

#Now we initialize the game through a function (MASSIVE)

def initialize_game(team_name):

    # Creating all drivers as objects of the driver class and storing them in a list, you'll see why I'm storing in a list later ;)
    drivers = [
        #First Twenty Drivers are gonna be in your opponent 10 teams, Each team in formula one has two drivers
        Driver("Max Verstappen", 2500000, 99),
        Driver("Yuki Tsunoda", 1000000, 92),
        Driver("Charles Leclerc", 1500000, 97),
        Driver("Lewis Hamilton", 2000000, 98),
        Driver("Kimi Antonelli", 1400000, 93),
        Driver("George Russell", 1450000, 94),
        Driver("Oscar Piastri", 2400000, 98),
        Driver("Lando Norris", 2350000, 97),
        Driver("Alexander Albon", 950000, 90),
        Driver("Carlos Sainz", 920000, 88),
        Driver("Liam Lawson", 880000, 77),
        Driver("Isack Hadjar", 850000, 76),
        Driver("Fernando Alonso", 900000, 85),
        Driver("Lance Stroll", 500000, 60),
        Driver("Pierre Gasly", 700000, 70),
        Driver("Franco Colapinto", 690000, 69),
        Driver("Esteban Ocon", 700000, 70),
        Driver("Oliver Bearman", 720000, 72),
        Driver("Nico Hulkenberg", 850000, 76),
        Driver("Gabriel Bortoleto", 720000, 72),
        # Marketplace Drivers, These wil be purchasable in the game
        Driver("Sergio Perez", 800000, 74),
        Driver("Valtteri Bottas", 890000, 87),
        Driver("Hamood Habibi", 3000000, 100),
        Driver("Luke Browning", 780000, 73),
        Driver("Daniel Riccardo", 1000000, 80),
        Driver("Mick Schumacher", 800000, 74),
        Driver("Zhou Guanyu", 780000, 73)
    ]
    
    # Creating teams and assign drivers
    teams = [
        #Now you'll see why all of them were in lists :)
        Team("Red Bull", 9000000, 970, drivers[0], drivers[1]),  # Verstappen and Tsunoda
        Team("Ferrari", 9500000, 950, drivers[2], drivers[3]),    # Leclerc and Hamilton
        Team("Mercedes", 9500000, 970, drivers[4], drivers[5]),   # Russell and Antonelli
        Team("McLaren", 10000000, 990, drivers[6], drivers[7]),   # Piastri and Norris
        Team("Williams", 8500000, 950, drivers[8], drivers[9]),   # Albon and Sainz (Smooth Operatoooor)
        Team("VCARB", 8500000, 940, drivers[10], drivers[11]),    # Lawson and Hadjar (NOOOOOO! I destroyed the caaar!)
        Team("Aston Martin", 9000000, 930, drivers[12], drivers[13]), # Alonso and Stroll
        Team("Alpine", 8500000, 900, drivers[14], drivers[15]),   # Gasly and Colapinto (Pierre GAAASSSLLYYYYYY)
        Team("Haas", 8000000, 880, drivers[16], drivers[17]),     # Ocon and Bearman (5 Seconds Penalty for Ocon XD)
        Team("Sauber", 5000000, 800, drivers[18], drivers[19])    # Hulk and Bortoleto
    ]
    
    # Player's team gets the last two drivers (Schumacher and Zhou)
    player_team = Team(team_name, 7000000, 890, drivers[-1], drivers[-2]) #You see a variable here for the name attribute? well you'll see why soon ;)
    teams.append(player_team) #Appending this object into the teams list
    
    car_parts = [
        #Creating cer parts as objects of the car part class inside a list, yk why ;) ;)
        CarPart("Gearbox Upgrade", 50, 1000000),
        CarPart("Research Aerodynamics", 20, 150000),
        CarPart("ERS Development", 25, 500000),
        CarPart("Diffuser Upgrade", 15, 100000)
    ]
    
    return teams, drivers, car_parts, player_team #Packages all lists in the intialiaztion function and stores them until asked for by anything calling those particular lists in this function

#Sir taught us we should stay prepared for invalid inputs by the user, this function does exactly that! We'll call it everytime we need to ask user for decisions 
def get_valid_input(prompt, valid_choices):
    #This loop will keep asking until valid input is received
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid input. Please choose from: {', '.join(valid_choices)}")

def get_valid_int(prompt, min_val, max_val): #Same thing but now for integers
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a valid number")

#This function will calculate the race results by using team.carpower and driver.skill, didn't use the 'random' library because sir did not allow us to use anything outside of the course

def simulate_race(teams):
    print("\n=== RACE RESULTS ===")
    team_scores = [] #A list for race results
    for team in teams: #A loop to calculate race score of each team by looping through the teams list and using each team's attributes respectively
        score = (team.drivers[0].skill + team.drivers[1].skill  + team.car_power) / 2
        team_scores.append((team, score))#Appends the team's result into the list
    
    team_scores.sort(key=lambda x: x[1], reverse=True) #Was forced to go this route as there was no other way for numerically sorting
    #.sort or sorted() is a built in method/function for sorting, in team_scores, the second element is score (points) so "lambda x: x[1]" represents the second element of the list shall be used for sorting
    #reverse = True means sort in descending order because positions are determined in that order like highest position is 1, then 2 and so on while max points are 25, 18 and so on
    points_system = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1] #In F1, the driver at first position gets 25 points, second position gets 18 and so on
    
    for i, (team, _) in enumerate(team_scores[:10]): #This loop assigns points and cash prize to each team according to their position
        points = points_system[i]
        team.points += points
        team.drivers[0].points += points
        team.drivers[1].points += points
        team.budget += 50_000 + (points * 10_000)
    
    for i, (team, _) in enumerate(team_scores, 1): #And this loop prints each teams race result and eventually an entire list of the results
        print(f"{i}. {team.name} ({team.drivers[0].name} & {team.drivers[1].name})")

def marketplace(player_team, all_drivers, car_parts, teams): #function for the marketplace you'll upgrade your team through
    print("\nx>>>>> MARKETPLACE >>>>>")
    print(f"^ Budget: ${player_team.budget}")
    
    while True:
        choice = get_valid_input("\n^ 1. Buy Driver\n^ 2. Buy Car Part\n^ 3. Exit\n> ", ["1", "2", "3"]) #remember that choice function? Well here it is!
        
        if choice == "1":
            free_agents = [d for d in all_drivers if all(d not in t.drivers for t in teams)] #loop to check all free drivers in the drivers list
            if not free_agents:
                print("No drivers available!")#if none this message pops up and continue sends user to the next block
                continue
                
            print("\nAvailable Drivers:")#Otherwise we get a list of freely avilable drivers through a loop running through and printing a list of their names and price
            for i, driver in enumerate(free_agents, 1):
                print(f"{i}. {driver.name} (Skill: {driver.skill}, Cost: ${driver.cost})")
            
            choice = get_valid_input("Choose driver (or '0' to cancel): ", [str(i) for i in range(len(free_agents)+1)])
            if choice == "0":
                continue
                
            selected_driver = free_agents[int(choice)-1]
            if player_team.budget >= selected_driver.cost: #checking whether you can actually affordthe driver or not
                player_team.drivers[0] = selected_driver
                player_team.budget -= selected_driver.cost
                print(f"Signed {selected_driver.name}!")
            else:
                print("Not enough money!")
                
        elif choice == "2":
            print("\nCar Parts:")
            for i, part in enumerate(car_parts, 1):
                print(f"{i}. {part.name} (+{part.power_boost} car power, ${part.cost})")
            
            choice = get_valid_input("Choose part (or '0' to cancel): ", [str(i) for i in range(len(car_parts)+1)])
            if choice == "0":
                continue
                
            selected_part = car_parts[int(choice)-1]
            if player_team.budget >= selected_part.cost:
                player_team.car_power += selected_part.power_boost
                player_team.budget -= selected_part.cost
                print(f"Installed {selected_part.name}! New car power: {player_team.car_power}")
            else:
                print("Not enough money!")
                
        elif choice == "3":
            break

def train_driver(player_team):
    """Improve a driver's skill"""
    print("\n=== DRIVER TRAINING ===")
    print(f"Budget: ${player_team.budget}")
    
    print("\nSelect driver to train:")
    for i, driver in enumerate(player_team.drivers, 1):
        print(f"{i}. {driver.name} (Skill: {driver.skill})")
    
    choice = get_valid_input("> ", ["1", "2"])
    cost = 50_000
    
    if player_team.budget >= cost:
        player_team.drivers[int(choice)-1].skill += 2
        player_team.budget -= cost
        print(f"Training complete! New skill: {player_team.drivers[int(choice)-1].skill}")
    else:
        print("Not enough money!")

def show_standings(teams):
    """Display championship standings"""
    print("\n=== CONSTRUCTORS' CHAMPIONSHIP ===")
    ranked_teams = sorted(teams, key=lambda t: t.points, reverse=True)
    for i, team in enumerate(ranked_teams, 1):
        print(f"{i}. {team.name}: {team.points} pts")
    
    print("\n=== DRIVERS' CHAMPIONSHIP ===")
    all_drivers = [d for team in teams for d in team.drivers]
    ranked_drivers = sorted(all_drivers, key=lambda d: d.points, reverse=True)
    for i, driver in enumerate(ranked_drivers[:10], 1):
        print(f"{i}. {driver.name}: {driver.points} pts")

#This is the loop for the main game and it's menu

def main():

    # Taking input for your team's name (remember we declared variable back then? it was for this line)
    team_name = input("Enter your team's name: ")
    
    # Initialize game with the name (remember those return values? well now is the time we use intialization function and those return values ie. lists)
    teams, all_drivers, car_parts, player_team = initialize_game(team_name)
    
    print("x>>>>> F1 Manager (Text-Based) >>>>>")
    print(f"^ Welcome, {player_team.name}'s Team Principal!")
    
    while player_team.current_race <= 24:
        print(f"x>>>>> RACE {player_team.current_race}/24 >>>>>")
        choice = get_valid_input("^ 1. Start Race\n^ 2. Marketplace\n^ 3. Train Driver\n^ 4. Standings\n^ 5. Quit\nx> ", ["1", "2", "3", "4", "5"])
        #Now you shall see how handy those function will be! :D
        if choice == "1":
            simulate_race(teams)
            player_team.current_race += 1
        elif choice == "2":
            marketplace(player_team, all_drivers, car_parts, teams)
        elif choice == "3":
            train_driver(player_team)
        elif choice == "4":
            show_standings(teams)
        elif choice == "5":
            print("Quitting...")
            return
    
    print("\nx>>>>> The 2025 Season has been completed >>>>>") #when all 24 races are completed you get season end results
    show_standings(teams)
    print("\n^ Your final position:")
    ranked_teams = sorted(teams, key=lambda t: t.points, reverse=True)
    for i, team in enumerate(ranked_teams, 1):
        if team == player_team:
            print(f"^ {i}. {team.name}: {team.points} pts <-")

if __name__ == "__main__":#ensures code runs directly and not accidently upon imports
    main()