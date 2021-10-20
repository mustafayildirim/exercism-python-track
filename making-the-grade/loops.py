def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    list_of_students = []
    for score in student_scores:
        list_of_students.append(round(score))

    return list_of_students


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    student_count = 0
    for score in student_scores:
        if round(score) <= 40:
            student_count = student_count + 1
    return student_count


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    return best_scores


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """

    difference = int((highest - 40) / 4)
    list_of_students = [41]
    for i in range(3):
        list_of_students.append(41 + difference * (i+1))

    return list_of_students



def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    list_of_students = []
    for index, student in enumerate(student_names):
        list_of_students.append(f'{index+1}. {student}: {student_scores[index]}')

    return list_of_students


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    for student in student_info:
        if student[1] == 100:
            return student

    return 'No perfect score.'
