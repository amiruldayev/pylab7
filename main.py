import random


def task1():
    print("\t\t\t\t\tTask 1")
    def read_and_display_text_file(file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    print(line.strip())
        except:
            print("File not found")
    file_path = 'text1.txt'
    read_and_display_text_file(file_path)

def task2():
    print("\t\t\t\t\tTask 2")
    def read_random_line(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if lines:
                    random_line = random.choice(lines)
                    print(random_line.strip())
                else:
                    print("Error")
        except:
            print("Error")
    file_path = 'text2.txt'
    read_random_line(file_path)



def task3():
    print("\t\t\t\t\tTask 3")
    def count_uppercase_characters(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                uppercase_count = sum(1 for char in content if char.isupper())
                print(f"uppercase characters: {uppercase_count}")
        except:
            print("Error")
    file_path = 'text1.txt'
    count_uppercase_characters(file_path)




def task4():
    print("\t\t\t\t\tTask 4")

    def count_lines_not_starting_with_D(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                lines_without_D = [line.strip() for line in lines if not line.startswith('D')]
                count = len(lines_without_D)
                print(f"D: {count}")
        except :
            print("Error")

    file_path = 'text4.txt'
    count_lines_not_starting_with_D(file_path)


def task5():
    print("\t\t\t\t\tTask 5")
    def count_words_ending_with_F(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                words = content.split()
                words_ending_with_F = [word.strip(".,!?") for word in words if word.lower().endswith('f')]
                count = len(words_ending_with_F)
                print(f"end with 'F': {count}")
        except:
            print("Error")

    file_path = 'text5.txt'
    count_words_ending_with_F(file_path)


def task6():
    print("\t\t\t\t\tTask 6")
    def count_all_and_none_words(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                words = content.split()
                count_all = words.count("all")
                count_none = words.count("none")
                print(f"all: {count_all}")
                print(f"none: {count_none}")
        except :
            print(f"Error")
    file_path = 'text6.txt'
    count_all_and_none_words(file_path)


def task7():
    print("\t\t\t\t\tTask 7")

    def count_word_frequency(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read().lower()
                content = ''.join(char for char in content if char.isalnum() or char.isspace())

                words = content.split()
                word_frequency = {}

                for word in words:
                    word_frequency[word] = word_frequency.get(word, 0) + 1

                for word, count in word_frequency.items():
                    print(f"{word}: {count}")
        except:
            print("Error")
    file_path = 'text6.txt'
    count_word_frequency(file_path)


def task8():
    print("\t\t\t\t\tTask 8")

    def find_longest_word(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()

                content = ''.join(char for char in content if char.isalnum() or char.isspace())

                words = content.split()

                longest_word = max(words, key=len)

                print(f"longest:{longest_word}")
        except :
            print("Error")
    file_path = 'text6.txt'
    find_longest_word(file_path)

def task9():
    print("\t\t\t\t\tTask 9")
    def correct_characters(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                corrected_content = content.replace('b', 'j')
                print(corrected_content)
        except :
            print("Error")
    file_path = 'text9.txt'
    correct_characters(file_path)


def task10():
    print("\t\t\t\t\tTask 10")

    def count_occurrences(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                count_A = content.lower().count('a')
                count_B = content.lower().count('b')

                print(f"A: {count_A}")
                print(f"B: {count_B}")
        except:
            print("Error")

    file_path = 'text9.txt'
    count_occurrences(file_path)


task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()
task9()
task10()