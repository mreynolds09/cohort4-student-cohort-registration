import sqlite3


connection = sqlite3.connect('my_database.db')
db_cursor = connection.cursor()
    
def create_schema():
    with open('schema.sql', 'rt') as sql_queries:
    
        queries = sql_queries.read()
        db_cursor.executescript(queries)
        
        connection.commit()

create_schema()


def view_all_people(where=None):    
    if where:
        rows = db_cursor.execute("SELECT * FROM People WHERE person_id LIKE ?", (where)).fetchall()
        
    else:   
        rows = db_cursor.execute("SELECT * FROM People",)
    
    headers = [
        "Person_ID",
        "first_name",
        "last_name",
        "email",
        "phone",
        "password",
        "address",
        "city",
        "state",
        "Zip_code",
        "Active",
    
    ]

    print(
        #  id             firstn           lastn        email           phone         password        address        city          state          Zipcode        active
        f"{headers[0]:10}{headers[1]:12}{headers[2]:12}{headers[3]:30}{headers[4]:15}{headers[5]:20}{headers[6]:15}{headers[7]:10}{headers[8]:10}{headers[9]:10}{headers[10]}")
    print(
        f'{"---------":10}{"---------":12}{"---------":12}{"---------":30}{"-----":15}{"---------":20}'
    )

    for row in rows:
        row = [str (i) for i in row]
        print(
            f"{row[0]:10}{row[1]:12}{row[2]:12}{row[3]:30}{row[4]:15}{row[5]:20}{row[6]:15}{row[7]:10}{row[8]:10}{row[9]:10}{row[10]}")


def view_all_cohorts(where=None):
    if where:
        rows = db_cursor.execute("SELECT * FROM Cohorts WHERE cohort_id LIKE ?", (where)).fetchall()
                                    
    else:   
        rows = db_cursor.execute("SELECT * FROM Cohorts",)
    
    headers = [
        "cohort_id",
        "instructor_id", 
        "course_id", 
        "start_date", 
        "end_date", 
        "active"
    
    ]

    print(
        #  cohortid    insturctor_id   course_id    start_date       end_date     active                        
        f"{headers[0]:15}{headers[1]:15}{headers[2]:20}{headers[3]:20}{headers[4]:15}{headers[5]:}")
    print(
        f'{"------------":15}{"---------":15}{"-----------------":20}{"---------":20}{"-----":15}{"---------"}'
    )

    for row in rows:
        row = [str (i) for i in row]
        print(
            f"{row[0]:15}{row[1]:15}{row[2]:20}{row[3]:20}{row[4]:15}{row[5]:}")
     


def view_all_active_people(where=None):    
    if where:
        rows = db_cursor.execute("SELECT * FROM People WHERE active LIKE 1", (where)).fetchall()
        
    else:   
        rows = db_cursor.execute("SELECT * FROM People",)
    
    headers = [
        "Person_ID",
        "first_name",
        "last_name",
        "email",
        "phone",
        "password",
        "address",
        "city",
        "state",
        "Zip_code",
        "Active",
    
    ]

    print(
        #  id             firstn           lastn        email           phone         password        address        city          state          Zipcode        active
        f"{headers[0]:10}{headers[1]:12}{headers[2]:12}{headers[3]:30}{headers[4]:15}{headers[5]:20}{headers[6]:15}{headers[7]:10}{headers[8]:10}{headers[9]:10}{headers[10]}")
    print(
        f'{"---------":10}{"---------":12}{"---------":12}{"---------":30}{"-----":15}{"---------":20}'
    )

    for row in rows:
        row = [str (i) for i in row]
        print(
            f"{row[0]:10}{row[1]:12}{row[2]:12}{row[3]:30}{row[4]:15}{row[5]:20}{row[6]:15}{row[7]:10}{row[8]:10}{row[9]:10}{row[10]}")    

