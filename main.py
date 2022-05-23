# Price by Provider and Size
LP_MR_S = 1.50
LP_M = 4.90
LP_L = 6.90
MR_S = 0.50
MR_M = 3.00
MR_L = 4.00

# Lists of data: Date,Size and Carrier
input_data_raw = []
date_raw = []
size_raw = []
carrier_raw = []

# List of cost per delivery
cost = []

# List of discount per delivery
discount = []
# Count  L shipment via LP
count_LP_L = 0

# The third L shipment via LP is free, once a calendar month.
calendar_days = 30

# Open and read input.txt data
with open('input.txt','r+') as f: lines = f.read().splitlines()
for line in lines:
    input_data_raw.append(line.split(" "))

# Select specific data in file and create lists of: Date,Size and Carrier
for data in input_data_raw:
    date_raw.append((data[0]))
    size_raw.append(data[1])
    try:
        carrier_raw.append(data[2])
    except:
        carrier_raw.append("Ignore")

 # Calculation module
for value in input_data_raw:
    try:
        if value[1] == 'S' and value[2] == 'LP':
            price = LP_MR_S
            discounted_price = ('-')
            cost.append(price)
            discount.append(discounted_price)
        elif value[1] == 'M' and value[2] == 'LP':
            price = LP_M
            discounted_price = ('-')
            cost.append(price)
            discount.append(discounted_price)
        elif value[1] == 'L' and value[2] == 'LP':
            count_LP_L +=1
            if (count_LP_L == 3) and (len(date_raw) < calendar_days):
                price = 0
                cost.append(price)
                discounted_price = LP_L
                discount.append(discounted_price)
            else:
                price = LP_L
                discounted_price = ('-')
                cost.append(price)
                discount.append(discounted_price)
        elif value[1] == 'S' and value[2] == 'MR':
            price = MR_S
            discounted_price = 0.50
            cost.append(price)
            discount.append(discounted_price)
        elif value[1] == 'M' and value[2] == 'MR':
            price = MR_M
            discounted_price = ('-')
            cost.append(price)
            discount.append(discounted_price)
        elif value[1] == 'L' and value[2] == 'MR':
            price = MR_L
            discounted_price = ('-')
            cost.append(price)
            discount.append(discounted_price)
        elif (value[1] != 'S' or 'M' or 'L') and (value[2] != 'LP' or 'MR'):
            price.append('Ignored')
    except:
            price = 'Ignored'
            cost.append(price)


# Make a flat list (out of a list of lists)
input_data = [item for sublist in input_data_raw for item in sublist]

all_data = []
all_data.append(input_data)
all_data.append(cost)
all_data.append(discount)
all_data = [item for sublist in all_data for item in sublist]

with open("output.txt", "w") as file:
    content = str(all_data)
    file.write(content)
    file.close()



