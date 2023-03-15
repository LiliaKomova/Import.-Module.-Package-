from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    try:
        print(datetime.now())
        calculate_salary()
        get_employees()
    except:
        print('Error!')
