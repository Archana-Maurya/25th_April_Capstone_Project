def create_ticket(issue):
    return {
        "ticket_id": "T101",
        "status": "Ticket Created Successfully",
        "issue": issue
    }


print(create_ticket("Order delayed"))