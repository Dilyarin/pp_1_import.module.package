from application.salary import Salary
from application.db.people import People
from datetime import datetime, date, time


def main():
    print(datetime.today())

    CompanyX = Salary(100)
    CompanyX.calculate_salary()

    New = People('people')
    New.get_employees()

if __name__ == '__main__':
    main()




