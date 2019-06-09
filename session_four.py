
# Exercice 1
 data = []
 num = input("Enter an integer ('q' to quit): ")
 while num != 'q':
     data.append(int(num))
     num = input("Enter an integer ('q' to quit): ")
 data.sort()
 print("The values, sorted into ascending order are:")
 for element in data:
     print(element)

 # Exercice 2

 def main() :
  	year = int(input('enter a year'))
  	animals = ["monkey","rooster","dog","pig","rat","ox","tiger","rabbit","dragon","snake","horse","sheep"]
  	print(year, "is", animals[year % 12])
# main()

 # Exercice 3

 import random

 random_list = [random.choice(list(range(1, 100))) for i in range(10)]

 def get_min_index(any_list):
     print("the min is", min(any_list))
     print("its index is", random_list.index(min(random_list)))

 print(random_list)
 get_min_index(random_list)

# # Exercice 4

 def main():
     s = input("Enter numbers: ") 
     items = s.split()
     numbers = [int(x) for x in items]
     print("The distinct numbers are:", eliminateDuplicates(numbers))

 def eliminateDuplicates(list):
     result = [] 
     for element in list:
         if not (element in result):
             result.append(element)
     return result

 main()


# exercice 5 anagrams

def main():
    s1 = input("Enter the first string: ").strip()
    s2 = input("Enter the second string: ").strip()
    print(s1, "and", s2, "are", ("anagrams." if isAnagram(s1, s2) else "not anagrams."))

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    newS1 = sort(s1);
    newS2 = sort(s2);

    return newS1 == newS2

def sort(s):
    r = list(s)
    r.sort()

    result = ""
    for ch in r:
        result += ch

    return result

main()


# exercice 6  hangman

import random

def main():
    words = ["write", "program", "that", "receive", "positive", "change", "study", "excellent", "nice"]
    while True:
        index = random.randint(0, len(words) - 1)
        hiddenWord = words[index]
        guessedWord = len(hiddenWord) * ['*']
        numberOfCorrectLettersGuessed = 0
        numberOfMisses = 0
        while numberOfCorrectLettersGuessed < len(hiddenWord):
            letter = input("(Guess) Enter a letter in word " + toString(guessedWord) + " > ").strip()
            if letter in guessedWord:
                print("\t", letter, "is already in the word")
            elif hiddenWord.find(letter) < 0:
                print("\t", letter, "is not in the word")
                numberOfMisses += 1
            else:
                k = hiddenWord.find(letter)
                while k >= 0:
                    guessedWord[k] = letter
                    numberOfCorrectLettersGuessed += 1
                    k = hiddenWord.find(letter, k + 1)
        print("The word is " + hiddenWord + ". You missed "
                + str(numberOfMisses) + (" time" if (numberOfMisses <= 1) else " times"))
        anotherGame = input("Do you want to guess for another word? Enter y or n> ").strip()
        if anotherGame == 'n':
            print("Finished")
            break

def toString(list):
    s = ""
    for e in list:
        s += e
    return s

main()