def view_all_stu_cohrt_reg(where=None):
    if where:
        rows = db_cursor.execute("SELECT * FROM Student_Cohort_Reg WHERE student_id LIKE ?", (where)).fetchall()
                                    
    else:   
        rows = db_cursor.execute("SELECT * FROM Student_Cohort_Reg",)
    
    headers = [
        "student_id",
        "cohort_id",
        "registration_date",
        "completion_date",
        "drop_date",
        "active"
    
    ]

    print(
        #  student_id    cohort_id   registration_date  completion_date drop_date     active                        
        f"{headers[0]:15}{headers[1]:15}{headers[2]:20}{headers[3]:20}{headers[4]:15}{headers[5]:}")
    print(
        f'{"-----------":15}{"----------":15}{"-----------------":20}{"------------------":20}{"--------":15}{"-----"}'
    )

    for row in rows:
        row = [str (i) for i in row]
        print(
            f"{row[0]:15}{row[1]:15}{row[2]:20}{row[3]:20}{row[4]:15}{row[5]:}")
     


def view_all_courses(where=None):
    if where:
        rows = db_cursor.execute("SELECT * FROM Courses WHERE course_id LIKE ?", (where)).fetchall()
                                    
    else:   
        rows = db_cursor.execute("SELECT * FROM Courses",)
        
        headers = [
            "course_id",
            "name",
            "description",
            "active"
        
        ]

        print(
            #  course_id      name         description     active                                   
            f"{headers[0]:10}{headers[1]:30}{headers[2]:58}{headers[3]}")
        print(
            f'{"---":10}{"-----------------------":30}{"-------------------------------------------------------":58}{"-------"}'
        )

        for row in rows:
            row = [str (i) for i in row]
            print(
                f"{row[0]:10}{row[1]:30}{row[2]:58}{row[3]}")


def create_people():
    with open('People.sql', 'rt' ,) as sql_queries:
        
        queries = sql_queries.read()
        db_cursor.executescript(queries)
        
create_people()
        
        
def create_cohorts():
    with open('Cohorts.sql', 'rt' ,) as sql_queries:
        
        queries = sql_queries.read()
        db_cursor.executescript(queries)
    
        
create_cohorts()      


 
def create_course():
   
    with open('courses.sql', 'rt',) as sql_queries:
        # print('Adding a Course')
        queries = sql_queries.read()
        db_cursor.executescript(queries)
       
        
create_course()       
                

def assign_stud_to_cohort():
    with open('Student_Cohort_Reg.sql',  'rt') as sql_queries:
        print('Creating Student Cohort Registration')
        sql_queries = sql_queries.read()
        db_cursor.executescript(sql_queries)
assign_stud_to_cohort()

def remove_stud_from_cohort():
    sql_Delete_query = """DELETE FROM Student_Cohort_Reg WHERE student_id = ?"""
    # row to delete
    
    db_cursor.execute(sql_Delete_query, (student_id,))
    connection.commit()
    
    return


def view_all_actv_people():
     with open('People.sql', 'rt' ,) as sql_queries:
        
        queries = sql_queries.read()
        db_cursor.executescript(queries)
        

           


