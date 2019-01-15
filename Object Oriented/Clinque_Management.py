import json
from builtins import str


class CliniqueManagement:

    def __init__(self):
        pass

    def UserInput(self):  # This method is to take the input from user
        print()
        print("*********Welcome to Clinique System*******")
        print()
        try:
            ch = input("Press : y/n to continue or exit:")
            while ch == 'y':
                print(" \n 1.Doctor Options  \n 2.For Patient options ? \n 3.Exit")  # Enter the User's Choice
                choice = int(input("Enter your choice:"))
                if choice == 1:
                    print("\n 1.Add Doctor \n 2.View Doctors \n 3.Exit")  # For a selection of a doctor
                    ch1 = int(input("Enter your choice:"))
                    if ch1 == 1:
                        self.add_doctors()  # Add Doctor
                    elif ch1 == 2:
                        self.view_doctors()  # Display Doctor details
                    elif ch1 == 3:
                        break
                    else:
                        print("!!..Invalid choice..!!")
                        break
                elif choice == 2:
                    print("\n 1.Add Appointment \n 2.Search Doctor \n 3.Exit")
                    ch2 = int(input("Enter your choice:"))
                    if ch2 == 1:
                        self.addAppointment()
                    elif ch2 == 2:
                        print(
                            "\n 1.Search Doctor by Name \n 2.Search Doctor Id \n 3.Search Doctor Specialization \n 4.Exit")
                        ch3 = int(input("Enter your choice:"))
                        if ch3 == 1:
                            self.searchDoctorbyName()  # Search doctor by the name
                        elif ch3 == 2:
                            self.searchDoctorbyId()  # Search doctor by id
                        elif ch3 == 3:
                            self.search_doctor_by_Specialization()  # Search by specialization


                    elif ch2 == 3:
                        break
                    else:
                        print("!!..Invalid choice..!!")
                        break
                elif choice == 3:
                    break
                else:
                    print("!!!..Invalid choice..!!!")
                    break
        except ValueError:
            print("Enter Valid Choice")

    def doctor_information(self):
        """
         This method is to create the json file which contain information about doctors
        :return: it return doctor file in the form of dictionary
        """
        with open('doctor.json', 'r') as file_obj:  # Read the file
            json_str = file_obj.read()
            # loads the data and convert it into dictionary format

            json_value = json.loads(json_str)

            file_obj.close()

        return json_value

    def paitent_information(self):

        # open json file to read
        try:
            with open('paitent.json', 'r') as file_obj:
                json_str = file_obj.read()
                # loads the data and convert it into dictionary format
                json_value = json.loads(json_str)
            file_obj.close()
            return json_value

        except FileNotFoundError:
            print("File Not Found")

    def appoinment(self):
        """
         This method is to create the json file which contain all information about patients appointment
        :return: it returns appointment file in the form of dictionary
        """
        try:
            with open('appointment.json', 'r') as file_obj:
                json_str = file_obj.read()
                # loads the data and convert it into dictionary format
                json_value = json.loads(json_str)
            file_obj.close()
            return json_value

        except FileNotFoundError:
            print("File Not Found")

    def add_doctors(self):
        """
         This method is to add new entery doctor
        """
        doctor_name = input("Enter Name:")
        doctor_id = int(input("Enter Id:"))
        specilization = input("Enter Specialization:")
        availability = input("Enter Availability(AM/PM/Both):")

        with open('doctor.json', 'r') as file_obj:
            # open json file to read
            json_str = file_obj.read()
            # loads the data and convert it into dictionary format
            new_json_value = json.loads(json_str)

        # add new entry
        new_dict = {"Name": doctor_name, "Id": doctor_id, "specialization": specilization, "Availability": availability}

        # open json file to write
        with open('doctor.json', 'w') as file_obj:
            new_json_value["doctor"].append(new_dict)
            # convert python dictionary to json format string
            file_obj.write(json.dumps(new_json_value, indent=2))

    def view_doctors(self):
        """
         This method is to display all available doctors
        """
        # call function to read file which returns dictionary
        doctor_dict = self.doctor_information()
        # store list of json file in new list doctor_list
        doctor_list = doctor_dict["doctor"]

        print("Available Doctors are:")
        print("----------------------------------------")
        print("Name                    specialization ")
        print("----------------------------------------")

        for i in range(len(doctor_list)):  # Iterate Doctor File
            name = doctor_list[i]["Name"]
            specialization = doctor_list[i]["specialization"]

            print(name, "          ", specialization)

    def addAppointment(self):
        """
         This method is to take appointment by patient
        """
        print("Name of doctors")
        print("---------------")
        # call function to read file which returns dictionary
        doctor_dict = self.doctor_information()
        # store list of json file in new list doctor_list
        doctor_list = doctor_dict["doctor"]

        for i in range(len(doctor_list)):
            name = doctor_list[i]["Name"]
            specialization = doctor_list[i]["specialization"]
            Availability = doctor_list[i]['Availability']
            print(name, " ", specialization, " ",
                  Availability)  # using index i prints name of doctor from doctor_list['Name']

        doctor_name = input("Name of Doctor to take appointment(i.e Dr. Armaan Malik)??")  # doctor name as input
        time: str = input("please Enter appointment time..(AM/PM/Both) :")

        appointment_dict = self.appoinment()  # read appointment json.
        appointment_list = appointment_dict[doctor_name]  # store all patients of 1 doctor in list.

        print("this is appointment list ", appointment_list)
        # check each doctor has maximum 5 patient
        if len(appointment_list) < 5:
            for i in range(len(doctor_list)):
                if doctor_list[i]["Name"] == doctor_name:
                    if time.upper() == doctor_list[i]["Availability"]:
                        print("Doctor is available..!! Please Enter the patient details:")
                        name = input("Enter patient name:")
                        id = int(input("Enter patient Id:"))
                        age = int(input("Enter patient age:"))
                        mob_no = input("Enter patient's mobile number:")

                        with open('appointment.json', 'r') as file_obj:
                            json_str = file_obj.read()
                            # loads the data and convert it into dictionary format
                            new_json_value = json.loads(json_str)

                            # add new entry
                        new_dict = {"patient Name": name, "Id": id, "Age": age, "mobile number": mob_no, "time": time}

                        # open json file to write
                        with open('appointment.json', 'w') as file_obj:
                            new_json_value[doctor_name].append(new_dict)
                            # convert python dictionary to json format string
                            file_obj.write(json.dumps(new_json_value, indent=2))

                        print("Your appointment is fixed. Thank You !")

                    else:
                        print("Sorry. Doctor is not available..!! ")

    def searchDoctorbyName(self):
        """
         This method is to search the doctor by name to check the availability of doctor
        """
        doctor_dict = self.doctor_information()
        doctor_list = doctor_dict["doctor"]
        name = input("Enter doctor name you want to search (i.e Dr.Drake Ramoray ):")
        for i in range(len(doctor_list)):
            # check entered name is equal to name in file
            if name == doctor_list[i]["Name"]:
                print(name, " works for this Clinique..!!")
                break
            else:
                print("We don't have any doctor named :", name)
                break

    def searchDoctorbyId(self):
        """
         This method is to search the doctor by Id to check the availability of doctor
        """
        doctor_dict = self.doctor_information()
        doctor_list = doctor_dict["doctor"]
        # check entered id is equal to id in file
        id = int(input("Enter doctor Id you want to search:"))
        for i in range(len(doctor_list)):
            if id == doctor_list[i]["Id"]:
                print("Doctor is available..!!")
                break
            else:
                print("Doctor is not available..!!")
                break

    def search_doctor_by_Specialization(self):
        """
        This method is to search the doctor by specialization to check the availability of doctor
        """
        doctor_dict = self.doctor_information()
        doctor_list = doctor_dict["doctor"]
        specialization = input("Enter doctor specialization you want to search:")
        for i in range(len(doctor_list)):
            # check entered specialization is equal to specialization in file
            if specialization == doctor_list[i]["specialization"]:
                print("Doctor is available..!!")
                break
            else:
                print("Doctor is not available..!!")
                break


if __name__ == '__main__':
    cliniqueobj = CliniqueManagement()

    patient_file = cliniqueobj.paitent_information()
    # print(patient_file)
    appointment_file = cliniqueobj.appoinment()
    # print(appointment_file)

cliniqueobj.UserInput()
