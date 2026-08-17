from app.data import courses


def list_courses():
   
    return [course for course in courses if course["active"] or not course["active"]]


def get_course_by_id(course_id: int):
    return next((course for course in courses if course["id"] == course_id), None)


def delete_course(course_id: int):
    course = get_course_by_id(course_id)

    if not course:
        return False

    courses.remove(course)
    return True
