CREATE TABLE IF NOT EXISTS People (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    password TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    active INTEGER
);

CREATE TABLE IF NOT EXISTS Cohorts (
        cohort_id INTEGER PRIMARY KEY,
        instructor_id INTEGER,
        course_id INTEGER,
        start_date TEXT,
        end_date REAL,
        active INTEGER
);



CREATE TABLE IF NOT EXISTS Student_Cohort_Reg (
    student_id INTEGER ,
    cohort_id INTEGER ,
    registration_date TEXT NOT NULL,
    completion_date TEXT,
    drop_date TEXT,
    active INTEGER,
    
    FOREIGN KEY (student_id)
        REFERENCES People (student_id),
    FOREIGN KEY (cohort_id)
        REFERENCES Cohorts (cohort_id),
  
    PRIMARY KEY (student_id, cohort_id)
);


CREATE TABLE IF NOT EXISTS Courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    active INTEGER




);