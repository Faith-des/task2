import csv
count=0
with open('vera.csv','r') as f:
    reader = csv.DictReader(f,delimiter=',')
    for row in reader:
        price = int(row['price'].lstrip('$'))
        sqft = int(row['sqft'])
        if row['state'] == 'California' and price/sqft >= 40:
            count += 1

print(count)
