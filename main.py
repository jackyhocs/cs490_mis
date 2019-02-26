import time

from external_services import ExternalService
from mis_app import ManagerialApp

def main():
    service_handler = ExternalService()
    managerial_app = ManagerialApp()

    while True:
        print("Server running!")
        print(managerial_app.get_report(2))
        time.sleep(5)

main()