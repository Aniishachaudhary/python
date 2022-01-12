print("Swallow Speed Analysis: Version 1.0")

def validate_readings(reading): 
    """This function is used to check the email"""
    if (reading[0].capitalize() == "U" or reading[0].capitalize() == "E"): # this line convert inital word into capital form and check whether it is equall or not          
        return True
    else:
        return False

def convert_e_u(reading):
    """This function returns float values"""
    if reading[0].lower() == "u":# changing the giebn data into lower case and caomparig it
        return float(reading[1:])
    elif reading[0].lower() == "e":#lower will change upper case into lower case
        return float(reading[1:])/1.60934

def convert_miles_km(x):
    """This function used for calculations"""
    return x * 1.60934

dataset = []#empty set

while True:
    reading = input("Enter the next reading : ")
    
    if reading == "":
        break
    elif validate_readings(reading) == True: #calling the function Validdata in the above 
        print("Reading saved.")

        if reading[0].capitalize() == "E":
            dataset.append(convert_e_u(reading))#adding the data into empty set
        else:
            dataset.append(float(reading[1:]))
    elif validate_readings(reading) == False:#cassing the validate_readings(reading) and checking wether the data is true or false 
        print("Invalid Input!")
        
if dataset == []:
    print("No readings. Nothing to do.")
    exit()
else:
    print("Reading summary")
    if len(dataset)==1:
        print(f"{len(dataset)} Reading Analysed.")
    else:
        print(f"{len(dataset)} Readings Analysed.")

print(dataset)
max_reading_in_miles = max(dataset)
max_reading_in_km = convert_miles_km(max_reading_in_miles)
min_reading_in_miles = min(dataset)
min_reading_in_km = convert_miles_km(min_reading_in_miles)

average_reading_in_miles = sum(dataset)/len(dataset)#calculating average
average_reading_in_km = convert_miles_km(average_reading_in_miles)

print("max speed :{:.1f} MPH {:.1f} KPH ".format(max_reading_in_miles,max_reading_in_km))
print("max avg :  {:.1f} MPH {:.1f} KPH ".format(average_reading_in_miles,average_reading_in_km))
print("min speed :{:.1f} MPH {:.1f} KPH ".format(min_reading_in_miles,min_reading_in_km))