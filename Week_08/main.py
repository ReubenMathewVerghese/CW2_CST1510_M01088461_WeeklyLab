import app.data.schema as schema
import app.data.incidents as incidents
import app.data.tickets as tickets
import app.data.datasets as datasets


def prompt_for_crud(table_name: str) -> None:
    user_inp: int = int(input(f"1) CREATE {table_name}\n2) READ {table_name}\n3) UPDATE {table_name}\n4) DELETE {table_name}\n"))
    match user_inp:
        case 1:
            create_row()
        case 2:
            read_row()
        case 3:
            update_row()
        case 4:
            delete_row()
        case _:
            print("WRONG INPUT")


def get_table_name() -> str:
    user_inp: int = int(input("1) Cyber_Incidents\n2) IT_Tickets\n3) Datasets_Metadata\n"))
    match user_inp:
        case 1:
            return "Cyber_Incidents"
        case 2:
            return "IT_Tickets"
        case 3:
            return "Datasets_Metadata"
        case _:
            return "WRONG INPUT"


def create_row():
    match table_name: #type: ignore
        case "Cyber_Incidents":
            date = input("Enter date: ")
            incident_name = input("Enter incident name: ")
            severity: str = input("Enter severity: ")
            status: str = input("Enter status: ")
            incidents.insert_incident(date, incident_name, severity, status)
        case "IT_Tickets":
            id = input("Enter ticket id: ")
            sub = input("Enter subject ")
            prio = input("Enter priority:  ")
            status = input("Enter status: ")
            cr_date = input("Enter created date: ")
            tickets.insert_ticket(id, sub, prio, status, cr_date)
        case "Datasets_Metadata":
            id = input("Enter ticket id: ")
            name = input("Enter name ")
            ctgry = input("Enter ctgry: ")
            file_size = input("Enter file_size: ")
            datasets.insert_dataset(id, name, ctgry, file_size)


def read_row():
    id = int(input("Enter id: "))
    match table_name:
        case "Cyber_Incidents":
            print(incidents.get_all_incidents(f"id = {id}"))
        case "IT_Tickets":
            print(tickets.get_all_tickets(f"ticket_id = {id}"))
        case "Datasets_Metadata":
            print(datasets.get_all_datasets(f"id = {id}"))


def update_row():
    id = input("Enter id: ")
    match table_name:
        case "Cyber_Incidents":
            new_id = input("Enter new id: ")
            date = input("Enter date: ")
            incident_name = input("Enter incident name: ")
            severity: str = input("Enter severity: ")
            status: str = input("Enter status: ")
            incidents.update_incident(id, new_id, date, incident_name, severity, status)
        case "IT_Tickets":
            new_id = input("Enter ticket id: ")
            sub = input("Enter subject ")
            prio = input("Enter priority:  ")
            status = input("Enter status: ")
            cr_date = input("Enter created date: ")
            tickets.update_ticket(id, new_id, sub, prio, status, cr_date)
        case "Datasets_Metadata":
            new_id = input("Enter ticket id: ")
            name = input("Enter name ")
            ctgry = input("Enter ctgry: ")
            file_size = input("Enter file_size: ")
            datasets.update_datasets(id, new_id, name, ctgry, file_size)


def delete_row():
    id = input("Enter id: ")
    match table_name:
        case "Cyber_Incidents":
            incidents.delete_incident(id)
        case "IT_Tickets":
            tickets.delete_ticket(id)
        case "Datasets_Metadata":
            datasets.delete_dataset(id)


if __name__ == "__main__":
    schema.create_all_tables()
    table_name: str = get_table_name()
    prompt_for_crud(table_name)