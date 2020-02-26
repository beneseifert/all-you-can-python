import os
import io


def show_recipes():
    folder = "./rezepte/"
    files = os.listdir(folder)
    for file_name in files:
        try:
            with io.open(folder + file_name, 'r', encoding='utf-8') as file:
                print(file_name)
                print("Zutaten:")
                print(file.read())
                print("\n")
        except FileNotFoundError:
            pass


show_recipes()
