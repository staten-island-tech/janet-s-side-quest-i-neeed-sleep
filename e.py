courses = {
    "Python Programming": {
        "fee": 150,
        "seats": 0,
        "category" : "Technology"
    },
    "Machine Learning": {
        "fee": 150,
        "seats": 3,
        "category" : "Technology"
    },
    "Business Strategy": {
        "fee": 150,
        "seats": 2,
        "category" : "Business"
    },
    "Marketing 101": {
        "fee": 150,
        "seats": 2,
        "category" : "Business"
    }
}

student_enrollment = ["Python Programming","Business Strategy"]

e = []
m = 0
t = 0

for i in courses:
    if i["seats"] > 0:
        e.append(i)
    if i in student_enrollment:
        m += i["fee"]

for i in student_enrollment:
    if i != e:
        print(f"{i} is full, try enrolling ")

for i in student_enrollment:
    t+=1
if t >= 3:
    print("Applying 5% discount for enrolling 3 or more courses.")
    m *= .95

for i in courses:
    if i == student_enrollment and i["category"] == "Technology":
        print("Applying $20 scholarship for enrolling in a Technology course.")
        m-=20

print(f"Total enrollment cost: ${m}")