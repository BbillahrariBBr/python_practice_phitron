class School:
    def __init__(self,school_name) -> None:
        self.school_name = school_name
        print('School init Called')

class Grade:
    def __init__(self,grade_name) -> None:
        self.grade_name = grade_name
        print('Grade class init called')

class SportsTeam:
    def __init__(self,sport_name) -> None:
        self.sport_name = sport_name
        self.team = []
    
    def add_player(self,player_name):
        self.team.append(player_name)

class Student(School,Grade,SportsTeam):
    def __init__(self,name,grade_name,school_name,sport_name):
        self.name = name
        print('Student init called')
        Grade.__init__(self,grade_name)
        School.__init__(self,school_name)
        SportsTeam.__init__(self,sport_name)

        


ananta = Student('Aj','MBA', 'UK school','Cricket')

print(ananta.name)
print(ananta.grade_name)
print(ananta.school_name)
print(ananta.sport_name)
ananta.add_player('Borsha')
print(ananta.team)