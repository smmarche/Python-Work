
import csv
import statistics
import matplotlib.pyplot as drawing
import os
grades = {}



def average_scores(list_of_scores):
    """Returns the average of a list of numbers"""
    #turns the list of string numbers into floats
    list_of_scores=[float(x) for x in list_of_scores]
    #sums the list of numbers
    total_sum = sum(list_of_scores)
    #gives the length of the list of numbers
    number_of_scores = len(list_of_scores)
    #divides the sum of the list of numbers by the length of the list
    average_result = total_sum / number_of_scores
    #returns this result of the division
    return average_result


def letter_grade(grade):
    """Returns the letter grade for a certain numerical grade"""

    if grade < 60:
        return "F"
    elif grade < 70:
        return "D"
    elif grade < 80:
        return "C"
    elif grade < 90:
        return "B"
    elif grade >= 90:
        return "A"


def dictionary_of_student_scores():
    """This function creates a dictionary pair with the UIN and weighted scores associated with each UIN."""
    UIN_scores = {}
    for UIN in grades:
        UIN_scores[UIN] = 0.45*sum(grades[UIN][-4:-1])/3 + 0.10*sum(grades[UIN][6:12])/6 + .10 * sum(grades[UIN][12:18])/6 \
                          + .25*sum(grades[UIN][:6])/6 + .1 * grades[UIN][-1]
    return UIN_scores



def option_1():
    """This allows a file to be read and saved into a dictionary."""
    path = input("Enter the full path of the CSV file you would like read: ")
    with open(path) as file:
        if not os.path.exists(path):
            print("Either the file doesn't exist or you don't have the correct permissions to access it.")
        else:
            csv_list = csv.reader(file, delimiter=',')
            for i, row in enumerate(csv_list):
                if i != 0:
                    grades[row[0]] = [float(item) for index, item in enumerate(row) if index != 0]
            print("Read the csv file.")
    print()


def option_2():
    """This function generates a txt file specific to a certain UIN. This file will contain the students's
     average scores and letter grade. """
    #The if statement below checks if the user has done option 1: read the file and if not, it prompts them to do so
    if not grades:
        print("Please read file before proceeding (option 1).")
        return 0
    while True:
        uin = input("Please provide the student's UIN: ")
        print()
        if len(uin) != 10 or not uin.isnumeric():
            print("UIN is not in the correct format.")
            print()
        # If the provided UIN is not in the file, the program notifies the user and repeats
        elif uin not in grades:
            print(f'The UIN ({uin}) is not in the grade center.')
        # Pulls up the grades attached to the UIN
        else:
            # Creating a txt file with the handle as the uin
            student_stats = open(f"{uin}.txt", "w")
            for key, value in grades.items():
                if key == uin:
                    # Gives the exam average and the weighted exam score
                    exam_scores = value[-4:-1]
                    sum_weighted_exam_scores = average_scores(exam_scores) * .45
                    rounded_exam_score = round(average_scores(exam_scores), 1)
                    exam_mean_one = f"Exams mean: {rounded_exam_score}\n"
                    student_stats.write(exam_mean_one)
                    # Gives the lab mean and the weighted lab mean
                    lab_scores = value[:6]
                    weighted_lab_score = average_scores(lab_scores) * .25
                    rounded_lab_scores = round(average_scores(lab_scores), 1)
                    lab_mean = f"Labs mean: {rounded_lab_scores}\n"
                    student_stats.write(lab_mean)
                    # Gives the quiz mean and the weighted quiz mean
                    quiz_scores = value[6:12]
                    weighted_quiz_score = average_scores(quiz_scores) * .1
                    rounded_quiz_score = round(average_scores(quiz_scores), 1)
                    quiz_mean = f"Quizzes mean: {rounded_quiz_score}\n"
                    student_stats.write(quiz_mean)
                    # Gives the reading mean and the weighted reading mean
                    reading_scores = value[12:18]
                    weighted_reading_score = average_scores(reading_scores) * .1
                    rounded_reading_score = round(average_scores(reading_scores), 1)
                    reading_mean = f"Reading activities mean: {rounded_reading_score}\n"
                    student_stats.write(reading_mean)
                    # Gives the weighted project score
                    project_grade = float(value[-1])
                    weighted_project_score = project_grade * .1
                    # Sums all weighted scores
                    score = sum_weighted_exam_scores + weighted_quiz_score + weighted_reading_score + \
                            weighted_lab_score + weighted_project_score
                    rounded_score = round(score, 1)
                    score_printout = f"Score: {rounded_score}%\n"
                    student_stats.write(score_printout)

                    letter_grade_printout = f"Letter grade: {letter_grade(rounded_score)}\n"
                    student_stats.write(letter_grade_printout)

            student_stats.close()
            break


    #The if statement below checks if the user has done option 1: read the file and if not, it prompts them to do so
