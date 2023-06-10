# Third party imports
from pysat.solvers import Glucose3
from pysat.formula import IDPool

# Local imports
from .utils import output
from .utils import generate_variables
from .conditions import check_first_condition
from .conditions import check_second_condition
from .conditions import check_third_condition

glucose = Glucose3()
id_pool = IDPool()


print('-=-' * 10 + ' Solucionador de eventos ' + '-=-' * 10)

courses_amount = int(input('Quantidade de cursos do evento -> '))

courses_names = []
for course_index in list(range(1, courses_amount + 1)):
    course_name = str(input(f'{course_index}º curso -> '))
    courses_names.append(course_name)

slots_amount = int(input(('\nSlots de tempo -> ')))
slots_names = list(map(lambda index: f'Slot {index}', list(range(1, slots_amount + 1))))

generate_variables(courses_names, slots_names, id_pool)

print('\n=-=-=-= Lista de cursos =-=-=-=')
for course_name in courses_names:
    print(f'{id_pool.id(course_name)} - {course_name}')

print('\n=-=-=-= Lista de slots =-=-=-=')
for slot_name in slots_names:
    print(slot_name)


print('\n=-=-=-= Cursos com inscrições em comum =-=-=-=')
print('ID-ID -> relaciona um par de cursos')
print('0 -> Sair')

courses_pairs = {}
input_pair = None

while(input_pair != '0'):
    input_pair = str(input('\nInforme o par de cursos -> '))
    
    if input_pair == '0':
        break

    try:
        input_pair = input_pair.split('-')
        if input_pair[0] == input_pair[1]:
            print('Não é possível relacionar um curso a ele mesmo!')
        else:
            courses_pairs.setdefault(int(input_pair[0]), int(input_pair[1]))
    except Exception as error:
        print(error)

check_first_condition(courses_names, slots_names, id_pool, glucose)
check_second_condition(courses_names, slots_names, id_pool, glucose)   
check_third_condition(courses_pairs, slots_names, id_pool, glucose)

output(glucose, id_pool)

glucose.delete()

