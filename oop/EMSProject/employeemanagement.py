'''
An interface to manage employees performance
'''

class PerfomanceManager:
    def track(self,employees,hours):
        print("**** Tracking employees performance**** ")
        print("=================================")

        for employee in employees:
            # employee.work(hours)
            status = employee.work(hours)
            print(f"{employee.name} : {status}")
            print("------------------------------")


class ManagerRole:
    def work(self,hours):
        return f"Manager is handling the project team for {hours} hours"


class DeveloperRole:
    def work(self,hours):
        return f"Developer is working on the project for {hours} hours"

class SalesRole:
    def work(self,hours):
        return f"Salesman is handling client calls for {hours} hours"


class WorkerRole:
    def work(self,hours):
        return f"As a worker completed his task in {hours} hours"

