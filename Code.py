#These are the list of dependencies
import pymysql


class Admin:    
    def __init__(self):
        print("Welcome Admin")
        print("Enter the number for what you want to see below")
        while(True):
            print("1. Get student data\n2. Get Company Data\n3. Prepare eligible student list\n4. Share Recruitment Details\n5. Delete Records\n6. Get Job Postings\n7. Exit Admin\n")
            choice = int(input())
            if(choice == 1):
                self.__get_student_data()
            elif(choice == 2):
                self.__get_company_data()
            elif(choice == 3):
                self.__prepare_eligible_list()
            elif(choice == 4):
                self.__share_recruitment_details()
            elif(choice ==5):
                self.__deleterecords()
            elif(choice == 6):
                self.__get_job_postings()
            elif(choice == 7):
                return
    
    #FUNCTION GET STUDENT DATA
    def __get_student_data(self):
        #database connection establishment
        connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        #Writing the query to fetch the details of student
        entiretab = "SELECT NAME,ROLLNO,EMAIL,STREAM,YEAR,GPA FROM student"
        cursor.execute(entiretab)
        rows = cursor.fetchall()
        #Printing the details of the students
        for r in rows:
            print(r)
        return
        
    #Function to get company data
    def __get_company_data(self):
        #database connection
        connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        #Query to fetch the details of the company
        entiretab = "SELECT company_name,company_id FROM company"
        cursor.execute(entiretab)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        return

    #Function to get the eligible students list 
    def __prepare_eligible_list(self):
        #Similar database connection
        connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        #Need an input for the minimum gpa requirement from admin
        val = float(input("Enter the GPA for eligibility for placement"))
        query = "Delete from student_eligible"
        cursor.execute(query)
        connection.commit()
        entiretab = "insert ignore into student_eligible  (select * from student where gpa > {})".format(val)
        cursor.execute(entiretab)
        connection.commit()
        print("The Eligibility list has been prepared for the placement season")
        return

    #Function which gives the admin the choice to share recruitment details
    def __share_recruitment_details(self):
        Recruitment_Task_obj = Recruitment_Task()

    #Function to get the records of the students who cleared a round
    #This will be updated by an examination system
    def __record_cleared_student_data(self):
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        entiretab = "SELECT * from cleared_students"
        cursor.execute(entiretab)
        rows = cursor.fetchall()
        print(rows)
        return
    # Share Recruitment Details Functions
    def __check_eligibility(self):
        connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        entiretab = "SELECT name,rollno,email,stream,year,gpa FROM student_eligible"
        cursor.execute(entiretab)
        rows = cursor.fetchall()
        print("The eligible students are:\n\n")
        for r in rows:
            print(r)
        print("\n")
        return

    #Function to get the date and time of the placement tests
    def __get_date_time(self):
        print("The students have been informed about the test")
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        #The details of the test are present in the test_details table
        entiretab = "SELECT * from test_details"
        cursor.execute(entiretab)
        rows = cursor.fetchall()
        print(rows)
        return

    #Function to get the list of student who appeared for the test
    #This will be externally updated by an examination system
    def __record_appeared_student_data(self):
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        #The details of the appeared student  are present in the appeared_students table
        entiretab = "SELECT * from appeared_students"
        cursor.execute(entiretab)
        rows = cursor.fetchall()
        print(rows)
        return

    #FUNCTION TO DELETE RECORDS
    def __deleterecords(self):
        print("Which records would you like to delete")
        while(True):
            choice = int(input("1. Student\n2. Company\n3. Job Posting\n4. Exit Deletion\n"))
            if(choice == 1):
                rollo = input("Enter the Roll Number which you'd like to delete")
                connection = pymysql.connect(
                host="localhost", user="root", passwd="", database="mydb")
                cursor = connection.cursor()
                #Writing the query to fetch the details of student
                entiretab = "DELETE FROM student WHERE ROLLNO={}".format(rollo)
                cursor.execute(entiretab)
                connection.commit()
                print("Record deleted")
            elif(choice == 2):
                compid = input("Enter the Company ID which you'd like to delete")
                connection = pymysql.connect(
                host="localhost", user="root", passwd="", database="mydb")
                cursor = connection.cursor()
                #Writing the query to fetch the details of student
                entiretab = "DELETE FROM company WHERE company_id={}".format(compid)
                cursor.execute(entiretab)
                connection.commit()
                print("Record deleted")
            elif(choice == 3):
                jid = input("Enter the Job ID which you'd like to delete")
                connection = pymysql.connect(
                host="localhost", user="root", passwd="", database="mydb")
                cursor = connection.cursor()
                #Writing the query to fetch the details of student
                entiretab = "DELETE FROM job WHERE job_id='{}'".format(jid)
                cursor.execute(entiretab)
                connection.commit()
                print("Record deleted")
            elif(choice == 4):
                break
            else:
                print("Please Enter a valid choice")

    #FUNCTION TO GET JOB POSTINGS
    def __get_job_postings(self):
        #database connection establishment
        connection = pymysql.connect(
        host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        #Writing the query to fetch the details of student
        entiretab = "SELECT * FROM job"
        cursor.execute(entiretab)
        rows = cursor.fetchall()
        #Printing the details of the students
        for r in rows:
            print(r)
        return   

class Recruitment_Task(Admin):
    def __init__(self):
        print("Enter the number for what you want to see below")
        while(True):
            print("1. Check Eligibility of students\n2. Display Test date,time,venue\n3. Record appeared students data\n4. Record students data who cleared test\n5. Exit")
            choice = int(input())
            if(choice == 1):
                self.__check_eligibility()
            elif(choice == 2):
                self.__get_date_time()
            elif(choice == 3):
                self.__record_appeared_student_data()
            elif(choice == 4):
                self.__record_cleared_student_data()
            elif(choice == 5):
                return
    def __check_eligibility(self):
        self._Admin__check_eligibility()
        return
    def __get_date_time(self):
        self._Admin__get_date_time()
        return
    def __record_appeared_student_data(self):
        self._Admin__record_appeared_student_data()
        return
    def __record_cleared_student_data(self):
        self._Admin__record_cleared_student_data()
        return

class Student:
    def __init__(self):
        #student 
        print("Hello Student, Welcome to the Recruitment Portal")
        print("Login by Entering your roll number and password or enter 1 to exit")
        if (self.__student_login() == True):
            while(True):
                print("1. View Recruitment details\n2. Register for job profile\n3. View Test Details\n4. View Result of rounds\n5. Exit from profile")
                choice = int(input())
                if(choice == 1):
                    self.__view_recruitment_details()
                elif(choice == 2):
                    self.__register_for_company_profile()    
                elif(choice == 3):
                    self.__view_test_details()
                elif(choice == 4):
                    self.__views_result_of_round()
                elif(choice == 5):
                    print("You have LOGGED OUT from your profile")
                    break
        return

    def __student_login(self):
        #Function for the checking of student login
        print("Roll Number :", end=' ')
        rn = input()
        if(rn == '1'):
            return
        print("Password :", end=' ')
        password = input()
        connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        #Query to get student details
        entiretab = "SELECT name,rollno,email,stream,year,gpa FROM student_eligible where rollno='" +rn+"'and password= '" + password+"'"
        cursor.execute(entiretab)
        rows = cursor.fetchone()
        if(rows is None):
            print("Invalid user")
            print("\nEnter details again or press 1 to exit from Student")
            return False
        else:
            #Printing the details of the students
            name, rollno, email, stream, year, gpa = rows
            print("\n\nWelcome, ", name)
            print("\nROLL NO:", rollno, end='\t')
            print("EMAIL: ", email, end='\t')
            print("\nSTREAM: ", stream, end='\t')
            print("YEAR: ", year, end='\t')
            print("YOUR GPA IS ", gpa)
            return True

    #Responsible for fetching the jobs posted on
    def __view_recruitment_details(self):
        connection = pymysql.connect(
        host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        #Query is written below
        entiretab = "SELECT company_name,location,job_id,job_description,nopos,salary,gpa_req from job natural join company"
        cursor.execute(entiretab)
        rows = cursor.fetchall()
        print("The following Jobs have been posted :\n")
        print(rows)
        print("\n")

    #Function to register for the company profile
    def __register_for_company_profile(self):
        print("Enter the job ID for which you would like to apply")
        jid = input()
        print("Enter your roll number")
        roll =int(input())
        connection = pymysql.connect(
        host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        entiretab = "SELECT gpa from student where rollno ={}".format(roll)
        cursor.execute(entiretab)
        rows = cursor.fetchone()
        gpa = rows[0]
        ent = "Select gpa_req from job where job_id like '{}'".format(jid)
        cursor.execute(ent)
        (gpa_req,) = cursor.fetchone()
        if(gpa < gpa_req):
            print("Sorry you're not eligible for this job")
        else:
            q = "Insert into job_reg values({},'{}')".format(roll,jid)
            cursor.execute(q)
            connection.commit()
            print("You have successfully registered for the job")
        return

    #Function that shows the students the details of the upcoming tests
    def __view_test_details(self):
        connection = pymysql.connect(
        host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        ent = "Select * from test_details"
        cursor.execute(ent)
        rows = cursor.fetchall()
        for r in rows:
            print(r)

    #Function that shows the result of the rounds
    #This will be updated by the external examination system
    def __views_result_of_round(self):
        connection = pymysql.connect(
        host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        ent = "Select * from cleared_students"
        cursor.execute(ent)
        rows = cursor.fetchall()
        for r in rows:
            print(r)

class Company:
    def __init__(self):
        print("Hello Company")
        if(self.__company_registration()==True):
            print("Welcome dear Company")
            while(True):
                print("Enter 1. Post Job Profile\n2. Conduct Recruitment Rounds\n3. Display details of drive \n4. Exit")
                c=int(input())
                if(c==1):
                    self.__post_job_profiles()
                    print("THe job profile has been posted")
                elif(c==2):
                    self.__conduct_rounds()
                elif(c==3):
                    self.__details_of_drive()
                elif(c==4):
                    print("LOGGING OUT OF THE COMPANY PROFILE")
                    break
                    return
        else:
            print("INVALID INPUT")
        return

    def __company_login(self):
        print("COMPANY ID :", end=' ')
        rn = input()
        if(rn == '1'):
            return
        print("Password :", end=' ')
        password = input()
        connection = pymysql.connect(
        host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        entiretab = "SELECT company_name,company_id,location FROM company where company_id='" +rn+"'and password= '" + password+"'"
        cursor.execute(entiretab)
        rows = cursor.fetchone()
        if(rows is None):
            print("Invalid user")
            print("\nEnter details again or press 1 to exit from Company")
            return False
        else:
            name,comp_id,location = rows
            print("COMPANy NAME: ",name)
            print("COMPANy ID :",comp_id)
            print("COMPANY LOCATION:",location)
        return True

    #Company registration module
    def __company_registration(self):
        print("Welcome to IIITD Recruitment System")
        print("Register for 1. Recruitment or 2. Login to access the portal")
        c = int(input())
        if(c==1):
            print("Enter the company name: ")
            n = input()
            print("Enter the company ID you received from placement office of IIITD")
            cid = input()
            print("Enter Your Company Location")
            loc = input()
            print("Enter password")
            pas = input()
            connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="mydb")
            cursor = connection.cursor()
            entiretab = "INSERT into company values('{}',{},'{}','{}')".format(n,cid,loc,pas)
            cursor.execute(entiretab)
            connection.commit()
            return True
        else:   
            self.__company_login()
            return True
        return False

    #Module to post job profiles offered by the company
    def __post_job_profiles(self):
        print("Enter Company ID: ")
        cid = int(input())
        print("Enter UNIQUE job ID: ")
        jid = input()
        print("Enter Job description: ")
        jd = input()
        print("Enter positions available: ")
        nop=int(input())
        print("Enter the expected salary: ")
        sal = int(input())    
        print("Enter the GPA criteria for eligibility: ")        
        gpa = float(input())
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        entiretab = "INSERT into job values({},'{}','{}',{},{},{})".format(cid,jid,jd,nop,sal,gpa)
        cursor.execute(entiretab)
        connection.commit()
        return

    #This module is supposed to fetch the details of the students who cleared the test
    def __gather_details_of_cleared(self):
        print("Cleared students table will be updated the examination system")
        return

    #this module is supposed to be called when the tests are to be conducted
    def __conduct_rounds(self):
        print("The rounds will now be conducted !!!")
        print("Appeared students table is created by the examination system")
        self.__gather_details_of_cleared()
        return

    #THe details of the drive can be posted or seen from this module below
    def __details_of_drive(self):
        print("1. See the existing drives or 2. post one")
        choice = int(input())
        if(choice == 1):
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="mydb")
            cursor = connection.cursor()
            entiretab = "SELECT * FROM test_details "
            cursor.execute(entiretab)
            rows = cursor.fetchall()
            print(rows)
        elif(choice == 2): 
            print("Enter the job id whose timing you wish to post")
            jid = input()
            print("Enter the date")
            date = input()
            print("Enter the time in 24 hour format")
            time = input()
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="mydb")
            cursor = connection.cursor()
            query = "Insert into test_details values('{}','{}','{}')".format(jid,date,time)
            cursor.execute(query)
            connection.commit()
        return 
             
###############################################################################################
#Main function 
if __name__ == '__main__':
    while(True):
        print("Enter the type of account you want to login as:")
        print("1. Admin\n2. Student\n3. Company\n4. Exit")
        choice = int(input())
        
        if(choice == 1):
            admin_obj = Admin()
        elif (choice == 2):
            student_obj = Student()
        elif (choice == 3):
            company_obj = Company()
        elif (choice == 4):
            exit()
        else:
            print("Please select any of the above 3 types of users")
###########################################################################################################