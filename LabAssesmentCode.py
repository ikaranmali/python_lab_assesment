'''
Author: Karan Mali
Email :ikaranmali@gmail.com
Date: 11-09-2022
'''
import time, sys

class city_data():

    main_dataset = []    
    
    def __init__(self):

        self.select_operation_menu()
        

#--- Select Menu ----

    def select_operation_menu(self):
        print("\n-------Operation Menu---------")
        choose_operation = 0
        while choose_operation !=5:
            try:
                choose_operation = int(input("\nEnter number to choose operation to perform:\n Press 1. To display pollutant details.\n Press 2. To add pollutant details. \n Press 3. To update existing pollutant details.\n Press 4. To delete existing pollutant details. \n Press 5. To exit.\n\n"))
                print("\nSelected operation: {}".format(choose_operation))
            except ValueError:
                print("Exception incorrect input, Please input a number!")
                pass
            if choose_operation == 1:
                self.display_pollutant_details()
            elif choose_operation == 2:
                self.add_pollutant_details()
            elif choose_operation == 3:
                self.update_existing_pollutant_details()
            elif choose_operation == 4:
                self.delete_existing_pollutant_details()
            elif choose_operation == 5:
                sys.exit("Exiting!!")
            else:
                print("\nPlease try again by selecting operation from given menu.")
                continue

# --- Display Details
    def display_pollutant_details(self):
        print("\nMain Dataset as follows:\n",self.main_dataset)
#--- delete element
    def delete_element(self,index):
        self.main_dataset.pop(index)
        print("Deleted from main data\n")
        self.display_pollutant_details()

#--- Add Details ----
    def add_pollutant_details(self):
        ts = int(time.time())
        city_name = str(input("\nPlease enter city name:"))
        co = str(input("\nPlease enter co value:"))
        no2 = str(input("\nPlease enter no2 value:"))
        co2 = str(input("\nPlease enter co2 value:"))
        
        self.pollutant_dataset = {
            "ts":ts,
            "city_name": city_name,
            "co":co,
            "no2":no2,
            "co2":co2
        }

        self.main_dataset.append(self.pollutant_dataset)
        print("\nAdded details:{}".format(self.pollutant_dataset))

#--- Update Details ---    
    def update_existing_pollutant_details(self):
        update_city_name = input("Enter city name to update details:\n")
        print("\nEntered city name: {}".format(update_city_name))
        #Check if city name exists in main dataset.

        for index,dataset in enumerate(self.main_dataset):
            # print(dataset)
            if dataset["city_name"]==update_city_name:
                update_index = index         
                print("\n{} city name exists in dataset\n".format(update_city_name))
                update_co = input("Enter updated co value:\n")
                update_no2 = input("Enter updated no2 value:\n")
                update_co2 = input("Enter updated co2 value:\n")
                self.main_dataset[update_index]["co"]=update_co
                self.main_dataset[update_index]["co2"]=update_co2
                self.main_dataset[update_index]["no2"]=update_no2
                print("updated data:",self.main_dataset[update_index])
            else:
                print("City name does not exist in main dataset\n")
                pass
#--- Delete Details ---
    def delete_existing_pollutant_details(self):
        self.display_pollutant_details()
        delete_timestamp = int(input("\nEnter timestamp 'ts' value from main-dataset to delete details:\n"))
        print("\nEntered timestamp 'ts': {}".format(delete_timestamp))
        #Check if city name exists in main dataset.
        for index,dataset in enumerate(self.main_dataset):
            if dataset["ts"]==delete_timestamp:
                delete_index = index
                self.delete_element(delete_index)
            else:
                print("ts does not exist in main dataset\n")
                pass

if __name__ == '__main__':
    try:
        class_object = city_data()
    except Exception as e:
        print(e)
        pass
    except KeyboardInterrupt:
        print("Terminated by user.")