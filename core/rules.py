"""
AI Job Hunter
Job Scoring Rules
"""

# ==========================================================
# TITLE SCORES
# ==========================================================

TITLE_RULES = {
    # Highest Priority
    "it support": 25,
    "help desk": 25,
    "service desk": 25,
    "desktop support": 25,
    "technical support": 25,
    "support technician": 25,
    "field technician": 22,
    "deployment technician": 22,

    # Very Good
    "system administrator": 20,
    "systems administrator": 20,
    "junior system administrator": 25,
    "network technician": 18,
    "network support": 18,
    "it technician": 20,

    # Future Goals
    "cloud": 12,
    "azure": 12,
    "devops": 12,
    "linux": 10,

    # Lower Priority
    "security analyst": 10,
    "soc analyst": 10,
}

# ==========================================================
# SKILL SCORES
# ==========================================================

SKILL_RULES = {
    "active directory": 10,
    "windows server": 10,
    "office 365": 8,
    "microsoft 365": 8,
    "entra": 8,
    "azure": 8,
    "powershell": 10,
    "dns": 6,
    "dhcp": 6,
    "tcp/ip": 6,
    "vpn": 6,
    "lan": 5,
    "wan": 5,
    "firewall": 5,
    "cisco": 5,
    "vmware": 6,
    "hyper-v": 6,
    "linux": 6,
    "docker": 6,
    "git": 4,
    "python": 5,
    "customer service": 8,
    "troubleshooting": 10,
    "hardware": 6,
    "printer": 4,
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