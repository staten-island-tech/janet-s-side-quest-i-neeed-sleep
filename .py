courses = {
    "Python Programming": {"fee": 150,"seats": 0,"category" : "Technology"},
    "Machine Learning": {"fee": 200,"seats": 3,"category" : "Technology"},
    "Business Strategy": {"fee": 100,"seats": 5,"category" : "Business"},
    "Marketing 101": {"fee": 120,"seats": 2,"category" : "Business"},
    "Cybersecurity": {"fee": 180,"seats": 4,"category" : "Technology"}
}

student_enrollment = ["Python Programming","Cybersecurity", "Marketing 101"]

for i in courses:
    for s in student_enrollment:
        