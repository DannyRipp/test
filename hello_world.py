num_a = "mississippi, connecticut, maine".split(',')
#print(num_a)
name3 = "daniel"
name2 = "tevor"
#if name2 == "trevor":
   # print("trevor is in the list")
#elif name3 == "daniel":
#    print("dan is in the list")
class Cust:


    def __init__(self, name, money):
        self.name=name
        self.money = money

    def get_name(self):
        print(self.name)
    def get_mon(self):
        print(self.money)
moneyy=5.35
namee="billy"
jimmy= Cust(namee, moneyy)
aList=[jimmy]
#james=Student("elf")
#james.get_name()

def num_of_a(name1):
    num_b = name1.count('a')
    return num_b

def counting(numb):
    for x in range(numb):
        print("ayy")
        print("y")

def listmaker(number, word):
   for x in range(number):
       wordz=word+("y"*x)
       print(wordz)

    #stringg="ayy"
    #thelist=[stringg]
    #thelist.append(stringg)
    #pos=len(thelist)

    #for x in range(pos):
    #    the_y=

#my_num = num_of_a("haaam")
#print(my_num)
#ans=input()
#counting(int (ans))
print("how many?")
ans=input()
listmaker(int (ans), "ayy")