first_name = input("Enter first name:")
last_name = input("Enter last name:")
section = input("Enter section:")
fav_subject = input("Enter favorite subject:")

full_name = f"{first_name} {last_name}".title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_subject = fav_subject.title()
character_count = len(full_name)

print("\nFormatted Output:")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {formatted_section}")
print(f"Favorite Subject: {formatted_subject}")
print(f"Character Count: {character_count}")

