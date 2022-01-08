#####################################################################################
########### jakhon37 ##########
###########  Project ##########
########### Student Record System #########
######################################################################################


import os
import pandas as pd
from pandas import DataFrame
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Student:
    studentList = []

    print("      ------------------")
    print("   --------------------------")
    print("--------------------------------")
    print("Welcome to Student Record System")
    print("--------------------------------")
    print("------Nodirov Jakhongir--------")
    print("--------------------------------")
    print("   --------------------------")
    print("      -------------------")

    # LOAD DATA
    def __init__(self):
        # self.C = []
        self.load()

    def load(self):
        print(' Loading Students List')
        if not os.path.exists('studentRecords.txt'):
            print(' Skipping, nothing to load')
            return
        try:
            self.studentList = pd.read_fwf('studentRecords.txt', delim_whitespace=False, header=0, index_col=0)
            print(' Loaded!')
        except:
            print("No date in list")
            self.studentList = pd.DataFrame({'ID': 0, 'Name': '0', 'Gender': 0, 'Age': 0, 'EnrolmentData': '0', 'MidtermScore': 0, 'FinalScore': 0},
                                     index=[0])
            with open("studentRecords.txt", "w") as f:
                self.studentList = DataFrame(self.studentList)
                df_marks3 = self.studentList.to_string()
                f.write(df_marks3)
            print('New list Created!')



    # ADD STUDENT
    def add(self):
        new_row = {'ID': 0, 'Name': '0', 'Gender': 0, 'Age': 0, 'EnrolmentData': '0', 'MidtermScore': 0, 'FinalScore': 0}
        for i in new_row:
            if i == 'ID':
                value = input("Enter ID: ")
            elif i == 'Name':
                value = input("Enter Name: ")
            elif i == 'Gender':
                value = int(input("Enter Gender (0: male; 1:female) : "))
            elif i == 'Age':
                value = int(input("Enter Age: "))
            elif i == 'EnrolmentData':
                value = input("Enter Enrolment Date: ")
            elif i == 'MidtermScore':
                value = int(input("Enter Midterm Score: "))
            elif i == 'FinalScore':
                value = int(input("Enter Final Score: "))
            else:
                print('Please choose right option!')

            new_row[i] = value
        new_row['GPA'] = 0
        self.studentList = self.studentList.append(new_row, ignore_index=True)
        print(f'Students Student: {new_row}')

    # CALCULATE AND UPDATE GPA
    def cal_gpa(self):
        for _ in self.studentList['GPA']:
            mid_score = self.studentList['MidtermScore']
            final_score = self.studentList['FinalScore']
            gpa = 0.4 * mid_score + 0.6 * final_score
            self.studentList['GPA'] = gpa
        print('GPA has been successfully updated!')

    # UPDATE LIST OF STUDENTS
    def update(self):
        id_student = int(input("Please enter students' id to update their info :"))
        df = self.studentList
        df1 = df.index[df['ID'] == id_student].tolist()
        upd_info = input('Please choose what do you wand to update:\n'
                         'ID=1 \n'
                         'Name=2\n'
                         'Gender=3\n'
                         "Age=4\n"
                         "Enroll=5\n"
                         'Midterm=6\n'
                         'Final=7\n'
                         ':   ')
        if upd_info == '1':
            new_n = input('Enter new ID: ')
            df.at[df1, 'ID'] = new_n
            print("You have changed ID")
        elif upd_info == '2':
            new_n = input('Enter new Name: ')
            df.at[df1, 'Name'] = new_n
            print("You have changed Name")
        elif upd_info == '3':
            new_n = input('Enter new Gender: ')
            df.at[df1, 'Gender'] = new_n
            print("You have changed Gender")
        elif upd_info == '4':
            new_n = input('Enter new Age: ')
            df.at[df1, 'Age'] = new_n
            print("You have changed Age")
        elif upd_info == '5':
            new_n = input('Enter new Enrollment date: ')
            df.at[df1, 'EnrolmentData'] = new_n
            print("You have changed Enrollment date")
        elif upd_info == '6':
            new_n = int(input('Enter new Midterm Score: '))
            df.at[df1, 'MidtermScore'] = new_n
            print("You have changed Midterm Score")
        elif upd_info == '7':
            new_n = int(input('Enter new Final Score: '))
            df.at[df1, 'FinalScore'] = new_n
            print("You have changed Final Score")
        else:
            print('Please choose valid option!')

    # PRINT LIST
    def print_all(self):
        print(self.studentList)

    # CALCULATE GRADUATION DATE
    def calculate_grad_date(self):
        id_student = int(input("Please enter students' id to check graduation date:  "))
        df = self.studentList
        df1 = df.index[df['ID'] == id_student].tolist()
        df2 = df1[0]
        data_of_enrl = df.at[df2, 'EnrolmentData']
        print("Enrolment data of the student is: " + data_of_enrl)
        study_year = int(input("Please enter students' duration of study:  "))
        format_string = "%Y/%m/%d"
        datetime_object = datetime.strptime(data_of_enrl, format_string).date()
        new_date = datetime_object + relativedelta(years=study_year)
        new_date_string = datetime.strftime(new_date, format_string).replace(' 0', ' ')
        print("Graduation data of the student is: " + new_date_string)

    # SAVE THE DATA TO studentRecords.txt
    def save_to_disk(self):
        print(" Saving the Students' list ")

        with open("studentRecords.txt", "w") as f:
            self.studentList = DataFrame(self.studentList)
            df_marks3 = self.studentList.to_string()
            f.write(df_marks3)
        print(' Saved!')


# RUN THE PROGRAM
def main():
    inv = Student()

    while True:
        action = input('Actions:\n'
                       ' 1 -> Add new student\n'
                       ' 2 -> Update GPA\n'
                       ' 3 -> Update list\n'
                       ' 4 -> Show list\n'
                       ' 5 -> Show Graduation Data \n'
                       ' 6 -> Save\n'
                       ' 7 -> Exit \n'
                       'Choose one of the options:   ')
        if action == '7':
            break
        if action == '1':
            inv.add()
        if action == '2':
            inv.cal_gpa()
        if action == '3':
            inv.update()
        if action == '4':
            inv.print_all()
        if action == '5':
            inv.calculate_grad_date()
        if action == '6':
            inv.save_to_disk()
    inv.save_to_disk()


if __name__ == '__main__':
    main()