def option_3():
    """After the user provides the UIN, bar charts of exams, labs, quizzes, and reading activities are made into
    separate png files within a directory."""
    # the if statement below checks if the user has done option 1: read the file and if not, it prompts them to do so
    if not grades:
        print("Please read file before proceeding (option 1).")
        return 0
    uin_two = input("Please provide the student's UIN: ")
    print()
    # drawing.figure(#) distinguishes the following figures within this function
    drawing.figure(1)
    # x_exam is the specific x labels for the barchart of exam grades
    x_exam = ['Exam 1', 'Exam 2', 'Exam 3']
    # y_exam is the specific y labels for the barchart of exam grades since the index from 18 to 21(not inclusive)
    # is the exam grades
    y_exam = grades[uin_two][18:21]
    drawing.xlabel("Exam Number")
    drawing.ylabel("Score (%)")
    drawing.title(f"Exam grades for {uin_two}")
    # drawing.bar(...) creates the actual bar chart with x and y labels, aligned in the center and the color blue
    drawing.bar(x_exam, y_exam, align='center', color="b", label=f"Exam grades for {uin_two}")
    # drawing.legend() writes what the label states in the code above to be the legend
    drawing.legend()
    # the following 2 lines of code are what make the directory
    path = f'./{uin_two}'
    os.mkdir(path)
    # drawing.savefig(...) saves the figures in separate png files and in this case as bar_chart_of_exam.png
    drawing.savefig(path + '/bar_chart_of_exam.png')
    drawing.show()
    drawing.close()

    drawing.figure(2)
    x_lab = ['Lab 1', 'Lab 2', 'Lab 3', 'Lab 4', 'Lab 5', 'Lab 6']
    # y_lab is the specific y labels for the barchart of lab grades since the
    # index from 0 to 6 (not inclusive) is the lab grades
    y_lab = grades[uin_two][:6]
    drawing.xlabel("Lab Number")
    drawing.ylabel("Score (%)")
    drawing.title(f"Lab grades for {uin_two}")
    drawing.bar(x_lab, y_lab, align='center', color="r", label=f"Lab grades for {uin_two}")
    drawing.legend()
    # drawing.savefig(...) saves the figures in separate png files and in this case as bar_chart_of_lab.png
    drawing.savefig(path + '/bar_chart_of_lab.png')
    drawing.show()
    drawing.close()

    drawing.figure(3)
    x_quiz = ['Quiz 1', 'Quiz 2', 'Quiz 3', 'Quiz 4', 'Quiz 5', 'Quiz 6']
    # y_quiz is the specific y labels for the barchart of quiz grades since the
    # index from 6 to 12 (not inclusive) is the quiz grades
    y_quiz = grades[uin_two][6:12]
    drawing.xlabel("Quiz Number")
    drawing.ylabel("Score (%)")
    drawing.title(f"Quiz grades for {uin_two}")
    drawing.bar(x_quiz, y_quiz, align='center', color="r", label=f"Quiz grades for {uin_two}")
    drawing.legend()
    # drawing.savefig(...) saves the figures in separate png files and in this case as bar_chart_of_quiz.png
    drawing.savefig(path + '/bar_chart_of_quiz.png')
    drawing.show()
    drawing.close()

    drawing.figure(4)
    x_reading = ['Reading 1', 'Reading 2', 'Reading 3', 'Reading 4', 'Reading 5', 'Reading 6']
    # y_reading is the specific y labels for the barchart of reading activity grades since the
    # index from 12 to 18 (not inclusive) is the reading activity grades
    y_reading = grades[uin_two][12:18]
    drawing.xlabel("Reading Activity Number")
    drawing.ylabel("Score (%)")
    drawing.title(f"Reading activity grades for {uin_two}")
    drawing.bar(x_reading, y_reading, align='center', color="b", label=f"Exam grades for {uin_two}")
    drawing.legend()
    # drawing.savefig(...) saves the figures in separate png files and
    # in this case as bar_chart_of_reading_activities.png
    drawing.savefig(path + '/bar_chart_of_reading_activities.png')
    drawing.show()
    drawing.close()


