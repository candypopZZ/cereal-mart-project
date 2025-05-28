PROCEDURE 1: Add new products and suppliers 
CREATE OR REPLACE PROCEDURE add_product_and_supplier ( 
p_product_id IN NUMBER, 
p_productName IN VARCHAR2, 
p_productCategory IN VARCHAR2, 
p_price IN NUMBER, 
p_supplier_id IN NUMBER, 
s_supplierName IN VARCHAR2, 
s_contactNumber IN VARCHAR2 
) 
IS 
BEGIN 
-- Add a new product to the products table 
INSERT INTO products (product_id, productName, productCategory, price, supplier_id) 
VALUES (011, 'Green tea', 'Beverages', 4.50, 5); 
-- Insert into Suppliers Table 
INSERT INTO Suppliers (Supplier_Id, SupplierName, ContactNumber) 
VALUES (5, 'Beverage Hub', '0126789012'); 
DBMS_OUTPUT.PUT_LINE('New product and supplier successfully added.'); 
EXCEPTION 
WHEN DUP_VAL_ON_INDEX THEN 
DBMS_OUTPUT.PUT_LINE('Error: Duplicate product ID or customer ID.'); 
WHEN OTHERS THEN 
DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM); 
END; 
/

--PROCEDURE 2: Retrieve product details based on product ID using a cursor 
CREATE OR REPLACE PROCEDURE get_product_details (
 p_product_id IN NUMBER
)
IS
 CURSOR product_cursor IS
 SELECT product_id, productName, productCategory, price, supplier_id
 FROM products
 WHERE product_id = p_product_id;
 v_product_id products.product_id%TYPE;
 v_productName products.productName%TYPE;
 v_productCategory products.productCategory%TYPE;
 v_price products.price%TYPE;
 v_supplier_id products.supplier_id%TYPE;
BEGIN
 -- Open the cursor and fetch the data
 OPEN product_cursor;
 FETCH product_cursor INTO v_product_id, v_productName, v_productCategory, 
v_price, v_supplier_id;
 -- Check if the product exists
 IF product_cursor%FOUND THEN
 DBMS_OUTPUT.PUT_LINE('Product ID: ' v_product_id);
 DBMS_OUTPUT.PUT_LINE('Product Name: ' v_productName);
 DBMS_OUTPUT.PUT_LINE('Product Category: ' v_productCategory);
 DBMS_OUTPUT.PUT_LINE('Price: ' v_price);
 DBMS_OUTPUT.PUT_LINE('Supplier ID: ' v_supplier_id);
 ELSE
 DBMS_OUTPUT.PUT_LINE('Product with ID ' p_product_id ' not found.');
 END IF;
 -- Close the cursor
 CLOSE product_cursor;
EXCEPTION
 WHEN OTHERS THEN
 DBMS_OUTPUT.PUT_LINE('Error: ' SQLERRM);
END;
/

8.FUNCTION
--Function 1: Calculate the discount for loyal customers based on their total spending. 
Loyal customers get a 5% discount if their total spending exceeds 500. Otherwise, no 
discount is applied. 
CREATE OR REPLACE FUNCTION calculate_discount ( 
p_customer_id IN NUMBER 
) RETURN NUMBER 
IS 
v_total_spending NUMBER := 0; 
v_discount NUMBER := 0; 
BEGIN 
SELECT SUM(totalAmount) 
INTO v_total_spending 
FROM Orders 
WHERE customer_id = p_customer_id; 
IF v_total_spending > 500 THEN 
v_discount := v_total_spending * 0.05; -- 5% discount 
END IF; 
RETURN v_discount; 
EXCEPTION 
WHEN NO_DATA_FOUND THEN 
RETURN 0; 
END;\

--Function 2: Calculate the total quantity of products purchased by a customer based 
on their order. 
CREATE OR REPLACE FUNCTION total_quantity_purchased ( 
p_customer_id IN NUMBER 
) RETURN NUMBER 
IS 
v_total_quantity NUMBER := 0; 
BEGIN 
SELECT SUM(totalAmount) 
INTO v_total_quantity 
FROM Orders 
WHERE customer_id = p_customer_id; 
RETURN v_total_quantity; 
EXCEPTION 
WHEN NO_DATA_FOUND THEN 
RETURN 0; 
END; 

-- Anonymous block: 

DECLARE 
v_customer_id NUMBER := 1; -- Example customer ID 
v_discount NUMBER; 
v_total_quantity NUMBER; 
BEGIN 
-- Call the calculate_discount function 
v_discount := calculate_discount(v_customer_id); 
-- Call the total_quantity_purchased function 
v_total_quantity := total_quantity_purchased(v_customer_id); 
DBMS_OUTPUT.PUT_LINE('Customer ID: ' || v_customer_id); 
DBMS_OUTPUT.PUT_LINE('Discount Amount: $' || TO_CHAR(v_discount, 
'999,999.99')); 
DBMS_OUTPUT.PUT_LINE('Total Quantity Purchased: ' || v_total_quantity); 
EXCEPTION 
WHEN OTHERS THEN 
DBMS_OUTPUT.PUT_LINE('Error occurred: ' || SQLERRM); 
END; 
/
