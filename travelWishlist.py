travelList = ["Seoul,South Korea" , "Mumbai,India" , "Osaka,Japan" , "New York City, USA" , "London, England" , "Paris, France",  "Dubai, UAE" , "Abu Duabi, UAE" , "Singapore Airport" , "New Dehil, India" , "Goa, India" , "Las Vegas, USA" ]
travelList.append("Mahrashtra, India")
travelList.append("Florida, USA")
travelList.append("Tokyo, Japan")

print (travelList)
print ("This is your travel destinations list")
print ("      ")

print ("This pogram can do many things such as : Adding a travel destination to the list, Finding a travel destination from the list, Removing a travel destination from the list, Sorting the destinations by alphabet and Counting how many destinations there are")
print ("      ")
print ("If you want the pogram to Add a Destination to the list, write 1 in the question below")
print ("      ")
print ("If you want the pogram to find a Destination from the list, write 2 in the question below")
print ("      ")
print ("If you want the pogram to remove a Destination to the list, write 3 in the question below")
print ("      ")
print ("If you want the pogram to sort the list of Destinations by alphabetical order, write 4 in the question below")
print ("      ")
print ("If you want the pogram to count how many destinations there are, write 5 in the question below")
print ("      ")

pogramFunction = int(input("What Do you want the pogram to do for you"))

if pogramFunction == 1: 
    print ("This pogram is adding a destination to the list")
    print ("      ")
    destination = input("Where do you want to go?")
    travelList.append(destination)
    print ("      ")
    print (travelList)

if pogramFunction == 2:
    print ("This pogram is finding a destination from the list")
    print ("      ")
    findDestination = input("Which Destination do you want to find?") 
    print ("      ")
    print (travelList.index(findDestination))

if pogramFunction == 3:
    print ("This pogram is removing a destination from the list")
    print ("      ")
    removeDestionation = input("What destination do you want to remove")
    travelList.remove(removeDestionation)
    print ("      ")
    print (travelList)
    print ("      ")
    print ("You have successfully removed the destination")

   
if pogramFunction == 4:
    print ("This pogram is sorting the list of destinations in alphabetical order")
    print ("      ")
    print (travelList)
    travelList.sort()
    print ("      ")
    print (travelList)

if pogramFunction == 5:
    print ("This pogram is counting how many destinations there are")
    print ("      ")
    print (len(travelList))
