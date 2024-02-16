import os



FAV_COLOR = input('What is your favorite color? ')
GENDER = input('What is your gender? ')
COLLEGE_STUDENT = input('Are you a college student?' )

os.environ["FAV_COLOR"] = FAV_COLOR
os.environ["GENDER"] = GENDER
os.environ["COLLEGE_STUDENT"] = COLLEGE_STUDENT

print(os.getenv("FAV_COLOR"))
print(os.getenv("GENDER"))
print(os.getenv("COLLEGE_STUDENT"))