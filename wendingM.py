import csv

inv = dict()
with open('test.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for line in reader:
        inv[line['key']] = [line['description'], line['price'], line['quantity']]

print(inv)        
exit(1)

def reducedValue (Numbr):
    d= int(Numbr)
    d = d- 1
    Numbr = str(d)
    return Numbr

def saved_code():
    try:
        for i in wpg:
            if a == i[2]:
                print (i[1])
                b = input("the amount")
                c=float(b)
                if c > float(i[1]):
                    d= c-float(i[1])
                    print(d)
                elif c< float(i[1]):
                    print("please pay to reach the amount")
                else :
                    Total = Total + c
                    i[3] = reducedValue(i[3])
                    print ("item bought succesfully")
    except Exception as exc:
        print (exc)
        # break

def print_inventory(inv_dict):
    for key, value in inv_dict.items():
        print("%s: %s: %s" % (key, value[0], value[1]))
            
def purchase(inv_dict, a, balance):
    result = None
    if a not in inv_dict:
        print("Could not find %s" % a)
    else:
        item = inv_dict[a]
        if balance < item[1]:
            print("Please add %s" % (item[1] - balance))
        else:
            print("Purchased %s" % item[0])
            balance = balance - item[1]
            result = balance
    return result

inventory_dict = dict()
with open("initial_food_inventory.csv") as wpgfile :
    reader = csv.reader(wpgfile)
    for line in reader:
        inventory_dict[line[2]] = [line[0], float(line[1]), int(line[3])]
    
Total = 0.0
while True:
    print_inventory(inventory_dict)
    print("Balance: {}".format(Total))
    a = input("enter the a code, money, or quit: ")
    if '.' in a:
        Total += float(a)
    elif a.startswith('q') or a.startswith('e'):
        print("Exiting")
        break
    else:
        result = purchase(inventory_dict, a, Total)
        if result is not None:
            Total = result
