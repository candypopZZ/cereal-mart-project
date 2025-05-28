CREATE TABLE suppliers (
 supplier_id INT PRIMARY KEY NOT NULL,
 supplierName VARCHAR2(30) NULL,
 contactNumber VARCHAR2(12) NULL,
 address VARCHAR2(40) NULL,
 productCategory VARCHAR2(40) NULL
);
CREATE TABLE employees (
 employee_id INT PRIMARY KEY NOT NULL,
 firstName VARCHAR2(15) NULL,
 lastName VARCHAR2(15) NULL,
 jobPosition VARCHAR2(35) NOT NULL,
 salary DECIMAL(10, 2) NULL,
 contactNumber VARCHAR2(12) NULL,
 email VARCHAR2(30) NULL,
 hireDate DATE NULL
);
CREATE TABLE customers (
 customer_id INT PRIMARY KEY NOT NULL,
 firstName VARCHAR2(15) NULL,
 lastName VARCHAR2(15) NULL,
 contactNumber VARCHAR2(12) NULL,
 address VARCHAR2(40) NULL
);
CREATE TABLE orders (
 order_id INT PRIMARY KEY NOT NULL,
 customer_id INT NOT NULL,
 orderDate DATE NULL,
 totalAmount DECIMAL(10, 2) NOT NULL,
 paymentStatus VARCHAR2(10) NOT NULL,
 orderStatus VARCHAR2(10) NOT NULL,
 CONSTRAINT CUSTOMERS_customer_id_FK FOREIGN KEY(customer_id) 
 REFERENCES customers(customer_id) 
 ON DELETE CASCADE
);
9
CREATE TABLE products (
 product_id INT PRIMARY KEY NOT NULL,
 productName VARCHAR2(20) NOT NULL,
 productCategory VARCHAR2(35) NULL,
 price DECIMAL(10, 2) NULL,
 stockQuantity NUMBER(10) NULL,
 supplier_id INT NOT NULL,
 expiryDate DATE NOT NULL,
 CONSTRAINT SUPPLIERS_supplier_id_FK FOREIGN KEY(supplier_id) 
 REFERENCES suppliers(supplier_id) 
 ON DELETE CASCADE
);
