# Function that is going to print statements about cheese and crackers. It has 
# 2 parameters, cheese_count and boxes_of_crackers

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

def cheese_cracker_ratio(cheese, crackers):
    """Ideal ratio is one cheese slice to one cracker."""
    if cheese / crackers >= 1.0 and cheese / crackers <= 5.0:
        print "That's a good ratio."
        return True
    elif cheese / crackers > 5.0:
        print "That's a lot of cheese!"
        return False
    else:
        print "Go buy some cheese."
        return False

def buying_cheese(start_cheese,start_crackers):
    ratio_okay = False
    while ratio_okay != True:
        ratio_okay = cheese_cracker_ratio(start_cheese,start_crackers)
        print "Your cheese ratio is %f.  Go buy more cheese!"  % (float(start_cheese)/start_crackers)
        start_cheese += 5 
    print "You now have enough cheese!"


# Call the function cheese_and_crackers with numbers. 
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


# Call the function with variables that you have assigned. 
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Calls the function, while doing math on the parameters
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# calling the function, while doing math on variables used as parameters. 
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


cheese_cracker_ratio(1, 5)
cheese_cracker_ratio(6, 1)
cheese_cracker_ratio(2, 1)

buying_cheese(1,25)

