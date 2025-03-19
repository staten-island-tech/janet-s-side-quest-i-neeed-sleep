courses = {
    "Python Programming": {
        "fee": 150,
        "seats": 0,
        "category" : "Technology"
    },
    "Machine Learning": {
        "fee": 200,
        "seats": 3,
        "category" : "Technology"
    },
    "Business Strategy": {
        "fee": 100,
        "seats": 5,
        "category" : "Business"
    },
    "Marketing 101": {
        "fee": 120,
        "seats": 2,
        "category" : "Business"
    },
    "Cybersecurity": {
        "fee": 180,
        "seats": 4,
        "category" : "Technology"
    }
}

student_enrollment = ["Python Programming","Cybersecurity", "Marketing 101"]

m = 0
mbd = 0
t = 0
x = ""
d = ""
w = ""
oo = 0
ee = False

for i in courses:
    oo += 1

for i in range(2*oo):
    for i, l in courses.items():
        for s in student_enrollment:
            if s in i and l["seats"] == 0:
                w = l["category"]
                d = i
            if s in i == False:
                if l["category"] == w and l["seats"] > 0:
                    x = i

for i, l in courses.items():
    for s in student_enrollment:
        if s in i and l["seats"] == 0:
            print(f"{d} is full. Suggesting {x} instead.")

for i, l in courses.items():
    for s in student_enrollment:
        if s in i:
            mbd += l["fee"]

for i in student_enrollment:
    t+=1
if t >= 3:
    print("Applying 5% discount for enrolling 3 or more courses.")
    m = mbd *.95

for i, l in courses.items():
    if i in student_enrollment and l["category"] == "Technology" and ee == False:
            print("Applying $20 scholarship for enrolling in a Technology course.")
            m-=20
            ee = True


print(f"Total enrollment cost before discount: ${mbd}")
print(f"Total enrollment cost after discount: ${m}")