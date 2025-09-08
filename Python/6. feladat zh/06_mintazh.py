def load_data(file_name):
    with open(file_name, "r", encoding="UTF-8") as f:
        return f.readlines()
    
def calculate_alcohol_consumption(beer, wine, spirit):
    return (5 * beer + 11 * wine + 40 * spirit) / 100

def process_data(file_name):
    raw_data = load_data(file_name)

    raw_data.pop(0)

    data =[]
    for r in raw_data:
        line = r.strip().split(",")
        line[3] = float(line[3])
        line[4] = int(line[4])
        line[5] = float(line[5])        
        line[6] = int(line[6])
        line[7] = int(line[7])
        line[8] = int(line[8])

        total_alcohol_consumption = calculate_alcohol_consumption(line[6], line[7], line[8])
        line.append(total_alcohol_consumption)

        data.append(line)
    
    return data

def filter_data(data):
    from_value = input("Add meg az alkohol fogyasztás minimum értékét: ")

    if not from_value.isnumeric():
        return
    
    from_value = int(from_value)

    filtered_data = []

    for d in data:
        if d[-1] > from_value:
            filtered_data.append(f"{d[0]},{d[3]},{d[-1]}")

    output = "\n".join(filtered_data)

    with open("eredmenyek.txt", "w", encoding="UTF-8") as f:
        f.write(output)
    
    print("A fájlba írás befejeződött.")

data = process_data("HappinessAlcoholConsumption.csv")
while(True):
    menu = input("********FŐMENÜ*******************\n(M) Adott fogyasztás feletti értékek fájlba írása\n(Q) Kilépés\n")
    if menu.lower() == "m":
        filter_data(data)
    elif menu.lower() == "q":
        break