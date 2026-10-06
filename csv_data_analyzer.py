import csv

with open("sample_data.csv", "r") as file:
    data = file.read()
# print()
# print(data)


lines = data.splitlines()
# print()
# print(lines
# print()
# print(type(data))
# print()
# print(type(lines))

header = lines[0]
records =  lines[1:]

# print(lines[0])
# print(header)
# print(records)
# print(len(records))
# print(type(records))

header_fields = header.split(",")
# print(header_fields)
# print(header_fields.index("Origin"))

records_as_dicts = []

for record in records:
    fields = record.split(",")
    record_dict = {
    "Load_ID": fields[0],
    "Date": fields[1],
    "Origin": fields[2],
    "Destination": fields[3],
    "Product": fields[4],
    "Quantity_tonnes": fields[5],
    "Distance_km": fields[6],
    "Status": fields[7]
    }
    records_as_dicts.append(record_dict)

# print(records_as_dicts)
# print(len(records_as_dicts))
# print(records_as_dicts[15])
# print(records_as_dicts[0]["Destination"])

#  print(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7])

# print(record["Date"])
# print(record["Origin"])
# print(record["Status"])
# print(record["Product"])
# print(record["Destination"])

# print("columns:", len(header_fields))
# print("Records:", len(records))
# print("Header Fields:", header_fields)

search_id = input("Enter Load ID: ").strip().upper()

found = False

for record in records_as_dicts:
    if record["Load_ID"] == search_id:
        print("----------------------------------------")
        print("             LOAD RECORD")
        print("----------------------------------------")
        print(f"Load ID:       {record['Load_ID']}")
        print(f"Date:          {record['Date']}")
        print(f"Origin:        {record['Origin']}")
        print(f"Destination:   {record['Destination']}")
        print(f"Product:       {record['Product']}")
        print(f"Quantity:      {record['Quantity_tonnes']} tonnes")
        print(f"Distance:      {record['Distance_km']} km")
        print(f"Status:        {record['Status']}")
        print("----------------------------------------")
        found = True

if not found:
     print(f"Invalid Load ID: {search_id}. Please try again.")



    




