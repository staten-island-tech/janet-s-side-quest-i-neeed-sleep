## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list

file_path = "SalesData.csv"  
data = csv_to_list(file_path)


a = 0

for i in data[1:]:
    for e in range(1,30):
        a += int(i[e])
    a/=30
    a = round(a, 2)
    print(f"{i[0]}:{a}")