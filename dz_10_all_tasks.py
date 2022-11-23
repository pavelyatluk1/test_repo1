# Pavlo Yatluk
# dz_10
# №1 Напишіть функцію яка приймає номер мфсяця і повертає його назву. Реалізувати декілька виключень.

def month_name():
    try:
        n = int(input())
        m_n = month_year.get(n)
        return m_n
    except Exception:
        print('Введіть число від 1 до 12')

month_year = {1: 'January', 2: "Febrгary", 3: "arch", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November", 12: "December"}

print(month_name())

#2 Написати програму яка приймає рядок з числами та переіряє чи всі числа в ньому унікальні.

def uniq_nun():
    try:
        s = [1, o]
        s1 = []
        for i in range(len(s)):
            if s[i] in s1:
                res = "В списку числа не унікальні"
                break
                return res
            else:
                s1.append(s[i])
                res = "В списку всі числа  унікальні"
        return res
    except Exception:
        print("В списку повинні бути цілі числа")

print(uniq_nun())


#3. Копія коду з лекції без змін

class MyCustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'MyCustomError, {0} '.format(self.message)
        else:
            return 'MyCustomError has been raised'

raise MyCustomError('We have a problem')
