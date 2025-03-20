courses = {
    "Python Programming": {"fee": 150,"seats": 0,"category" : "Technology"},
    "Machine Learning": {"fee": 200,"seats": 3,"category" : "Technology"},
    "Business Strategy": {"fee": 100,"seats": 5,"category" : "Business"},
    "Marketing 101": {"fee": 120,"seats": 2,"category" : "Business"},
    "Cybersecurity": {"fee": 180,"seats": 4,"category" : "Technology"}
}

student_enrollment = ["Python Programming","Cybersecurity", "Marketing 101"]

m = 0
mbd = 0
x = "e"
d = ""
w = ""
ee = False


for y in range(2*len(courses)):
    for i, l in courses.items():
        for s in student_enrollment:
            if s in i and l["seats"] == 0:
                w = l["category"]
                d = i
            if l["category"] == w and l["seats"] > 0 and i != s:
                x = i

for i, l in courses.items():
    for s in student_enrollment:
        if s in i and l["seats"] == 0 and x != "e":
            print(f"{d} is full. Suggesting {x} instead.")





for i, l in courses.items():
    for s in student_enrollment:
        if s in i:
            mbd += l["fee"]

if len(student_enrollment) >= 3:
    print("Applying 5% discount for enrolling 3 or more courses.")
    m = mbd *.95

for i, l in courses.items():
    if i in student_enrollment and l["category"] == "Technology" and ee == False:
            print("Applying $20 scholarship for enrolling in a Technology course.")
            m-=20
            ee = True


print(f"Total enrollment cost before discount: ${mbd}")
print(f"Total enrollment cost after discount: ${m}")