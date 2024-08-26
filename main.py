"""
This script provides personal information and generates a greeting
based on gender.
"""

# Personal information
NAME_F = "Андрій"
NAME_L = "Яцура"
AGE = "14"
PETS = "кіт і пес"
CITY = "Требіч"
IAY = (
    "дружелюбний тихий люблю по іграти в ігри (csgo,minecraft...) "
    "хочу навчатися програмуваню і тд"
)

# Display personal information
print("Мене звати")
print(NAME_F, NAME_L)
print(f"Мені {AGE} років")
print(f"У мене є {PETS}, і я їх люблю")
print(f"Живу у {CITY}, хоча я жив в Україні в Закарпаті")
print(f"Інформація про мене: {IAY}...")

# Greeting based on gender
FIRST_NAME = "Ivan"
LAST_NAME = "Ivanov"
GENDER = "man"

if GENDER == "man":
    SEX = "Пане"
else:
    SEX = "Пані"

NEW = f"{SEX} {FIRST_NAME} {LAST_NAME}"
print(NEW)
