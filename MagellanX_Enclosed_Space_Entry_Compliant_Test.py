import csv,datetime  
from datetime import datetime,timedelta


def check_gas_testing_time_compliance() -> bool:
    
    EntFilePath=r'C:\Users\prash\Desktop\DE\entrant_gas_reading.csv'  #Provide path for entrant_gas_reading.csv
    PerFilePath=r'C:\Users\prash\Desktop\DE\Periodic_Reading.csv'   #Provide path for periodical_gas_reading.csv

    Entrant = {}  #Creating  a dict to store Entrant gas reading 
    Periodic = []  #Creating a list to store PEriodical gas reading 

##Read the entrant file and store in variable Dict Entrant
    EntFile = open(EntFilePath, 'r')
    EntDict = csv.DictReader(EntFile)
    for row in EntDict:
        Entrant = row
    
 ##Read the Periodic file and store in variable Periodic   
    PerFile = open(PerFilePath, 'r') 
    PerList = csv.reader(PerFile)
    P = list(PerList)
    for x in P:
        for y in x:
            Periodic.append(y)
    Periodic.pop(0) ##Removing Column name gas reading time from list


    complaint = False

    #Converting string to datetime format 
    exittime = datetime.strptime(Entrant['exit time'], "%Y-%m-%dT%H:%M:%S.%fZ")
    entrtime = datetime.strptime(Entrant['entry time'], "%Y-%m-%dT%H:%M:%S.%fZ")
    entrplus30mins = datetime.strptime(Entrant['entry time'], "%Y-%m-%dT%H:%M:%S.%fZ") + timedelta(minutes=30)
    diff = ((exittime - entrtime).total_seconds() / 60)

    
    if diff >= 30:  # Check if the CW is staying more than 30 mins
        if len(Periodic) > 0:  # checking if the periodic entry has values
            for x in Periodic:  # checking if periodic entry is in compliance
                if datetime.strptime(x,"%Y-%m-%dT%H:%M:%S.%fZ")>=entrtime and datetime.strptime(x,"%Y-%m-%dT%H:%M:%S.%fZ")<=entrplus30mins:
                    # checking if the periodic read time lies between Entry time and time less than 30 mins plus entry time
                    complaint = True
    
    if complaint is True:
        return True
    else:
        return False

if __name__ == "__main__":
    if check_gas_testing_time_compliance():
        print("Compliant")
    else:
        print("Not Compliant")
