#function to get grades
def grade_calc(score):
    if score > 80:
        grade = 1
    elif score >= 70 and score <= 79:
        grade = 2
    elif score >= 50 and score <= 69:
        grade = 3
    elif score >= 40 and score <= 59:
        grade = 4
    else:
        grade = 5
    return grade

#function to calculate two best electives
def two_best(array):
    highest1 = array[0]
    highest2 = array[0]
    for i in range(1, 5):
        if array[i] < highest1:
            highest1 = array[i]
            highest2 = highest1
        elif array[i] < highest2:
            highest2 = array[i]
    return highest1 + highest2

def calculate_aggregate(self,English_grade,Maths_grade,Science_grade,Social_grade,RME_grade,BDT_grade,GH_lang_grade,French_grade,ICT_grade,core_aggregate,elective_grades,aggregate):
    self.core_aggregate = English_grade + Maths_grade + Science_grade + Social_grade
    self.elective_grades = [RME_grade, BDT_grade, GH_lang_grade, French_grade, ICT_grade]
    self.aggregate = core_aggregate + two_best(elective_grades)
    return self.aggregate

