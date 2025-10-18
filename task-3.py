import sys
from pathlib import Path
from colorama import Fore, Style, init

def visualize_directory(path, indent=0):
    """
    Візуалізує структуру директорії, виводячи імена піддиректорій та файлів
    з кольоровим форматуванням.

    Args:
        path (Path): Об'єкт Path, що вказує на директорію для візуалізації.
        indent (int): Рівень відступу для візуального представлення ієрархії.
    """
    if not path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{path}' не існує.{Style.RESET_ALL}")
        return
    if not path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{path}' не є директорією.{Style.RESET_ALL}")
        return

    prefix = "  " * indent
    
    for item in path.iterdir():
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
            visualize_directory(item, indent + 1)
        else:
            print(f"{prefix}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")

if __name__ == "__main__":
    init(autoreset=True) # Ініціалізація colorama для автоматичного скидання кольорів

    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Використання: python3 task-3.py <шлях_до_директорії>{Style.RESET_ALL}")
        sys.exit(1)

    target_path = Path(sys.argv[1])
    visualize_directory(target_path)
