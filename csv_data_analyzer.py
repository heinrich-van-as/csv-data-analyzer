import csv
from datetime import datetime

with open("messy_sample_data.csv", "r") as file:
    data = file.read()
# print()
# print(data)


lines = data.splitlines()
# print()
# print(lines)
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
# Load_index = header_fields.index("Load_ID") 
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

def lookup_load():
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

def validation_quick_check():
    print("\n========== VALIDATION QUICK CHECK ==========")

    # Check for missing values
    print("\nMissing values:")

    for record in records_as_dicts:
        for key, value in record.items():
            if value == "":
                print(f"Missing value in {key} for {record['Load_ID']}")

    # Check for unexpected statuses
    print("\nUnexpected statuses:")

    allowed_statuses = ["Delivered", "In Transit", "Pending", "Cancelled"]

    for record in records_as_dicts:
        status = record["Status"]

        if status not in allowed_statuses:
            print(f"Unexpected status in {record['Load_ID']}: {status}")

    # Check for duplicate Load IDs
    print("\nDuplicate Load IDs:")

    seen_ids = set()

    for record in records_as_dicts:
        load_id = record["Load_ID"]

        if load_id in seen_ids:
            print(f"Duplicate Load ID found: {load_id}")
        else:
            seen_ids.add(load_id)

    # Check numeric values
    print("\nNumeric validation:")

    for record in records_as_dicts:
        quantity = record["Quantity_tonnes"]
        distance = record["Distance_km"]

        try:
            quantity = float(quantity)
            distance = float(distance)

            if quantity <= 0:
                print(
                    f"Invalid quantity for {record['Load_ID']}: "
                    f"{record['Quantity_tonnes']}")

            if distance <= 0:
                print(
                    f"Invalid distance for {record['Load_ID']}: "
                    f"{record['Distance_km']}")

        except ValueError:
            print(f"Non-numeric value found in record {record['Load_ID']}")

    # Check dates
    print("\nDate validation:")

    for record in records_as_dicts:
        date = record["Date"]

        try:
            datetime.strptime(date, "%Y-%m-%d")

        except ValueError:
            print(f"Invalid date in record {record['Load_ID']}: {date}")

    print("\n========== VALIDATION COMPLETE ==========")

def clean_status_values():
    print("\n========== CLEAN STATUS VALUES ==========")

    corrections = {
        "Delievered": "Delivered",
        "delivered": "Delivered"
        }

    corrections_made = 0

    for record in records_as_dicts:
        status = record["Status"]

        if status in corrections:
            old_status = record["Status"]
            new_status = corrections[status]

            record["Status"] = new_status
            corrections_made += 1

            print(f"Corrected {record['Load_ID']}: {old_status} -> {new_status}.")

    if corrections_made == 0:
        print("No correctable status values were found.")

    else:
        print(f"\n{corrections_made} status value(s) corrected.")

    print("========== STATUS CLEANING COMPLETE ==========")

def review_missing_values():
    print("\n========== MISSING VALUE REVIEW ==========")

    missing_found = False

    for record in records_as_dicts:
        for key, value in record.items():
            if value == "":
                print(f"Missing value found in {key} for {record['Load_ID']}")

                missing_found = True

    if not missing_found:
        print("No missing values found.")

    print("========== MISSING VALUE REVIEW COMPLETE ==========")

def clean_nummeric_values():
    print("\n========== NUMERIC VALUE REVIEW ==========")

    corrections_made = 0
    problems_found = 0

    for record in records_as_dicts:

        # Check Quantity
        try:
            quantity = float(record["Quantity_tonnes"])

            if quantity <= 0:
                print(f"Invalid quantity for {record['Load_ID']}: "
                      f"{record['Quantity_tonnes']}")

                problems_found += 1

            else:
                record["Quantity_tonnes"] = quantity
                corrections_made += 1

        except ValueError:
            print(f"Non-numeric quantity for {record['Load_ID']}: "
                  f"{record['Quantity_tonnes']}")

            problems_found += 1

        # Check Distance
        try:
            distance = float(record["Distance_km"])

            if distance <= 0:
                print(
                    f"Invalid distance for {record['Load_ID']}: "
                    f"{record['Distance_km']}")
                
                problems_found += 1
            else:
                record["Distance_km"] = distance
                corrections_made += 1

        except ValueError:
            print(
                f"Non-numeric distance for {record['Load_ID']}: "
                f"{record['Distance_km']}")
            
            problems_found += 1

    print(f"\nValid numeric values converted: {corrections_made}")
    print(f"Numeric problems found: {problems_found}")

    print("========== NUMERIC REVIEW COMPLETE ==========")

def review_invalid_dates():
    print("\n========== DATE REVIEW ==========")

    invalid_dates_found = 0

    for record in records_as_dicts:
        date = record["Date"]

        try:
            datetime.strptime(date, "%Y-%m-%d")

        except ValueError:
            print(
                f"Invalid date for {record['Load_ID']}: "
                f"{record['Date']}"
            )
            invalid_dates_found += 1

    if invalid_dates_found == 0:
        print("No invalid dates found.")

    else:
        print(f"\nInvalid dates found: {invalid_dates_found}")

    print("========== DATE REVIEW COMPLETE ==========")
        

def main():
    while True:
        print("\n========================================")
        print("           CSV DATA ANALYZER")
        print("========================================")
        print("1. Look up Load ID")
        print("2. Validation Quick Check")
        print("3. Clean Data")
        print("0. Quit")
        print("========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            lookup_load()

        elif choice == "2":
            validation_quick_check()

        elif choice == "3":
            while True:
                print("\n========== CLEAN DATA ==========")
                print("1. Clean Status Values")
                print("2. Review Missing Values")
                print("3. Clean Numeric Values")
                print("4. Review Invalid Dates")
                print("0. Return to Main Menu")
                print("================================")

                clean_choice = input("Enter your choice: ").strip()

                if clean_choice == "1":
                    clean_status_values()

                elif clean_choice == "2":
                    review_missing_values()

                elif clean_choice == "3":
                    clean_nummeric_values()

                elif clean_choice == "4":
                    review_invalid_dates()

                elif clean_choice == "0":
                    break

                else:
                    print(f"Invalid choice ({clean_choice}). Please enter 1 or 0.")

        elif choice == "0":
            print()
            print("Exiting CSV Data Analyzer. Good bye.")
            print()
            break

        else:
            print()
            print(f"Invalid choice ({choice}). Please enter a valid choice: 1, 2, or 0.")
            print()

main()




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





    




