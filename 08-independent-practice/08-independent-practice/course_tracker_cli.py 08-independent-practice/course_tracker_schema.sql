DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    module_name TEXT NOT NULL,
    teacher TEXT NOT NULL,
    semester TEXT NOT NULL,
    status TEXT NOT NULL,
    grade TEXT NOT NULL,
    notes TEXT    
);

INSERT INTO courses
(id, module_name, teacher, semester, status, grade, notes)
VALUES
(1, 'Math', 'Arthur', 'Semester 1', 'In progress', 'A+', "I like Math"),
(2, 'Software', 'Ali', 'Semester 2', 'Completed', 'A', "Software is most important module"),
(3, 'AI', 'Luke', 'Semester 1', 'Not started', 'N/A', "I will try to pass this module"),
(4, 'Game dev', 'altan', 'Semester 2', 'Failed', 'F', "I will try harder next time")