while True:
    
    main_inquiry = input('''
     Student Registration Application
------------------------------------------
            Welcome
            
Choose from the following options
1. Create a Person record
2. Create a Course record (A course is a Class)
3. Create a Cohort
4. Assign a Student to a Cohort
5. Remove a Student from a Cohort
6. Deactivate a Course (It can no longer be selected for a new Cohort)
7. Deactivate a Person (They can no longer be selected for new Registrations or as an instructor for a Cohort)
8. Deactivate a Cohort (They can no longer be selected for new student registrations)
9. Complete a Course for a Student. This will set the completion date on the Student_Cohort_Registration.
10. Reactivate Course, Person, Cohort, Student_Cohort_Registration
11. View active registrations for a cohort
12. View active cohorts for a course
13. View all active people
14. Quit Program


Enter an option from the list above\n: > ''')
    if main_inquiry == '1':
        # Create a Person record
        # first_name, last_name, email, phone, password, address, city, state, postal_code, active
        print("Adding a person")
        first_name = input('Enter First Name: ')
        last_name = input('Enter Last Name: ')
        email = input('Enter Email: ')
        phone_num = input('Phone Number: ')
        pass_word = input ('Enter a Password: ')
        address = input ('Enter Street Address: ')
        city = input ('Enter City: ')
        state = input ('Enter State: ')
        postal_code = input ('Enter Zip Code: ')
        active = input ("") 
        db_cursor.execute("""
        INSERT INTO People(first_name, last_name, email, phone, password, address, city, state, postal_code, active)
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (first_name, last_name, email , phone_num, pass_word, address, city, state, postal_code,active))
        connection.commit ()
        print ( 'You have successfuly added a person!' )

        
    elif main_inquiry == '2':    
        # Create a Course record (A course is a Class)
        course_name = input ("Enter Course Name: ")
        course_description = input ('Enter Course Description: ')
        while True:
            active = input ("Enter Yes for active No for not active:")
            if active == 'Yes' or active == 'No':  
                db_cursor.execute("""
                INSERT INTO Courses(name, description, active)
                VALUES (?,?,?)
                """, (course_name, course_description , active))
                print ( 'You have successfuly added a Course!' )
                connection.commit ()
                break  
            if active != 'Yes' or active != 'No':
                print ('not a valid option try again!')    
        
    elif main_inquiry == '3': 
        # Create a Cohort 
        while True:
            user_input = input ('''
            Enter one of the following
            1. Would you like manually create a Cohort?                   
            2. Would you like to create a cohort by searching for someone?                    
                                            
            \n: > ''')
            if user_input == "1":
                print("Manually Adding a Cohort")
                cohort_id = input ("Enter Cohort_ID: ")
                instruc_id = input('Enter instructor_id: ')
                course_id = input('Enter Course ID: ')
                start_date = input('start_date: ')
                end_date = input ('end_date: ')
                active = input ('Active?: ')
                db_cursor.execute("""
                INSERT INTO Cohorts (cohort_id, instructor_id, course_id, start_date, end_date, active)
                VALUES (?,?,?,?,?,?)
                """, (cohort_id, instruc_id, course_id, start_date, end_date, active ))
                print ('You Manually added a Cohort!')
                

            elif user_input == "2":
                print ('Creating a Cohort!')
                people_search = input ("Press Enter to view all people!")
                view_all_people(people_search)
                
                user_input = input("Please Select Person from above list.")
                query = db_cursor.execute (f"SELECT * FROM People WHERE person_id = {user_input}")
                
                for row in (query):
                    print (f'Great Job! you have successfully Selected {row}')
                
                db_cursor.execute (f""" 
                INSERT INTO Cohorts(instructor_id)
                SELECT person_id
                FROM People WHERE person_id = {user_input}
                ; """)
                connection.commit()
                
                view_course = input ("Press Enter to view all courses: ")
                view_all_courses()
                user_input2 = input ("Please Select Course From Above List: ")
                query2 = db_cursor.execute (f"SELECT * FROM Courses WHERE course_id = {user_input2}")

                for row2 in (query2):
                    print (f'Great Job! you have successfully Selected {row2}')
                
                db_cursor.execute (f""" 
                INSERT INTO Cohorts(course_id)
                SELECT course_id
                FROM Courses WHERE course_id = {user_input}
                ; """)
                connection.commit()
    
    
    elif main_inquiry == '4':
        people_search = input ("Press Enter to view all people!")
        view_all_people(people_search)
        user_input = input("Please Select Person as the student using person_id.")
        query = db_cursor.execute (f"SELECT * FROM People WHERE person_id = {user_input}")
        
        for row in (query):
            print (f'Great Job! you have successfully Selected {row}')
                
        db_cursor.execute (f""" 
        INSERT INTO Student_Cohort_Reg(student_id)
        SELECT person_id
        FROM People WHERE person_id = {user_input}
        ; """)
        
        connection.commit()
        
        
    elif main_inquiry == '5':
        
        stu_cohrt_search = input ("Press Enter to view all Student Cohorts: ")
        view_all_stu_cohrt_reg()
        
        student_id = input ("Please Enter Student you want to remove from Cohort by their Student ID: ")
        del_confirm = input (f'Are you sure you want to delete Student ID #{student_id}? ')
        if del_confirm == "Yes":
            del_cust_input = ("DELETE student_id FROM Student_Cohort_Reg WHERE student_id = ?", str(student_id))
            remove_stud_from_cohort()
            print (f'You have successfully removed Student ID #{student_id} ')
        else: 
            continue   
        
    elif main_inquiry == '6':
       
        #  Deactivate a Person (They can no longer be selected for new Registrations or as an instructor for a Cohort)
        
        view_all_courses()
        user_input = input("Please Select Course from above list.")
        query = db_cursor.execute (f"SELECT * FROM Courses WHERE course_id = {user_input}")
        for row in (query):
            print (f'Great Job! you have successfully Selected {row}')
        db_cursor.execute (f"""UPDATE Courses
        SET active = '0' WHERE course_id = {user_input}; """)
        connection.commit()
    
    elif main_inquiry == '7':
        
        #  Deactivate a Person (They can no longer be selected for new Registrations or as an instructor for a Cohort)
        
        view_all_people()
        user_input = input("Please Select Person from above list.")
        
        update_query = "UPDATE People SET active = '0' WHERE person_id = ?;"
        result = db_cursor.execute (update_query, (user_input,)).fetchone()
        connection.commit()
                
    
    elif main_inquiry == '8': 
        
        
        view_all_cohorts()
        user_input = input("Please Select Cohort from above list Using Cohort_id.")
        query = db_cursor.execute (f"SELECT * FROM Cohorts WHERE cohort_id = {user_input}")
                
        for row in (query):
            print (f'Great Job! you have successfully Selected {row}')
        db_cursor.execute (f"""UPDATE Cohorts
        SET active = '0' WHERE cohort_id = {user_input}; """)
        connection.commit()
    
    elif main_inquiry == '9':
        search_cohort = input ("Press enter to view all student cohorts: ")
        view_all_stu_cohrt_reg()
        user_input = input("Please Select Student that you would like to add Course  Completion to: ")
        # query = db_cursor.execute 
        
        query =  "UPDATE Student_Cohort_Reg SET completion_date = current_date  WHERE student_id = ?"
        
        
        result = db_cursor.execute(query, (user_input,)).fetchone()
        
        print (f'Great Job! {user_input} has successfully completed their course! ')
        
    
    elif main_inquiry == '10':
        
        
        while True:
            reactivate_input = input ('''
            
            Please select what you want to reactivate
            Reactivation
            ------------
            1.Person
            2.Course
            3.Cohort
            4.Student Cohort Registration
            5.Go Back
            
            ''')
            
            if reactivate_input == '1':
               
               
                view_all_people()
                user_input = input("Please Select Person from above list that you want to reactivate.")
                
                update_query = "UPDATE People SET active = '1' WHERE person_id = ?;"
                result = db_cursor.execute (update_query, (user_input,)).fetchone()
                connection.commit()
                
            elif reactivate_input == '2':
                
               
                view_all_courses()
                user_input = input("Please Select Course from above list.")
                query = db_cursor.execute (f"SELECT * FROM Courses WHERE course_id = {user_input}")
                for row in (query):
                    print (f'Great Job! you have successfully Selected {row}')
                db_cursor.execute (f"""UPDATE Courses
                SET active = '1' WHERE course_id = {user_input}; """)
                connection.commit()
    
            elif reactivate_input == '3':
                
                view_all_cohorts()
                user_input = input("Please Select Cohort from above list Using Cohort_id.")
                query = db_cursor.execute (f"SELECT * FROM Cohorts WHERE cohort_id = {user_input}")
                        
                for row in (query):
                    print (f'Great Job! you have successfully Selected {row}')
                db_cursor.execute (f"""UPDATE Cohorts
                SET active = '1' WHERE cohort_id = {user_input}; """)
                connection.commit()
            elif reactivate_input == '4':
                view_all_stu_cohrt_reg()
                user_input = input("Please Select Student from above list that you want to reactivate.")
                
                update_query = "UPDATE Student_Cohort_Reg SET active = '1' WHERE cohort_id = ?;"
                result = db_cursor.execute (update_query, (user_input,)).fetchone()
                connection.commit()
            elif reactivate_input == '5':
                break
        
        
            # view_cohorts = input ("Press Enter to view all cohorts: ")
            # view_all_cohorts()
            # user_input = input("Please Select Cohort from above list Using Cohort_id.")
            # query = db_cursor.execute (f"SELECT * FROM Cohorts WHERE cohort_id = {user_input}")
                    
            # for row in (query):
            #     print (f'Great Job! you have successfully Selected {row}')
            # db_cursor.execute (f"""UPDATE Cohorts
            # SET active = '0' WHERE cohort_id = {user_input}; """)
            # connection.commit()
    
    
    
    elif main_inquiry == '11':
      
        query = db_cursor.execute (f"SELECT * FROM Student_Cohort_Reg WHERE active = 1")
        
        
        headers = [
        "student_id",
        "cohort_id",
        "registration_date",
        "completion_date",
        "drop_date",
        "active"
    
    ]

        print(
            #  student_id    cohort_id   registration_date  completion_date drop_date     active                        
            f"{headers[0]:15}{headers[1]:15}{headers[2]:20}{headers[3]:20}{headers[4]:15}{headers[5]:}")
        print(
            f'{"------------":15}{"---------":15}{"-----------------":20}{"---------":20}{"-----":15}{"---------"}'
        )

        for row in query:
            row = [str (i) for i in row]
            print(
                f"{row[0]:15}{row[1]:15}{row[2]:20}{row[3]:20}{row[4]:15}{row[5]:}")
        connection.commit()
    elif main_inquiry == '12':
        
        query = db_cursor.execute (f"SELECT * FROM Cohorts WHERE active = 1")
              
        
        headers = [
        "student_id",
        "cohort_id",
        "registration_date",
        "completion_date",
        "drop_date",
        "active"
    
    ]

        print(
            #  student_id    cohort_id   registration_date  completion_date drop_date     active                        
            f"{headers[0]:15}{headers[1]:15}{headers[2]:30}{headers[3]:20}{headers[4]:15}{headers[5]:}")
        print(
            f'{"------------":15}{"---------":15}{"-----------------":30}{"---------":20}{"-----":15}{"---------"}'
        )
            
        for row in query:
                row = [str (i) for i in row]
                print(
                    f"{row[0]:15}{row[1]:15}{row[2]:20}{row[3]:20}{row[4]:15}{row[5]:}")
        
        connection.commit()
    elif main_inquiry == '13':
        # view_people = input ("Press Enter to view all active people: ")
        
        
        query = db_cursor.execute (f"SELECT * FROM People WHERE active = 1")
        
        
        headers = [
        "Person_ID",
        "first_name",
        "last_name",
        "email",
        "phone",
        "password",
        "address",
        "city",
        "state",
        "Zip_code",
        "Active",
    
    ]

        print(
            #  id             firstn           lastn        email           phone         password        address        city          state          Zipcode        active
            f"{headers[0]:10}{headers[1]:12}{headers[2]:12}{headers[3]:30}{headers[4]:15}{headers[5]:20}{headers[6]:15}{headers[7]:10}{headers[8]:10}{headers[9]:10}{headers[10]}")
        print(
            f'{"---------":10}{"---------":12}{"---------":12}{"--------------------------":30}{"-----":15}{"---------":20}{"---------":15}{"---------":10}{"-------":10}{"--------":10}{"---------"}'
        )

        for row in query:
            row = [str (i) for i in row]
            print(
                f"{row[0]:10}{row[1]:12}{row[2]:12}{row[3]:30}{row[4]:15}{row[5]:20}{row[6]:15}{row[7]:10}{row[8]:10}{row[9]:10}{row[10]}")
        connection.commit()
    
    elif main_inquiry == '14':
        print("Thanks for stopping by!")
        break
    else:
        print("That is not a valid option")

        




   
   














   




        
                
            
                
                
                

                
                
               
            
        

        
       
       



        
        
        
        
