class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, new_name):
        self.name = new_name
        print("The student has changed its name from ", self.name," to ", new_name)
    def change_age(self, new_age):
        self.name = int(new_age)
        print("The student age has changed from ", self.age, " to ", new_age)
    def add_track(self, new_item):
        self.tracks = new_item
        print(new_item," was added as a new item")
    def get_score(self):
        return print("This is your score ", self.score)
    
Bob = Student(name="Bob", age=26, tracks= ["FE","BE"],score=20.90) 

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
