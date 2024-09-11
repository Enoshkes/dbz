class Warrior:

    def __init__(self, uid, name, ki, max_ki, race, gender, description, affiliation):
        self.uid = uid
        self.name = name
        self.ki = ki
        self.max_ki = max_ki
        self.race = race
        self.gender = gender
        self.description = description
        self.affiliation = affiliation


    def __repr__(self):
        return f"Warrior: ({self.name}, {self.description}) "