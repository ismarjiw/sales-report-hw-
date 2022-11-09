"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # empty list for sales people
melons_sold = [] # empty list for melons sold

f = open('sales-report.txt') # opens the .txt file 

for line in f: # for loop iterating over each line in the file
    line = line.rstrip() # removes extra space R of each line
    entries = line.split('|') # removes | from between each data point in file 
    salesperson = entries[0] # identifies that a salesperson can be found
                                # at index 0 per entry 
    melons = int(entries[2]) # identifies number of melons sold per entry found at index 2

    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
        
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')