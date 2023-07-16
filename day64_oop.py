class job:
  name = None
  salary = None
  hours_worked = None

  def __init__(self, name, salary, hours_worked):
    self.name = name
    self.salary = salary
    self.hours_worked = hours_worked

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hours_worked:>10}")

class doctor(job):
  experience = None
  speciality = None

  def __init__(self, salary, hours_worked, experience, speciality):
    self.name = "Doctor"
    self.salary = salary
    self.hours_worked = hours_worked
    self.experience = experience
    self.speciality = speciality

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hours_worked:>10}")
    print(f"{self.experience:<10} {self.speciality:>21}")

class teacher(job):
  subject = None
  position = None

  def __init__(self, salary, hours_worked, subject,  position):
    self.name = "Teacher"
    self.hours_worked = hours_worked
    self.salary = salary
    self.subject = subject
    self.position = position
  
  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hours_worked:>10}")
    print(f"{self.subject:<10} {self.position:>21}")

lawyer = job("Lawyer", "$100,000", "40")
lawyer.print()

doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print()

teach = teacher("$50,000", "48+", "Computer Science", "Asst. Principal")
teach.print()