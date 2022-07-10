from PetHome import Cat

cats = [
    {
        "name": "Барон",
        "age": "2",
        "gender":"Мальчик"
    },
    {
        "name": "Сэм",
        "age": "2",
        "gender":"Мальчик"
    }
]

for cat in cats:
    i = Cat(name = cat.get("name"),
            gender = cat.get("gender"),
            age = cat.get("age"))
    print(f'Имя: {i.name}, '
          f'возраст: {i.age} года, '
          f'пол: {i.gender}')