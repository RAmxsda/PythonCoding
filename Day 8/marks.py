student_score = {
    "GrandFather": 81,
    "GrandMother": 90,
    "Father": 76,
    "Mother": 88,
    "Me": 68,
    "Sister": 100,
}


grading_marks = {}
for student in student_score:
    if student_score[student] > 90:
        grading_marks[student] = "Outstanding"
    elif student_score[student] > 80:
        grading_marks[student] = "Excellent"
    elif student_score[student] >= 70:
        grading_marks[student] = "Good"
    elif student_score[student] >= 60:
        grading_marks[student] = "Work Hard"
    else:
        grading_marks[student] = "Fail"

print(grading_marks)


travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}


def add_new_country(country, cities, visits):
    travel_log[country] = {"cities_visited": cities, "total_visits": visits}
    return travel_log


add_new_country("NEPAL", ["POKHARA", "KATHMANDU", "KHAPTAD", "ILLAM"], 100000000000000)

print(travel_log)
for country in travel_log:
    print(country)
    for key in travel_log[country]:
        print(f"{key}: {travel_log[country][key]}")
