# Third party imports
from pysat.formula import IDPool
from pysat.solvers import Glucose3

def evaluate_atoms_by_name(clause: list, id_pool: IDPool):
    return list(map(lambda id: id_pool.obj(abs(id)), clause))

def generate_variables(courses_names: list, slots_names: list, id_pool: IDPool):
    for course_name in courses_names:
        id_pool.id(course_name)
    
    for slot_name in slots_names:
        id_pool.id(slot_name)


def output(glucose: Glucose3, id_pool: IDPool):
    print('\n=-=-=-= Resultado =-=-=-=\n')
    has_solution = glucose.solve()

    if has_solution:
        for id in glucose.get_model():
            if id > 0:
                atom = id_pool.obj(id)
                print(atom)
    else:
        print('Não é possível solucionar esse problema!')
    
