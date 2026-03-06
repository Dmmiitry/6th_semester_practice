class Worker:
    def __init__(self, surname_and_initial='', position='', salary=0, year_of_employment=0):
        self.surname_and_initial = surname_and_initial
        self.position = position
        self.salary = salary
        self.year_of_employment = year_of_employment

    # Метод для вывода информации о сотруднике
    def display(self):
        print(f'Фамилия и инициалы: {self.surname_and_initial}')
        print(f'Занимаемая должность: {self.position}')
        print(f'Зарплата: {self.salary}')
        print(f'Год приема на работу: {self.year_of_employment}')
    
    # Изменение значений полей
    def update_salary(self, new_salary):
        self.salary = new_salary

# Основная программа
if __name__ == "__main__":
    workers_list = []
    while True:
        try:
            n = int(input("Введите количество сотрудников: "))
            break
        except ValueError:
            print("Некорректный ввод")
            
    for i in range(n):
        surname_and_initial = input(f"Введите фамилию и инициалы сотрудника {i+1}: ")
        position = input(f"Введите должность сотрудника {i+1}: ")
        salary = float(input(f"Введите зарплату сотрудника {i+1}: "))
        year_of_employment = int(input(f"Введите год приёма на работу сотрудника {i+1}: "))
        
        worker = Worker(surname_and_initial, position, salary, year_of_employment)
        workers_list.append(worker)

    work_experience_years = int(input("Введите минимальное число лет стажа: "))
    current_year = 2025
    found_workers = False
    
    for w in workers_list:
        years_worked = current_year - w.year_of_employment
        if years_worked > work_experience_years:
            w.display()
            found_workers = True
    
    if not found_workers:
        print("Нет сотрудников с таким стажем.")