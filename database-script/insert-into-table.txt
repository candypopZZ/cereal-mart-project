-- Suppliers table
INSERT INTO suppliers (supplier_id, supplierName, contactNumber, address, 
productCategory) 
VALUES (1, 'FreshMeats Supply', '0123456789', '123 Jalan Mawar, Kuala Lumpur', 
'meatNseafood');
INSERT INTO suppliers (supplier_id, supplierName, contactNumber, address, 
ProductCategory) 
VALUES (2, 'BakeHouse Distributors', '0125678901', '456 Jalan Sutera, Shah Alam', 
'Bakery');
INSERT INTO suppliers (supplier_id, supplierName, contactNumber, address, 
ProductCategory) 
VALUES (3, 'DairyDelight', '0127890123', '789 Jalan Angsana, Petaling Jaya', 'Dairy');
INSERT INTO suppliers (supplier_id, supplierName, contactNumber, address, 
ProductCategory)
VALUES (4, 'SnackMasters', '0129876543', '12 Jalan Puchong, Kuala Lumpur', 
'Snacks');
INSERT INTO suppliers (supplier_id, supplierName, contactNumber, address, 
ProductCategory) 
VALUES (5, 'Beverage Hub', '0126789012', '34 Jalan Bukit, Penang', 'Beverages');
INSERT INTO suppliers (supplier_id, supplierName, contactNumber, address, 
ProductCategory) 
VALUES (6, 'Beauty and Care Supplies', '0121234567', '56 Jalan Serai, Johor Bahru', 
'Health and beauty');
INSERT INTO suppliers (supplier_id, supplierName, contactNumber, address, 
ProductCategory) 
VALUES (7, 'Gourmet Meats', '0123459876', '78 Jalan Kasturi, Ipoh', 'meatNseafood');
INSERT INTO suppliers (supplier_id, supplierName, contactNumber, address, 
ProductCategory) 
VALUES (8, 'Bakery Pro', '0123487654', '90 Jalan Melur, Melaka', 'Bakery');
INSERT INTO suppliers (supplier_id, supplierName, contactNumber, address, 
ProductCategory) 
VALUES (9, 'Healthy Snacks Co.', '0127893456', '101 Jalan Kenanga, Seremban', 
'Snacks');
INSERT INTO suppliers (supplier_id, supplierName, contactNumber, address, 
ProductCategory) 
VALUES (10, 'Dairy King', '0126782345', '202 Jalan Kemboja, Kuching','Dairy');

-- Employees table
INSERT INTO employees (employee_id, FirstName, LastName, JobPosition, Salary, 
ContactNumber, Email, HireDate)
VALUES (1, 'John', 'Routledge', 'Manager', 65000, '011234567891', 
'john.r@example.com', to_date ('2023-01-15', 'YYYY-MM-DD'));
INSERT INTO employees (employee_id, FirstName, LastName, JobPosition, Salary, 
ContactNumber, Email, HireDate)
VALUES (2, 'Sarah', 'Cameron', 'Sales Associate', 45000, '011234567892', 
'sarah.c@example.com', to_date('2023-02-18', 'YYYY-MM-DD'));
INSERT INTO employees (employee_id, FirstName, LastName, JobPosition, Salary, 
ContactNumber, Email, HireDate)
VALUES (3, 'Pope', 'Heyward', 'Accountant', 50000, '011234567893', 
'pope.h@example.com', to_date('2023-03-22', 'YYYY-MM-DD'));
INSERT INTO employees (employee_id, FirstName, LastName, JobPosition, Salary, 
ContactNumber, Email, HireDate)
VALUES (4, 'Kiara', 'Carrera', 'Marketing Specialist', 48000, '011234567894', 
'kiara.c@example.com',to_date ('2023-04-10', 'YYYY-MM-DD'));
INSERT INTO employees (employee_id, FirstName, LastName, JobPosition, Salary, 
ContactNumber, Email, HireDate)
VALUES (5, 'Rafe', 'Cameron', 'Project Manager', 70000, '011234567895', 
'rafe.c@example.com', to_date('2023-05-14', 'YYYY-MM-DD'));
INSERT INTO employees (employee_id, FirstName, LastName, JobPosition, Salary, 
ContactNumber, Email, HireDate)
VALUES (6, 'JJ', 'Maybank', 'Warehouse Supervisor', 42000, '011234567896', 
'jj.m@example.com',to_date ('2023-06-05', 'YYYY-MM-DD'));
INSERT INTO employees (employee_id, FirstName, LastName, JobPosition, Salary, 
ContactNumber, Email, HireDate)
VALUES (7, 'Ward', 'Cameron', 'Director', 90000, '011234567897', 
'ward.c@example.com', to_date('2023-07-19', 'YYYY-MM-DD'));
INSERT INTO employees (employee_id, FirstName, LastName, JobPosition, Salary, 
ContactNumber, Email, HireDate)
VALUES (8, 'Rose', 'Cameron', 'HR Manager', 55000, '011234567898', 
'rose.c@example.com',to_date ('2023-08-30', 'YYYY-MM-DD'));
INSERT INTO employees (employee_id, FirstName, LastName, JobPosition, Salary, 
ContactNumber, Email, HireDate)
VALUES (9, 'Topper', 'Thornton', 'Sales Representative', 43000, '011234567899', 
'topper.t@example.com',to_date ('2023-09-23', 'YYYY-MM-DD'));
INSERT INTO employees (employee_id, FirstName, LastName, JobPosition, Salary, 
ContactNumber, Email, HireDate)
VALUES (10, 'Barry', 'Cox', 'Security Officer', 40000, '011234567800', 
'barry.c@example.com', to_date('2023-10-11', 'YYYY-MM-DD'));