#The if statement below checks if the user has done option 1: read the file and if not, it prompts them to do so
def option_4():
    """This function gives a letter grade to each student's score and saves them to a dictionary."""
    #The if statement below checks if the user has done option 1: read the file and if not, it prompts them to do so
    if not grades:
        print("Please read file before proceeding (option 1).")
        return 0


    dictionary_of_student_scores()
    # Count the number of students

    class_statistics = open(f"report.txt", "w")
    number_of_students = f'Total number of students: {len(grades)}\n'
    class_statistics.write(number_of_students)
    all_student_scores =[]
    for scores in dictionary_of_student_scores().values():
        all_student_scores.append(scores)
    minimum_score = round(min(all_student_scores), 1)
    minimum_score_print = f'Minimum score: {minimum_score}\n'
    class_statistics.write(minimum_score_print)

    maximum_score = round(max(all_student_scores), 1)
    maximum_score_print = f'Maximum score: {maximum_score}\n'
    class_statistics.write(maximum_score_print)

    median_score = round(statistics.median(all_student_scores), 1)
    median_score_print = f'Median score {median_score}\n'
    class_statistics.write(median_score_print)

    mean_score = round(statistics.mean(all_student_scores), 1)
    mean_score_print = f'Mean score: {mean_score}\n'
    class_statistics.write(mean_score_print)

    standard_deviation = round(statistics.stdev(all_student_scores), 1)
    standard_deviation_print = f'Standard deviation: {standard_deviation}\n'
    class_statistics.write(standard_deviation_print)

    class_statistics.close()


def option_5():
    """This function counts how many students made each letter grade A-F. It then creates a pie
and bar chart with that information."""
    # the if statement below checks if the user has done option 1: read the file and if not, it prompts them to do so
    if not grades:
        print("Please read file before proceeding (option 1).")
        return 0
    # the function dictionary_of_student_scores() is called below to be able to use it in function option_5()
    dictionary_of_student_scores()
    drawing.figure(1)
    # separate counts for the letter grades A-F are made below to keep track of how many students got that letter
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_f = 0
    # the for loop below checks what letter grade each student got while using
    # the dictionary_of_student_scores() function
    for grade in dictionary_of_student_scores().values():
        letter = letter_grade(grade)
        if letter == "F":
            count_f += 1
        if letter == "D":
            count_d += 1
        if letter == "C":
            count_c += 1
        if letter == "B":
            count_b += 1
        if letter == "A":
            count_a += 1
    # grade_distribution is the number of students that made each letter grade
    grade_distribution = [count_a, count_b, count_c, count_d, count_f]
    # letter_grades are the labels of the pie chart
    letter_grades = ['A', 'B', 'C', 'D', 'F']
    # color_option allows multiple parts of the pie chart to be different colors
    color_option = ['MediumAquaMarine', 'b', 'y', 'm', 'r']
    drawing.pie(grade_distribution, labels=letter_grades, colors=color_option)
    drawing.legend()
    drawing.title("Pie chart of the letter grades distribution")
    # the line below creates a directory called class_charts
    path = './class_charts'
    os.mkdir(path)
    # within that directory you can add separate png files which is shown below
    drawing.savefig(path + '/pie_class_chart.png')
    drawing.show()
    drawing.close()

    drawing.figure(2)
    # x_letter_grade is the specific x labels for the bar chart
    x_letter_grade = ['A', 'B', 'C', 'D', 'F']
    # y_number_students is the specific y label for the bar chart which are actual values
    y_number_students = [count_a, count_b, count_c, count_d, count_f]
    drawing.xlabel("Letter Grade")
    drawing.ylabel("Number of Students")
    # drawing.title("...") gives the bar chart a title
    drawing.title("Bar chart of the letter grades distribution")
    # drawing.bar(...) creates the actual bar chart
    drawing.bar(x_letter_grade, y_number_students, align='center', color="r", label="Class Letter Grade Distribution")
    drawing.legend()
    # drawing.savefig(...) saves the drawing in the directory mentioned
    drawing.savefig(path + '/bar_class_chart.png')
    # drawing.show() shows the drawing
    drawing.show()
    # drawing.close() closes the drawing file
    drawing.close()


# Repeating menu options

while True:
    print("*******************Main Menu*****************")
    print("1. Read CSV file of grades")
    print("2. Generate student report file")
    print("3. Generate student report charts")
    print("4. Generate class report file")
    print("5. Generate class report charts")
    print("6. Quit")
    print("************************************************")
    print()
# Input to select menu options
    input_choice = input("Pick a menu option 1 through 6: ").lower()
# If the user picks 1 a CSV file is read
    if input_choice == "1":
        option_1()
# If the user picks 2, a report for the student is made
    if input_choice == "2":
        option_2()
# If the user chooses option 3, this creates a bar chart for a student's grades
    if input_choice == "3":
        option_3()
# If user picks 4, a report for the class is generated
    if input_choice == "4":
        option_4()
# If the user picks 5, a pie and bar chart are made for the entire class
    if input_choice == "5":
        option_5()
# Once the user types q or quit the program stops
    if input_choice == "q" or input_choice == "quit":
        break
