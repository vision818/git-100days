class character:
    name = None
    health = 100
    mp = 100

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}")

    def set_stats(self, health, mp):
        self.health = health
        self.mp = mp

class player(character):
    nickname = None
    lives = 3

    def __init__(self, nickname):
        self.name = 'Player'
        self.nickname = nickname

    def print(self):
        print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tNickname: {self.nickname}\tLives: {self.lives}")

    def is_alive(self):
        if self.lives > 0:
            print(f"{self.nickname} is alive!")
            return True
        else:
            print(f"{self.nickname} is dead!")
            return False
        
ian = player("Ian the player")
ian.print()
print(ian.is_alive())

class enemy:
    type = None
    strength = None
    health = 95
    mp = 90


    def __init__(self, name, type, strength):

        self.name = name
        self.type = type
        self.strength = strength

    def print(self):
        print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}")

class orc(enemy):
  speed = None

  def __init__(self, speed):
    self.name = "Orc"
    self.type = "Orc"
    self.strength = 200
    self.speed = speed

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tSpeed: {self.speed}")

sharron = orc(250)
gary = orc(205)

sharron.print()
gary.print()

class vampire(enemy):
  day = True

  def __init__(self, day):
    self.name = "Vampire"
    self.type = "Vampire"
    self.strength = 150
    self.day = day

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tDay: {self.day}")

eric = vampire(False)
eric.print()