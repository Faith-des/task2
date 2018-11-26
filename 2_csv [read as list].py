# breakpoint()
# help()
# dir()
# type()

# import csv
# count=0
# with open('vera.csv','r') as f:
#     reader = csv.DictReader(f,delimiter=',')
#     data_reader = [row for row in reader]
#     for data_reader in row:
#         if data_read[0] == 'California':
#             price = int(data_read[-2].replace('$','0'))
#             foot = price/data_read[-1]
#             if foot>=40:
#                 count+=1

state_count = 0
sqft_count = 0
with open('2 vera.csv', 'r') as f:
    # f = file object
    # With enumerate(), it adds a counter for every item of the loop
    for line_number, line in enumerate(f):
        # Skip the first line of the file
        if line_number == 0:  # 0 is the first line
            continue  # immediately loop again (don't run any code below)
        # Remove the trailing \n from each line.
        line = line.rstrip('\n')
        # Split the line (string) into a list on the comma
        line = line.split(',')
        # Assign the data to variables
        state, price, sqft = line
        # Convert price to an int (we must remove the $, first)
        price = int(price.lstrip('$'))
        # Convert sqft
        sqft = int(sqft)
        # Is the state California?
        if state == 'California':
            state_count += 1
        # Is the price per square foot >= 40
        price_per_square_foot = price / sqft
        if price_per_square_foot >= 40:
            sqft_count += 1

print(state_count)
print(sqft_count)
