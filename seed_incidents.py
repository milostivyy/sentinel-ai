#seed incidents into databse directly from here

from database import insert_incidents
incidents=[
    {
        "description": "VPN disconnects every few minutes",
        "category": "Network"
    },
    {
        "description": "Cannot access internal company resources",
        "category": "Network"

    },
    {
        "description": "Login fails despite correct password",
        "category": "Authentication"

    },
    {
        "description": "Account locked after multiple attempts",
        "category": "Authentication"
    },
    {
        "description": "Application freezes during startup",
        "category": "Application"
    }

]
insert_incidents(incidents)
print("Incidents inserted successfully!")
