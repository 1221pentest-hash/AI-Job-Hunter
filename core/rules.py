"""
AI Job Hunter
Job Scoring Rules
"""

# ==========================================================
# TITLE SCORES
# ==========================================================

TITLE_RULES = {
    # Highest Priority
    "it support": 50,
    "help desk": 50,
    "service desk": 50,
    "desktop support": 50,
    "technical support": 50,
    "support technician": 50,
    "field technician": 45,
    "deployment technician": 45,

    # Very Good
    "system administrator": 40,
    "systems administrator": 40,
    "junior system administrator": 45,
    "network technician": 35,
    "network support": 35,
    "it technician": 40,

    # Future Goals
    "cloud": 25,
    "azure": 25,
    "devops": 25,
    "linux": 20,

    # Lower Priority
    "security analyst": 15,
    "soc analyst": 15,
}

# ==========================================================
# SKILLS
# ==========================================================

SKILL_RULES = {
    "active directory": 12,
    "windows server": 12,
    "office 365": 10,
    "microsoft 365": 10,
    "entra": 10,
    "azure": 10,
    "powershell": 12,
    "dns": 8,
    "dhcp": 8,
    "tcp/ip": 8,
    "vpn": 8,
    "lan": 6,
    "wan": 6,
    "firewall": 6,
    "cisco": 6,
    "vmware": 8,
    "hyper-v": 8,
    "linux": 8,
    "docker": 8,
    "git": 5,
    "python": 6,
    "customer service": 10,
    "troubleshooting": 12,
    "hardware": 8,
    "printer": 5,
}

# ==========================================================
# PREFERRED COMPANIES
# ==========================================================

COMPANY_RULES = {
    "government": 15,
    "government of canada": 20,
    "city of ottawa": 20,
    "microsoft": 15,
    "ibm": 15,
    "cgi": 12,
    "bell": 10,
    "rogers": 10,
    "telus": 10,
}

# ==========================================================
# PENALTIES
# ==========================================================

PENALTY_RULES = {
    "senior": -20,
    "manager": -25,
    "director": -30,
    "sales": -20,
    "marketing": -20,
    "registered nurse": -100,
    "physician": -100,
    "driver": -40,
    "cook": -100,
    "chef": -100,
    "cashier": -100,
}