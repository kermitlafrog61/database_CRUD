def check_title(db: dict, title: str) -> (None | ValueError):
    if title not in db:
        raise ValueError('Такого товара нет')
    
def create(db: dict, title: str, price: float):
    if title not in db:
        db[title] = price
    else:
        print('Товар с таким с названием уже существует')

def read_database(db: dict, title: str=None) -> (dict | int):
    if title != None:
        check_title(db, title)    
        return db[title]
    else:
        return db

def update(db: dict, title: str, price: float):
    check_title(db, title)
    db[title] = price

def delete(db: dict, title: str):
    check_title(db, title)
    db.pop(title)

# {'apple': 80}