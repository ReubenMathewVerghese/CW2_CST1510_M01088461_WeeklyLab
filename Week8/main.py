import app.data.schema as schema
import app.data.incidents as incidents
import app.data.tickets as tickets
import app.data.datasets as datasets

def PromptForCRUD(tableName: str) -> None:
    userInp: int = int(input(f"1) CREATE {tableName}\n2) READ {tableName}\n3) UPDATE {tableName}\n4) DELETE {tableName}\n"))
    match userInp:
        case 1:
            insertrow()
        case 2:
            readrow()
        case 3:
            updaterow()
        case 4:
            deleterow()
        case _:
            print("WRONG INPUT")

def tablename() -> str:
    userInp: int = int(input("1) Cyber_Incidents\n2) IT_Tickets\n3) Datasets_Metadata\n"))
    match userInp:
        case 1:
            return "Cyber_Incidents"
        case 2:
            return "IT_Tickets"
        case 3:
            return "Datasets_Metadata"
        case _:
            return "WRONG INPUT"

def insertrow():
    match tableName: 
        case "Cyber_Incidents":
            date_of_incident = input("Enter date: ")
            incident_type = input("Enter incident type: ")
            severity_level: str = input("Enter severity: ")
            current_status: str = input("Enter status: ")
            
            incidents.insert_incident(date_of_incident, incident_type, severity_level, current_status)
            
        case "IT_Tickets":
            ticket_identifier = input("Enter ticket id: ")
            ticket_subject = input("Enter subject: ")
            priority_level = input("Enter priority: ")
            ticket_status = input("Enter status: ")
            created_date = input("Enter created date: ")
            
            tickets.insert_ticket(ticket_identifier, ticket_subject, priority_level, ticket_status, created_date)
            
        case "Datasets_Metadata":
            dataset_name = input("Enter dataset name: ")
            dataset_category = input("Enter category: ")
            file_size_mb = input("Enter file size (MB): ")
            
            datasets.insert_metadata(dataset_name, dataset_category, file_size_mb)

def readrow():
    id = int(input("Enter id: "))
    match tableName:
        case "Cyber_Incidents":
            print(incidents.getallincidents(f"id = {id}"))
        case "IT_Tickets":
            print(tickets.getalltickets(f"ticket_id = {id}"))
        case "Datasets_Metadata":
            print(datasets.getalldatasets(f"id = {id}"))

def updaterow():
    record_identifier = input("Enter id: ")
    match tableName:
        case "Cyber_Incidents":
            new_id = input("Enter new id: ")
            date_of_incident = input("Enter date: ")
            incident_type = input("Enter incident type: ")
            severity_level: str = input("Enter severity: ")
            current_status: str = input("Enter status: ")
            
            incidents.update_incident(record_identifier, new_id, date_of_incident, incident_type, severity_level, current_status)
            
        case "IT_Tickets":
            new_ticket_id = input("Enter new ticket id: ")
            ticket_subject = input("Enter subject: ")
            priority_level = input("Enter priority: ")
            ticket_status = input("Enter status: ")
            created_date = input("Enter created date: ")
            
            tickets.update_ticket(record_identifier, new_ticket_id, ticket_subject, priority_level, ticket_status, created_date)
            
        case "Datasets_Metadata":
            new_dataset_id = input("Enter new dataset id: ")
            dataset_name = input("Enter dataset name: ")
            dataset_category = input("Enter category: ")
            file_size_mb = input("Enter file size (MB): ")
            
            datasets.update_metadata(record_identifier, new_dataset_id, dataset_name, dataset_category, file_size_mb)

def deleterow():
    id =input("Enter id: ")
    match tableName:
        case "Cyber_Incidents":
            incidents.delete_incident(id)
        case "IT_Tickets":
            tickets.delete_ticket(id)
        case "Datasets_Metadata":
            datasets.delete_metadata(id)

if __name__ == "__main__":
    schema.create_all_tables()
    tableName = tablename()
    PromptForCRUD(tableName)