def total_salary(path):
    """
    Обчислює загальну та середню заробітну плату з файлу.

    Файл повинен містити рядки з іменами співробітників та їхніми зарплатами, розділеними комою,
    наприклад: "Іван Петренко,5000".

    Args:
        path (str): Шлях до файлу, що містить дані про зарплату.

    Returns:
        tuple: Кортеж, що містить загальну зарплату (int) та середню зарплату (int).
               Повертає (0, 0), якщо файл не знайдено, неможливо прочитати або він не містить дійсних зарплат.
    """
    try:
        with open(path, encoding='utf-8') as file:
            salaries = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue  # пропускаємо некоректні рядки
                try:
                    salary = int(parts[1])
                    salaries.append(salary)
                except ValueError:
                    continue  # пропускаємо рядки з нечисловими зарплатами
            if not salaries:
                return (0, 0)
            total = sum(salaries)
            average = total // len(salaries)
            return (total, average)
    except (FileNotFoundError, OSError):
        return (0, 0)

if __name__ == "__main__":
    import sys

    # Default file path relative to the script's location (assuming execution from goit-pycore-hw-04)
    default_file_path = "salaries.txt"
    
    # Check if a file path is provided as a command-line argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = default_file_path

    total, average = total_salary(file_path)
    print(f"Total salary: {total}, Average salary: {average}")