-- Customers table
INSERT INTO customers (customer_id, FirstName, LastName, ContactNumber,
Address)
VALUES(001, 'Gracie', 'Abrams', '0143978520', '123 Market Street, Suite 5, 
Springfield, IL 62701, USA');
INSERT INTO customers (customer_id, FirstName, LastName, ContactNumber, 
Address)
VALUES (002, 'Ethan', 'Hawke', '0134567890', '456 Elm Street, Apt 2A, Chicago, IL 
60614, USA');
INSERT INTO customers (customer_id, FirstName, LastName, ContactNumber, 
Address)
VALUES (003, 'Maya', 'Rudolph', '0123456789', '789 Oak Drive, Unit 12, Austin, TX 
78701, USA');
INSERT INTO customers (customer_id, FirstName, LastName, ContactNumber, 
Address)
VALUES (004, 'Lily', 'Collins', '0178934567', '321 Maple Avenue, Apt 4C, Miami, FL 
33101, USA');
INSERT INTO customers (customer_id, FirstName, LastName, ContactNumber, 
Address)
VALUES (005, 'Daniel', 'Craig', '0182345678', '159 Cedar Lane, Suite 7, Seattle, WA 
98101, USA');
INSERT INTO customers (customer_id, FirstName, LastName, ContactNumber, 
Address)
VALUES (006, 'Emma', 'Stone', '0156789345', '963 Pine Road, Apt 10, Denver, CO 
80202, USA');
INSERT INTO customers (customer_id, FirstName, LastName, ContactNumber, 
Address)
VALUES (007, 'John', 'Krasinski', '0145698723', '753 Birch Street, Floor 3, Boston, MA 
02108, USA');
INSERT INTO customers (customer_id, FirstName, LastName, ContactNumber, 
Address)
VALUES (008, 'Olivia', 'Wilde', '0162345987', '147 Willow Court, Apt B, New York, 
NY 10001, USA');
INSERT INTO customers (customer_id, FirstName, LastName, ContactNumber, 
Address)
VALUES (009, 'Ryan', 'Gosling', '0198765432', '258 Poplar Avenue, Unit 6, Los 
Angeles, CA 90001, USA');
INSERT INTO customers (customer_id, FirstName, LastName, ContactNumber, 
Address)
VALUES (010, 'Zoe', 'Kravitz', '0123987654', '369 Cypress Boulevard, Suite 9, San 
Francisco, CA 94102, USA');

-- Orders table
INSERT INTO orders (order_id, customer_id, orderDate, totalAmount, paymentStatus, 
orderStatus)
VALUES (26, 009, TO_DATE('2024-09-05', 'YYYY-MM-DD'), 52.50, 'completed', 
'completed');
INSERT INTO orders (order_id, customer_id, orderDate, totalAmount, paymentStatus, 
orderStatus)
VALUES (27, 003, TO_DATE('2024-09-10', 'YYYY-MM-DD'), 75.00, 'pending', 
'pending');
INSERT INTO orders (order_id, customer_id, orderDate, totalAmount, paymentStatus, 
orderStatus)
VALUES (28, 005, TO_DATE('2024-09-15', 'YYYY-MM-DD'), 120.30, 'completed', 
'pending');
INSERT INTO orders (order_id, customer_id, orderDate, totalAmount, paymentStatus, 
orderStatus)
VALUES (29, 008, TO_DATE('2024-09-20', 'YYYY-MM-DD'), 45.20, 'failed', 
'canceled');
INSERT INTO orders (order_id, customer_id, orderDate, totalAmount, paymentStatus, 
orderStatus)
VALUES (30, 001, TO_DATE('2024-09-22', 'YYYY-MM-DD'), 88.70, 'completed', 
'pending');
INSERT INTO orders (order_id, customer_id, orderDate, totalAmount, paymentStatus, 
orderStatus)
VALUES (31, 007, TO_DATE('2024-09-25', 'YYYY-MM-DD'), 63.45, 'completed', 
'completed');
INSERT INTO orders (order_id, customer_id, orderDate, totalAmount, paymentStatus, 
orderStatus)
VALUES (32, 002, TO_DATE('2024-09-28', 'YYYY-MM-DD'), 54.00, 'failed', 
'canceled');
INSERT INTO orders (order_id, customer_id, orderDate, totalAmount, paymentStatus, 
orderStatus)
VALUES (33, 010, TO_DATE('2024-10-01', 'YYYY-MM-DD'), 99.90, 'completed', 
'pending');
INSERT INTO orders (order_id, customer_id, orderDate, totalAmount, paymentStatus, 
orderStatus)
VALUES (34, 006, TO_DATE('2024-10-05', 'YYYY-MM-DD'), 30.00, 'pending', 
'pending');
INSERT INTO orders (order_id, customer_id, orderDate, totalAmount, paymentStatus, 
orderStatus)
VALUES (35, 004, TO_DATE('2024-10-07', 'YYYY-MM-DD'), 65.25, 'completed', 
'completed');

-- Products table
INSERT INTO products (product_id, productName, productCategory, price, 
stockQuantity, supplier_id, expiryDate)
VALUES (001, 'lamb', 'meatNseafood', 50.00, 45, 001, TO_DATE('2024-12-20', 
'YYYY-MM-DD'));
INSERT INTO products (product_id, productName, productCategory, price, 
stockQuantity, supplier_id, expiryDate)
VALUES (002, 'prawn', 'meatNseafood', 20.00, 60, 001, TO_DATE('2025-11-02', 
'YYYY-MM-DD'));
INSERT INTO products (product_id, productName, productCategory, price, 
stockQuantity, supplier_id, expiryDate)
VALUES (003, 'bread', 'bakery', 2.50, 30, 002, TO_DATE('2024-11-20', 'YYYY-MMDD'));
INSERT INTO products (product_id, productName, productCategory, price, 
stockQuantity, supplier_id, expiryDate)
VALUES (004, 'cookies', 'bakery', 4.00, 15, 002, TO_DATE('2025-01-14', 'YYYYMM-DD'));
INSERT INTO products (product_id, productName, productCategory, price, 
stockQuantity, supplier_id, expiryDate)
VALUES (005, 'milk', 'dairy', 5.50, 100, 010, TO_DATE('2025-03-24', 'YYYY-MMDD'));
INSERT INTO products (product_id, productName, productCategory, price, 
stockQuantity, supplier_id, expiryDate)
VALUES (006, 'chips', 'snacks', 3.00, 50, 009, TO_DATE('2024-12-10', 'YYYY-MMDD'));
INSERT INTO products (product_id, productName, productCategory, price, 
stockQuantity, supplier_id, expiryDate)
VALUES (007, 'chocolate bar', 'snacks', 2.20, 75, 009, TO_DATE('2025-01-05', 
'YYYY-MM-DD'));
INSERT INTO products (product_id, productName, productCategory, price, 
stockQuantity, supplier_id, expiryDate)
VALUES (008, 'shampoo', 'health and beauty', 15.00, 25, 006, TO_DATE('2025-08-30', 
'YYYY-MM-DD'));
INSERT INTO products (product_id, productName, productCategory, price, 
stockQuantity, supplier_id, expiryDate)
VALUES (009, 'green tea', 'beverages', 8.50, 60, 005, TO_DATE('2025-02-20', 'YYYYMM-DD'));
INSERT INTO products (product_id, productName, productCategory, price, 
stockQuantity, supplier_id, expiryDate)
VALUES (010, 'orange juice', 'beverages', 6.00, 40, 005, TO_DATE('2025-04-15', 
'YYYY-MM-DD'));
