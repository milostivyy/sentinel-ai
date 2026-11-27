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

new_incidents = [
    # Network
    {
        "description": "Unable to establish VPN connection after network restart",
        "category": "Network"
    },
    {
        "description": "Corporate network becomes unreachable intermittently",
        "category": "Network"
    },
    {
        "description": "DNS resolution fails for internal company domains",
        "category": "Network"
    },

    # Authentication
    {
        "description": "User receives unauthorized access error despite valid credentials",
        "category": "Authentication"
    },
    {
        "description": "Multi-factor authentication code is not being accepted",
        "category": "Authentication"
    },
    {
        "description": "User account gets locked immediately after login",
        "category": "Authentication"
    },

    # Application
    {
        "description": "Web application crashes when opening the dashboard",
        "category": "Application"
    },
    {
        "description": "Application returns HTTP 500 error during form submission",
        "category": "Application"
    },
    {
        "description": "Application freezes when uploading large files",
        "category": "Application"
    },
    {
        "description": "Users cannot download reports from the application",
        "category": "Application"
    },

    # Database
    {
        "description": "PostgreSQL database connection timeout during requests",
        "category": "Database"
    },
    {
        "description": "SQL queries are taking unusually long to execute",
        "category": "Database"
    },
    {
        "description": "Database connection pool reaches maximum capacity",
        "category": "Database"
    },
    {
        "description": "Database transaction fails due to deadlock",
        "category": "Database"
    },

    # Cloud and Infrastructure
    {
        "description": "Azure virtual machine becomes unreachable",
        "category": "Cloud"
    },
    {
        "description": "Application deployment fails due to container startup error",
        "category": "Cloud"
    },
    {
        "description": "Azure storage account returns access denied errors",
        "category": "Cloud"
    },

    # Performance
    {
        "description": "Production server experiences unusually high CPU utilization",
        "category": "Performance"
    },
    {
        "description": "API response time increases significantly under load",
        "category": "Performance"
    },
    {
        "description": "Laptop performance degrades when multiple applications run",
        "category": "Performance"
    }
]

insert_incidents(incidents)
print("Incidents inserted successfully!")
insert_incidents(new_incidents)
print("New incidents inserted successfully!")
