user_info = {
    "first_name": "Yaroslav",
    "last_name": "Krasnoperov",
    "age": 29,
    "skills": ["python", "fast_API", "sql"]
}


name = user_info.get("first_name1", "быдло")


for key, values in user_info.items():
    print(key, values)