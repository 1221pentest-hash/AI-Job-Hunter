"""
resume_data.py

Single Source of Truth for the user's professional profile.

This module contains only data.
No business logic should be added here.
"""


PROFILE = {
    "personal": {
        "name": "Israel Loyo",
        "location": "Montreal, Quebec, Canada",
    },

    "career": {
        "target_roles": [
            "IT Support Technician",
            "Help Desk Analyst",
            "Desktop Support Technician",
            "Technical Support Specialist",
            "Field Technician",
            "Junior Systems Administrator",
        ],

        "preferred_locations": [
            "Ottawa",
            "Kanata",
            "Nepean",
            "Gatineau",
            "Remote",
        ],

        "employment_type": [
            "Full-Time",
            "Hybrid",
            "Remote",
            "On-Site",
        ],
    },

    "certifications": [
        "CompTIA Security+",
        "Fortinet NSE 3",
        "Cybersecurity Analyst Diploma",
        "CCNA (In Progress)",
    ],

    "languages": [
        {
            "name": "English",
            "level": "Professional",
        },
        {
            "name": "French",
            "level": "B2",
        },
        {
            "name": "Spanish",
            "level": "Native",
        },
    ],

    "skills": {

        "operating_systems": [
            {
                "name": "Windows 10",
                "level": "Advanced",
                "source": "Professional Training",
            },
            {
                "name": "Windows 11",
                "level": "Advanced",
                "source": "Professional Training",
            },
            {
                "name": "Windows Server 2022",
                "level": "Intermediate",
                "source": "Enterprise Home Lab",
            },
            {
                "name": "Linux",
                "level": "Intermediate",
                "source": "DevOps Labs",
            },
        ],

        "microsoft": [
            {
                "name": "Active Directory",
                "level": "Intermediate",
                "source": "Enterprise Home Lab",
            },
            {
                "name": "Group Policy",
                "level": "Intermediate",
                "source": "Enterprise Home Lab",
            },
            {
                "name": "DNS",
                "level": "Intermediate",
                "source": "Enterprise Home Lab",
            },
            {
                "name": "DHCP",
                "level": "Intermediate",
                "source": "Enterprise Home Lab",
            },
            {
                "name": "Microsoft 365",
                "level": "Learning",
                "source": "Self Study",
            },
            {
                "name": "Entra ID",
                "level": "Learning",
                "source": "Azure Learning",
            },
        ],

        "networking": [
            {
                "name": "TCP/IP",
                "level": "Intermediate",
                "source": "CCNA",
            },
            {
                "name": "LAN/WAN",
                "level": "Intermediate",
                "source": "CCNA",
            },
            {
                "name": "VPN",
                "level": "Intermediate",
                "source": "CCNA",
            },
            {
                "name": "Cisco",
                "level": "Intermediate",
                "source": "CCNA",
            },
        ],

        "virtualization": [
            {
                "name": "VMware Workstation",
                "level": "Intermediate",
                "source": "Enterprise Home Lab",
            },
            {
                "name": "Virtual Machines",
                "level": "Intermediate",
                "source": "Enterprise Home Lab",
            },
        ],

        "security": [
            {
                "name": "Wazuh",
                "level": "Learning",
                "source": "SOC Lab",
            },
            {
                "name": "Firewall",
                "level": "Intermediate",
                "source": "Security Labs",
            },
        ],

        "scripting": [
            {
                "name": "Python",
                "level": "Learning",
                "source": "AI Job Hunter",
            },
            {
                "name": "PowerShell",
                "level": "Learning",
                "source": "Enterprise Home Lab",
            },
        ],

        "tools": [
            {
                "name": "Docker",
                "level": "Intermediate",
                "source": "DevOps Labs",
            },
            {
                "name": "Git",
                "level": "Intermediate",
                "source": "GitHub Projects",
            },
            {
                "name": "GitHub",
                "level": "Intermediate",
                "source": "Portfolio",
            },
            {
                "name": "VS Code",
                "level": "Advanced",
                "source": "Daily Development",
            },
        ],
    },

    "projects": [
        "AI Job Hunter",
        "Enterprise Active Directory Home Lab",
        "Docker Administration Labs",
        "SOC Home Lab",
    ],

    "soft_skills": [
        "Troubleshooting",
        "Customer Service",
        "Communication",
        "Problem Solving",
        "Documentation",
        "Time Management",
    ],
}