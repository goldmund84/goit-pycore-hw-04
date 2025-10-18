def get_cats_info(path):
    """
    Читає файл з інформацією про котів та повертає список словників.

    Кожен рядок файлу повинен містити унікальний ідентифікатор кота, його ім'я та вік,
    розділені комою. Наприклад: "60b90c1c13067a15887e1ae1,Tayson,3".

    Args:
        path (str): Шлях до текстового файлу з даними про котів.

    Returns:
        list: Список словників, де кожен словник містить інформацію про одного кота
              з ключами "id", "name", "age". Повертає порожній список у разі помилки
              читання файлу або якщо файл порожній/некоректний.
    """
    cats_info = []
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_dict = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats_info.append(cat_dict)
    except (FileNotFoundError, OSError):
        print(f"Помилка: Файл за шляхом '{path}' не знайдено або неможливо прочитати.")
        return []
    return cats_info

if __name__ == "__main__":
    # Assuming the script is executed from the goit-pycore-hw-04 directory
    file_path = "cats_file.txt"
    cats_info = get_cats_info(file_path)
    print(cats_info)
