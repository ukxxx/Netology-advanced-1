from application.salary import *
from application.db.people import *
import datetime
import pywinctl as pw

if __name__ == '__main__':
    print(datetime.date.today())
    get_employees()
    calculate_salary()
    window = pw.getActiveWindow()
    print(f'Current window title: {window.title}')