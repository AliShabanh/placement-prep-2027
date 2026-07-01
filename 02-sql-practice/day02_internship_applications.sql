-- Day 2 SQL Practice
-- Topic: Internship Applications Table
-- Goal: Practise CREATE TABLE, INSERT, SELECT, WHERE, ORDER BY, COUNT, GROUP BY, and LIMIT

DROP TABLE IF EXISTS applications;

CREATE TABLE applications (
    id INTEGER PRIMARY KEY,
    company TEXT NOT NULL,
    role_title TEXT NOT NULL,
    location TEXT NOT NULL,
    work_mode TEXT NOT NULL,
    status TEXT NOT NULL,
    deadline TEXT,
    applied_date TEXT,
    salary TEXT,
    notes TEXT
);

INSERT INTO applications
(id, company, role_title, location, work_mode, status, deadline, applied_date, salary, notes)
VALUES
(1, 'Microsoft', 'Software Engineering Intern', 'Dublin', 'Hybrid', 'Interested', '2026-09-30', NULL, 'Unknown', 'Focus on Python, cloud, and backend skills'),

(2, 'Google', 'STEP Intern', 'Dublin', 'Hybrid', 'Interested', '2026-10-15', NULL, 'Unknown', 'Check eligibility and application opening date'),

(3, 'Amazon', 'Software Development Engineer Intern', 'Dublin', 'Hybrid', 'Interested', '2026-10-20', NULL, 'Unknown', 'Practise data structures and algorithms'),

(4, 'Workday', 'Software Application Development Intern', 'Dublin', 'Hybrid', 'Interested', '2026-11-01', NULL, 'Unknown', 'Good match for software and backend'),

(5, 'Accenture', 'Technology Intern', 'Dublin', 'Hybrid', 'Interested', '2026-10-10', NULL, 'Unknown', 'Could include consulting, software, cloud, or data'),

(6, 'IBM', 'Data and AI Intern', 'Dublin', 'Hybrid', 'Interested', '2026-10-05', NULL, 'Unknown', 'Could fit Python, data, and AI interest');

-- Show all application records
SELECT *
FROM applications;

-- Show selected columns only
SELECT company, role_title, status
FROM applications;

-- Show roles located in Dublin
SELECT company, role_title, location
FROM applications
WHERE location = 'Dublin';

-- Show software-related roles
SELECT company, role_title
FROM applications
WHERE role_title LIKE '%Software%';

-- Sort applications by earliest deadline
SELECT company, role_title, deadline
FROM applications
ORDER BY deadline ASC;

-- Count all applications
SELECT COUNT(*) AS total_applications
FROM applications;

-- Count applications by status
SELECT status, COUNT(*) AS total
FROM applications
GROUP BY status;

-- My challenge queries

SELECT company, deadline
FROM applications;

SELECT company, role_title, status
FROM applications
WHERE status = 'Interested';

SELECT company, role_title
FROM applications
WHERE company LIKE 'A%';

SELECT company, role_title, deadline
FROM applications
WHERE deadline > '2026-10-20'
ORDER BY deadline ASC;

SELECT COUNT(*) AS dublin_roles
FROM applications
WHERE location = 'Dublin';

SELECT company, role_title
FROM applications
WHERE role_title LIKE '%Backend%'
   OR notes LIKE '%backend%';

SELECT company, role_title
FROM applications
WHERE role_title LIKE '%Technology%'
   OR role_title LIKE '%Engineering%';

SELECT company, role_title
FROM applications
ORDER BY company DESC;

SELECT company, role_title, deadline
FROM applications
ORDER BY deadline ASC
LIMIT 3;

SELECT company, role_title, salary
FROM applications
WHERE salary = 'Unknown';