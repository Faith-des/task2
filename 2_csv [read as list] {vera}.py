# open the file
count=0
with open ('2_vera.csv','r') as f:
    for line_number,line in enumerate(f):
        if line_number == 0:
            continue  
        state, price, sqft = line.rstrip('\n').split(',')
        # breakpoint()
        price = int(price.lstrip('$'))
        sqft = int(sqft)
        # if state =='California':
        #     if price/sqft >=40:
        #         count+=1
        if state == 'California' and price/sqft >= 40:
            count += 1
print (count)
        
