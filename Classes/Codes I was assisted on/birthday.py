# https://www.youtube.com/watch?v=uMhmUTgGmm8

class BirthdayBoy:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old")

me = BirthdayBoy("Tonny", 19)
print(f"{me.name} is {me.age} years old")
me.birthday()