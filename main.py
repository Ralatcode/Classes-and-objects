class Student:
    # [assignment] Skeleton class. Add your code here\

    # Constructor
    def __init__(self, name, age, tracks, score):
        # creates instances 
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    
    # creates a change name method
    def change_name(self, new_name):
        self.name = new_name
        print("The student has changed its name from ", self.name," to ", new_name)

    # creates a change age method
    def change_age(self, new_age):
        self.name = int(new_age)
        print("The student age has changed from ", self.age, " to ", new_age)
    # adds a new item to track method 
    def add_track(self, new_item):
        self.tracks.append(new_item)
        print(new_item," was added as a new item, new track is ", self.tracks)

    # returns the score
    def get_score(self):
        return print("This is your score ", self.score)
    
Bob = Student(name="Bob", age=26, tracks= ["FE","BE"],score=20.90) 

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
