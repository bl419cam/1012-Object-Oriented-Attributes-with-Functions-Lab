class School():

    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster

    def add_student(self, name, grade):
        if str(grade) in list(self.roster.keys()):
            self.roster[str(grade)].append(name)
        else:
            self.roster[str(grade)] = [name]

    def grade(self, grade):
        return self.roster[str(grade)]

    def sort_roster(self):
        for grade in self.roster.keys():
            self.roster[grade].sort()
        
        return self.roster