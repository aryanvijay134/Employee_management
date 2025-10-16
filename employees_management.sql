CREATE DATABASE employees_management;
USE employees_management;

CREATE TABLE department (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO department (dept_name) VALUES
('HR'),
('Finance'), 
('IT'), 
('Marketing');

SELECT * FROM department;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dept_id INT NOT NULL,
    doj DATE NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(10) NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

INSERT INTO employees (emp_id, name, dept_id, doj, email, password, phone)
VALUES
(101, 'John Doe', 3, '2023-01-15', 'johndoe@gmail.com', 'Ary@1234', '1234567891'),
(102, 'Jane Smith', 1, '2022-08-01', 'janesmith@gmail.com', 'Ary@1234', '1234567892'),
(103, 'Alias', 4, '2023-10-11', 'alias@gmail.com', 'Ary@1234', '1234567892'),
(104, 'Bob', 1, '2020-08-23', 'bob@gmail.com', 'Ary@1234', '1234567892'),
(105, 'Casey', 1, '2012-12-09', 'casey@gmail.com', 'Ary@1234', '1234567892'),
(106, 'Donald', 2, '2024-03-11', 'donald@gmail.com', 'Ary@1234', '1234567892'),
(107, 'Elizabeth', 4, '2022-01-17', 'elizabeth@gmail.com', 'Ary@1234', '1234567892'),
(108, 'Frank', 3, '2019-12-12', 'frank@gmail.com', 'Ary@1234', '1234567892');

SELECT*FROM employees;




	