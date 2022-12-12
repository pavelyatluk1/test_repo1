-- Pavlo Yatluk
-- dz_17
-- #1. Напишіть запит, щоб порахувати кількість вакансій,
-- доступних у таблиці employees.

use pds;
select count(distinct JOB_ID) from employees;

-- #2. Напишіть запит, щоб отримати середню ЗП та кількість
-- працівників відділу 90.

use pds;
SELECT avg(SALARY), count(*) FROM employees WHERE DEPARTMENT_ID = 90;

-- #3. Напишіть запит, щоб отримати  кількість
-- працівників за тією самою роботою.

use pds;
SELECT JOB_ID, COUNT(*) FROM employees GROUP BY JOB_ID;

-- #4. Напишіть запит, щоб вивести ім'я і прізвище співробітника,
-- код і повну назву ВІДДІЛУ.

use pds;
SELECT first_name, last_name, department_id, department_name
FROM employees
JOIN departments USING (department_id);

-- #5. Напишіть запит, щоб вивести ім'я і прізвище, роботу,
-- ідентифікатор відділу та імена співробітниуів, які
-- працюють у Лондоні.

use pds;
SELECT e.first_name, e.last_name, e.job_id, e.department_id
FROM employees e
JOIN departments d
ON (e.department_id = d.department_id)
JOIN locations l ON
(d.location_id = l.location_id)
WHERE LOWER(l.city) = 'London';