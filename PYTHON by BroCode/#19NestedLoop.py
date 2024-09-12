#nested loop  = a loop within another loop (outer, inner)

rows= int(input("Enter the row: "))
column= int(input("Enter the column: "))
symbol= input("Enter the symbol: ")

for x in range(rows):
    for y in range(0,column):
        print(symbol, end=" ")
    print()