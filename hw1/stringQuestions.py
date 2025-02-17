def prob1():
    print("---Problem 1---")
    name = input("Enter your name: ")
    birth_year = int(input("Enter the year which you were born: "))
    print(f"{name}, your age is {2025-birth_year}.")

def prob2():
    print("---Problem 2---")
    txt = "LMaasleitbtui"
    car1 = txt[::2]
    car2 = txt[1::2]
    print(f"1st car is {car1} and the 2nd one is {car2}")

def prob3():
    print("---Problem 3---")
    in_st = str(input("Enter a string: "))
    print(f"Length of the string {in_st}: {len(in_st)}"
          f"\n{in_st} in lowercase: {in_st.lower()}"
          f"\n{in_st} in uppercase: {in_st.upper()}")

def prob4():
    print("---Problem 4---")
    text = input("Enter a string: ")
    text = text.lower()
    return text == text[::-1]

def prob5():
    print("---Problem 5---")
    text = input("Enter a string: ").lower()
    vowels = "aeiou"
    # 1st way
    count_v = sum(1 for char in text if char in vowels)
    count_c = sum(1 for char in text if char.isalpha() and char not in vowels)
    print(f"Vowels: {count_v} \nConsonants: {count_c}")
    # 2nd way
    # count_v = 0
    # count_c = 0
    # for char in text:
    #     if(char in vowels):
    #         count_v += 1
    #     else:
    #         count_c += 1
    # print(f"Vowels: {count_v} \nConsonants: {count_c}")

def prob6():
    print("---Problem 6---")
    text = input("Enter a string: ").lower()
    part = input("Enter a sub string to check: ").lower()
    return part in text

def prob7():
    print("---Problem 7---")
    sentence = input("Enter a sentence: ")
    old_word = input("Enter the word you want to change: ")
    new_word = input("Enter the new word: ")
    print(sentence.replace(old_word, new_word))

def prob8():
    print("---Problem 8---")
    text = input("Enter a string: ")
    print(f"first char: {text[0]} \nlast char: {text[-1]}")

def prob9():
    print("---Problem 9---")
    text = input("Enter a string: ")
    print(f"reversed string: {text[::-1]}")

def prob10():
    print("---Problem 10---")
    sentence = input("Enter a sentence: ")
    print(f"Number of words: {len(sentence.split())}")

def prob11():
    print("---Problem 11---")
    text = input("Enter anything: ")
    return any(char.isdigit() for char in text)

def prob12():
    print("---Problem 12---")
    words = []
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        words.append(word)

    str = words[0]
    for i in words:
        if i == words[0]:
            continue
        str += f"-{i}"
    print(str)

def prob13():
    print("---Problem 13---")
    text = input("Enter a sentence: ")
    print(text.replace(' ', ''))

def prob14():
    print("---Problem 14---")
    str1 = input("Enter the 1st string: ")
    str2 = input("Enter the 2nd string: ")
    print(str1 == str2)

def prob15():
    print("---Problem 15---")
    text = input("Enter a sentence: ")
    str = ""
    for i in text.split():
        str += i[0].upper()
    print(f"Acronym: {str}")

def prob16():
    print("---Problem 16---")
    st = input("Enter a string: ")
    char = input("Enter a char: ")
    print(st.replace(char, ''))

def prob17():
    print("---Problem 17---")
    st = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    new_st = "".join("*" if ch in vowels else ch for ch in st)
    print(new_st)

def prob18():
    print("---Problem 18---")
    text = input("Enter a sentence: ")
    word1 = input("Enter the starting word: ")
    word2 = input("Enter the ending word: ")
    return text.startswith(word1) and text.endswith(word2)

def main2():
    print("String Questions: ")
    prob1()
    prob2()
    prob3()
    print(prob4())
    prob5()
    print(prob6())
    print(prob7())
    prob8()
    prob9()
    prob10()
    print(prob11())
    prob12()
    prob13()
    prob14()
    prob15()
    prob16()
    prob17()
    print(prob18())
