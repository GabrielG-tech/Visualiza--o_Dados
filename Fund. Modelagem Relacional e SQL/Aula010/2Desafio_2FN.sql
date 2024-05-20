CREATE TABLE IF NOT EXISTS students (
  studentID INT PRIMARY KEY,
  studentName VARCHAR(100)  
);

CREATE TABLE IF NOT EXISTS course (
  courseID INT PRIMARY KEY,
  courseName VARCHAR(100),
  instructorName VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS periodo (
  studentID INT,
  courseID INT,  
  grade VARCHAR(5),
  semester VARCHAR(20),    
  PRIMARY KEY (studentID, courseID),
  FOREIGN KEY (studentID) REFERENCES students(studentsID),
  FOREIGN KEY (courseID)  REFERENCES course(courseID)
);

INSERT OR IGNORE INTO students (studentID, studentName) VALUES
  (1, 'Alice Smith'),
  (2, 'Bob Johnson'),
  (3, 'Carol White');

INSERT OR IGNORE INTO course (courseID, courseName, instructorName) VALUES
  (101, 'Mathematics','Dr. John Doe'),
  (102, 'Physics'    ,'Dr. Jane Roe'),
  (103, 'Chemistry'  ,'Dr. John Doe');

INSERT OR IGNORE INTO periodo (studentID, courseID, grade, semester) VALUES
  (1,101,'A','Fall 2023'),
  (2,102,'B','Fall 2023'),
  (1,103,'B','Spring 2024'),
  (3,101,'A','Fall 2023'),
  (2,101,'C','Spring 2024');
  
SELECT 
  p.studentID, 
  s.studentName, 
  p.courseID, 
  c.courseName,
  c.instructorName, 
  p.grade,
  p.semester
FROM 
  periodo p
JOIN 
  students s ON p.studentID = s.studentID
JOIN 
  course c   ON p.courseID  = c.courseID;
