# ==========================================
# AI Job Hunter Configuration
# ==========================================

# Application Information
APP_NAME = "AI Job Hunter"
VERSION = "1.0"
AUTHOR = "Israel Loyo"


# ==========================================
# Job Search Configuration
# ==========================================

JOB_KEYWORDS = [
    "IT Support",
    "Help Desk",
    "Desktop Support",
    "Technical Support",
    "Field Technician",
    "IT Technician",
    "Service Desk",
    "Junior System Administrator",
]

JOB_LOCATIONS = [
    "Ottawa",
    "Kanata",
    "Nepean",
    "Gatineau",
    "Remote",
    "Canada",
]


# ==========================================
# Scoring Configuration
# ==========================================

TITLE_MATCH_SCORE = 50
LOCATION_MATCH_SCORE = 25

REMOTE_BONUS = 15
CANADA_BONUS = 10

GOOD_WORD_BONUS = 20
BAD_WORD_PENALTY = 40

TARGET_COMPANIES = [
    "IBM",
    "Dell",
    "CGI",
    "Bell",
    "Nokia",
    "Cisco",
    "Ciena",
    "Fortinet",
]
GOOD_WORDS = [
    "junior",
    "entry",
    "associate",
    "support",
    "technician",
    "help desk",
]

BAD_WORDS = [
    "senior",
    "sr",
    "lead",
    "manager",
    "director",
    "principal",
    "architect",
    "staff",
]
PRIORITY_LOCATIONS = [
    "Ottawa",
    "Gatineau",
    "Kanata",
    "Nepean",
    "Orleans",
]

SECONDARY_LOCATIONS = [
    "Montreal",
    "Laval",
    "Toronto",
    "Kingston",
]

ALLOW_REMOTE = True
ALLOW_USA_REMOTE = False
ALLOW_LATAM_REMOTE = False