# Third party imports
from pysat.formula import IDPool
from pysat.solvers import Glucose3
from .utils import evaluate_atoms_by_name

def check_first_condition(courses_names: list, slots_names: list, id_pool: IDPool, glucose: Glucose3):
    ''' Each short course must be offered in at least one slot '''
    for course_name in courses_names:
        clauses_by_course = []
        
        for slot_name in slots_names:
            id = id_pool.id(f"{course_name}-{slot_name}")
            clauses_by_course.append(id) 

        glucose.add_clause(clauses_by_course)

    
def check_second_condition(courses_names: list, slots_names: list, id_pool: IDPool, glucose: Glucose3):
    ''' Each course must be offered in a maximum of one slot '''
    clauses_by_course = {}
    for course_name in courses_names:
        for slot_name in slots_names:
            id = id_pool.id(f"{course_name}-{slot_name}")
            
            clauses_by_course.setdefault(course_name, [])
            clauses_by_course[course_name].append(id)

    for clauses in clauses_by_course.values():
        for course_slot_x_id in clauses:
            for course_slot_y_id in clauses:
                if course_slot_x_id == course_slot_y_id:
                    continue

                clause = [-course_slot_x_id, -course_slot_y_id]
                glucose.add_clause(clause)


def check_third_condition(courses_pairs: dict, slots_names: list, id_pool: IDPool, glucose: Glucose3):
    ''' Short courses with common registrations cannot be offered in the same slot. '''
    for course_x_id, course_y_id in courses_pairs.items():
        for slot_name in slots_names:
            id_x = id_pool.id(f'{id_pool.obj(course_x_id)}-{slot_name}')
            id_y = id_pool.id(f'{id_pool.obj(course_y_id)}-{slot_name}')
            
            clause = [-id_x, -id_y]
            glucose.add_clause(clause)