maximum_bad_grades = int(input()) #брой незадоволителни оценки - цяло число
average_grade = 0 # средна оценка ( още не е разделена на броя оценки)
total_problems_solved = 0 #
last_problem = ""
bad_grades_counter = 0 #
is_expelled = False # ако стане вярно означава, че е получил повече лоши оценки от maximum_bad_grades
current_problem = input() # Име на изпита

while current_problem != "Enough": #
    current_grade = int(input()) # Оценка на задачата
    if current_grade <= 4: # ако оценката е по малка или равна на 4
        bad_grades_counter += 1 # сумираме лошите оценки
        if bad_grades_counter == maximum_bad_grades: # ако е получил лоши оценки колкото maximum_bad_grades
            is_expelled = True # има повече лоши оценки от maximum_bad_grades
            break # прекратява While цикъла
    average_grade += current_grade # добавяме стойността на всяка оценка за средно аритметично
    total_problems_solved += 1 # общ брой оценки. (ще направим средно аритм. с тях)
    last_problem = current_problem #името на последната задача
    current_problem = input() # име на изпита и превъртаме цикъла на ново
if is_expelled: # is expelled == True
    print (f"You need a break, {bad_grades_counter} poor grades.")
else: # current_problem == "Enough"
    average_grade /= total_problems_solved
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {total_problems_solved}")
    print(f"Last problem: {last_problem}")
