from database import get_connection, get_all_incidents
connection=get_connection()
#connection was successful so close it, it is only a connectivity check.
if connection:
    connection.close()
incidents=get_all_incidents()
print("Historical incidents are as follows:")
for incident in incidents:
    print(incident)
