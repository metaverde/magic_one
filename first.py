#Ideally in sigil form- My kitchen is sparkling clean- for example
goal=""
def thank_you_gods(goal):
    count=0
    god = input("Which god are you petitioning?: ")
    god = str(god)
    times = input( "How many times would you like to input?: ")
    times= int(times)
    when = input("What is the timeframe for this magick?: ")
    while count < times:
        goal= input("What would you like to have happened " + when + " hence?: ")
        count+= 1
        print("Thank-you " + god +": " + goal + "!")

thank_you_gods(goal)


        
