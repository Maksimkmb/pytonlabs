import datetime


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DataBase(metaclass=SingletonMeta):
    def __init__(self):
        self.info = []

    def display_database(self):
        with open("database.csv", "r") as file:
            for line in file:
                print(line.strip())

    def write_to_file(self):
        with open("database.csv", "w") as file:
            for car in self.info:
                file.write(f"{car.brand},{car.model},{car.year},{car.colour}\n")

    def add_entry(self, start_id):
        brand, model, year, colour = self.get_user_input_for_car()
        car = Auto(brand, model, year, colour, start_id)
        self.info.append(car)
        self.write_to_file()

    def get_user_input_for_car(self):
        brand = input("Enter the brand of the car: ")
        model = input("Enter the model of the car: ")
        year = int(input("Enter the year of the car: "))
        colour = input("Enter the colour of the car: ")

        if not (0 <= year <= datetime.datetime.now().year):
            print("Invalid year.")
            return self.get_user_input_for_car()

        return brand, model, year, colour

    def update_entry(self, car_id):
        car = self.find_entry_by_id(car_id)
        if car:
            field_to_change = input("Enter the field you want to change: ")
            if field_to_change != "id":
                new_value = input(f"Enter new value for {field_to_change}: ")
                setattr(car, field_to_change, new_value)
                self.write_to_file()
            else:
                print("You cannot change the 'id' field.")
        else:
            print("Car not found.")

    def find_entry_by_id(self, car_id):
        for car in self.info:
            if car.id == car_id:
                return car
        return None

    def delete_entry(self, car_id):
        car = self.find_entry_by_id(car_id)
        if car:
            self.info.remove(car)
            self.write_to_file()
            print("Car removed.")
        else:
            print("Car not found.")

    def search_by_criterion(self):
        param = input("Enter parameter to search by: ")
        value = input(f"Enter value for {param}: ")
        result = self.find_entry_by_param(param, value)
        if result:
            print(result.id, result.brand, result.model, result.year, result.colour)
        else:
            print("No matching cars found.")

    def find_entry_by_param(self, param, value):
        for car in self.info:
            if getattr(car, param) == value:
                return car
        return None

    def sort_by_criterion(self):
        param = input("Enter parameter to sort by: ")
        if param in ["brand", "model", "year", "colour"]:
            self.info.sort(key=lambda x: getattr(x, param))
            self.write_to_file()
        else:
            print("Invalid parameter for sorting.")

    def display_statistics(self):
        years = [car.year for car in self.info]
        if years:
            avg_year = sum(years) / len(years)
            print("Average year:", round(avg_year, 2))
        else:
            print("No cars in the database.")


class Auto:
    def __init__(self, brand, model, year, colour, id):
        self.brand = brand
        self.model = model
        self.year = year
        self.colour = colour
        self.id = id


database_obj = DataBase()

while True:
    print(
        "1) Display Database\n2) Add Entry to Database\n3) Update an Entry\n4) Delete an Entry\n5) Search by Criterion\n6) Sort by Criterion\n7) Display Statistics\n8) Exit\n"
    )

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid choice.")
        continue

    match choice:
        case 1:
            database_obj.display_database()
        case 2:
            start_id = max([car.id for car in database_obj.info]) + 1 if database_obj.info else 1
            database_obj.add_entry(start_id)
        case 3:
            car_id = int(input("Enter the car number you want to update: "))
            database_obj.update_entry(car_id)
        case 4:
            car_id = int(input("Enter the car number you want to delete: "))
            database_obj.delete_entry(car_id)
        case 5:
            database_obj.search_by_criterion()
        case 6:
            database_obj.sort_by_criterion()
        case 7:
            database_obj.display_statistics()
        case 8:
            exit()
        case _:
            print("Enter a valid choice.")
