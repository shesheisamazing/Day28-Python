# class 1
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

# class 2
class Germany():
    def capital(self):
        print("Berlin is the capital of Germany.")

    def language(self):
        print("Deutsch (German) is the primary language of Germany.")

    def type(self):
        print("Germany is a developed country.")

# object creation
obj_ind = India()
obj_ger = Germany()

# common interface
for country in (obj_ind, obj_ger):
    country.capital()
    country.language()
    country.type()