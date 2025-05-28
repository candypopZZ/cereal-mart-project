import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import cx_Oracle
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'cerealmart123'  # Simple secret key for development

# Oracle database connection
try:
    conn = cx_Oracle.connect('system', '1234567', 'XE')
    print("Connected to Oracle database!")
except cx_Oracle.Error as error:
    print(f"Error connecting to Oracle database: {error}")

# Create cursor
cursor = conn.cursor()

def format_date_for_db(date_str):
    """Convert HTML date format to Oracle format"""
    try:
        if not date_str:
            return None
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d-%b-%Y').upper()
    except ValueError as e:
        flash(f"Date format error: {str(e)}", "error")
        return None

@app.route('/')
def home():
    return render_template('index.html')

# Suppliers routes
@app.route('/suppliers')
def suppliers():
    try:
        cursor.execute("SELECT * FROM Suppliers ORDER BY supplier_id")
        rows = cursor.fetchall()
        return render_template('suppliers.html', data=rows)
    except cx_Oracle.Error as e:
        flash(f"Error fetching suppliers: {str(e)}", "error")
        return redirect(url_for('home'))

@app.route('/add_supplier', methods=['POST'])
def add_supplier():
    try:
        cursor.execute("""
            INSERT INTO Suppliers (supplierName, productCategory, contactNumber, address)
            VALUES (:1, :2, :3, :4)
        """, (
            request.form['supplierName'],
            request.form['productCategory'],
            request.form['contactNumber'],
            request.form['address']
        ))
        conn.commit()
        flash("Supplier added successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error adding supplier: {str(e)}", "error")
    return redirect(url_for('suppliers'))

@app.route('/delete_supplier/<int:supplier_id>')
def delete_supplier(supplier_id):
    try:
        cursor.execute("DELETE FROM Suppliers WHERE supplier_id = :1", (supplier_id,))
        conn.commit()
        flash("Supplier deleted successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error deleting supplier: {str(e)}", "error")
    return redirect(url_for('suppliers'))

# Add these routes to your existing app.py file

@app.route('/update_supplier', methods=['POST'])
def update_supplier():
    try:
        supplier_id = request.form['supplierId']
        supplier_name = request.form['supplierName']
        contact_number = request.form['contactNumber']
        address = request.form['address']
        product_category = request.form['productCategory']

        cursor.execute("""
            UPDATE Suppliers 
            SET supplierName = :1,
                contactNumber = :2,
                address = :3,
                productCategory = :4
            WHERE supplier_id = :5
        """, (supplier_name, contact_number, address, product_category, supplier_id))
        
        conn.commit()
        flash("Supplier updated successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error updating supplier: {str(e)}", "error")
    
    return redirect(url_for('suppliers'))

@app.route('/edit_supplier/<int:supplier_id>')
def edit_supplier(supplier_id):
    try:
        cursor.execute("SELECT * FROM Suppliers WHERE supplier_id = :1", (supplier_id,))
        supplier = cursor.fetchone()
        
        if supplier:
            return render_template('edit_supplier.html', supplier=supplier)
        else:
            flash("Supplier not found", "error")
            return redirect(url_for('suppliers'))
            
    except cx_Oracle.Error as e:
        flash(f"Error fetching supplier details: {str(e)}", "error")
        return redirect(url_for('suppliers'))

# Products routes
@app.route('/products')
def products():
    try:
        cursor.execute("SELECT p.*, s.supplierName FROM Products p LEFT JOIN Suppliers s ON p.supplier_id = s.supplier_id ORDER BY p.product_id")
        rows = cursor.fetchall()
        
        # Fetch suppliers for the add product form
        cursor.execute("SELECT supplier_id, supplierName FROM Suppliers")
        suppliers = cursor.fetchall()
        
        return render_template('products.html', data=rows, suppliers=suppliers)
    except cx_Oracle.Error as e:
        flash(f"Error fetching products: {str(e)}", "error")
        return redirect(url_for('home'))

@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        cursor.execute("""
            INSERT INTO Products (productName, productCategory, price,
                                stockQuantity, supplier_id, expiryDate)
            VALUES (:1, :2, :3, :4, :5, TO_DATE(:6, 'YYYY-MM-DD'))
        """, (
            request.form['productName'],
            request.form['productCategory'],       # matches the form field name
            request.form['price'],
            request.form['stock'],          # matches the form field name
            request.form['supplierId'],     # matches the form field name
            request.form['expiryDate']
        ))
        conn.commit()
        flash("Product added successfully!", "success")
    except cx_Oracle.Error as e:
        print(f"Oracle Error: {str(e)}")  # Debug print
        flash(f"Error adding product: {str(e)}", "error")
    return redirect(url_for('products'))

@app.route('/delete_product/<int:product_id>')
def delete_product(product_id):
    try:
        cursor.execute("DELETE FROM Products WHERE product_id = :1", (product_id,))
        conn.commit()
        flash("Product deleted successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error deleting product: {str(e)}", "error")
    return redirect(url_for('products'))

@app.route('/update_product', methods=['POST'])
def update_product():
    try:
        product_id = request.form['product_id']
        product_name = request.form['productName']
        category = request.form['productCategory']
        price = request.form['price']
        stock = request.form['stockQuantity']
        supplier_id = request.form['supplier_id']
        expiryDate = request.form['expiryDate']
        
        cursor.execute("""
            UPDATE Products 
            SET productName = :1,
                productCategory = :2,
                price = :3,
                stockQuantity = :4,
                supplier_id = :5,
                expiryDate = TO_DATE(:6, 'YYYY-MM-DD')
            WHERE product_id = :7
        """, (product_name, category, price, stock, supplier_id, expiryDate, product_id))
        
        conn.commit()
        flash("Product updated successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error updating product: {str(e)}", "error")
    
    return redirect(url_for('products'))

@app.route('/edit_product/<int:product_id>')
def edit_product(product_id):
    try:
        # Get product information
        cursor.execute("""
            SELECT product_id, productName, productCategory, price, stockQuantity, expiryDate, supplier_id 
            FROM Products 
            WHERE product_id = :1
        """, (product_id,))
        product = cursor.fetchone()
        
        if product:
            return render_template('edit_product.html', product=product)
        else:
            flash("Product not found", "error")
            return redirect(url_for('products'))
            
    except cx_Oracle.Error as e:
        flash(f"Error fetching product details: {str(e)}", "error")
        return redirect(url_for('products'))

# Customers routes
@app.route('/customers')
def customers():
    try:
        cursor.execute("SELECT * FROM Customers ORDER BY customer_id")
        rows = cursor.fetchall()
        return render_template('customers.html', data=rows)
    except cx_Oracle.Error as e:
        flash(f"Error fetching customers: {str(e)}", "error")
        return redirect(url_for('home'))

@app.route('/add_customer', methods=['POST'])
def add_customer():
    try:
        cursor.execute("""
            INSERT INTO Customers (firstName, lastName, contactNumber, address)
            VALUES (:1, :2, :3, :4)
        """, (
            request.form['firstName'],
            request.form['lastName'],
            request.form['contactNumber'],
            request.form['address']
        ))
        conn.commit()
        flash("Customer added successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error adding customer: {str(e)}", "error")
    return redirect(url_for('customers'))

@app.route('/delete_customer/<int:customer_id>')
def delete_customer(customer_id):
    try:
        cursor.execute("DELETE FROM Customers WHERE customer_id = :1", (customer_id,))
        conn.commit()
        flash("Customer deleted successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error deleting customer: {str(e)}", "error")
    return redirect(url_for('customers'))

@app.route('/edit_customer/<int:customer_id>')
def edit_customer(customer_id):
    try:
        cursor.execute("SELECT * FROM Customers WHERE customer_id = :1", (customer_id,))
        customer = cursor.fetchone()

        if customer:
            return render_template('edit_customer.html', customer=customer)
        else:
            flash("Customer not found", "error")
            return redirect(url_for('customers'))
    except cx_Oracle.Error as e:
        flash(f"Error fetching customer details: {str(e)}", "error")
        return redirect(url_for('customers'))

@app.route('/update_customer', methods=['POST'])
def update_customer():
    try:
        customer_id = request.form['customerId']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        contact_number = request.form['contactNumber']
        address = request.form['address']

        cursor.execute("""
            UPDATE Customers
            SET firstName = :1,
                lastName = :2,
                contactNumber = :3,
                address = :4
            WHERE customer_id = :5
        """, (first_name, last_name, contact_number, address, customer_id))

        conn.commit()
        flash("Customer updated successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error updating customer: {str(e)}", "error")

    return redirect(url_for('customers'))

# Orders routes
@app.route('/orders')
def orders():
    try:
        cursor.execute("SELECT * FROM Orders ORDER BY order_id")
        rows = cursor.fetchall()
        return render_template('orders.html', data=rows)
    except cx_Oracle.Error as e:
        flash(f"Error fetching orders: {str(e)}", "error")
        return redirect(url_for('home'))

@app.route('/add_order', methods=['POST'])
def add_order():
    try:
        cursor.execute("""
            INSERT INTO Orders (customer_id, orderDate, totalAmount,
                              paymentStatus, orderStatus)
            VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4, :5)
        """, (
            request.form['customer_id'],
            request.form['orderDate'],
            request.form['totalAmount'],
            request.form['paymentStatus'],
            request.form['orderStatus']
        ))
        conn.commit()
        flash("Order added successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error adding order: {str(e)}", "error")
    return redirect(url_for('orders'))

@app.route('/delete_orders/<int:order_id>')
def delete_order(order_id):
    try:
        cursor.execute("DELETE FROM Orders WHERE order_id = :1", (order_id,))
        conn.commit()
        flash("Order deleted successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error deleting order: {str(e)}", "error")
    return redirect(url_for('orders'))

# Add these routes to your existing app.py file

@app.route('/edit_order/<int:order_id>')
def edit_order(order_id):
    try:
        cursor.execute("SELECT * FROM Orders WHERE order_id = :1", (order_id,))
        order = cursor.fetchone()
        
        if order:
            return render_template('edit_order.html', order=order)
        else:
            flash("Order not found", "error")
            return redirect(url_for('orders'))
            
    except cx_Oracle.Error as e:
        flash(f"Error fetching order details: {str(e)}", "error")
        return redirect(url_for('orders'))

@app.route('/update_order', methods=['POST'])
def update_order():
    try:
        order_id = request.form['orderId']
        customer_id = request.form['customer_id']
        order_date = request.form['orderDate']
        total_amount = request.form['totalAmount']
        payment_status = request.form['paymentStatus']
        order_status = request.form['orderStatus']

        cursor.execute("""
            UPDATE Orders 
            SET customer_id = :1,
                orderDate = TO_DATE(:2, 'DD - MON - YYYY'),
                totalAmount = :3,
                paymentStatus = :4,
                orderStatus = :5
            WHERE order_id = :6
        """, (customer_id, order_date, total_amount, payment_status, order_status, order_id))
        
        conn.commit()
        flash("Order updated successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error updating order: {str(e)}", "error")
    
    return redirect(url_for('orders'))

# Employees routes
@app.route('/employees')
def employees():
    try:
        cursor.execute("SELECT * FROM Employees ORDER BY employee_id")
        rows = cursor.fetchall()
        return render_template('employees.html', data=rows)
    except cx_Oracle.Error as e:
        flash(f"Error fetching employees: {str(e)}", "error")
        return redirect(url_for('home'))

@app.route('/add_employee', methods=['POST'])
def add_employee():
    try:
        hire_date = format_date_for_db(request.form['hireDate'])
        cursor.execute("""
            INSERT INTO Employees (firstName, lastName, jobPosition, salary, contactNumber, email, hireDate)
            VALUES (:1, :2, :3, :4, :5, :6, TO_DATE(:7, 'DD-MON-YYYY'))
        """, (
            request.form['firstName'],
            request.form['lastName'],
            request.form['jobPosition'],
            float(request.form['salary']),
            request.form['contactNumber'],
            request.form['email'],
            hire_date
        ))
        conn.commit()
        flash("Employee added successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error adding employee: {str(e)}", "error")
    return redirect(url_for('employees'))

@app.route('/delete_employee/<int:employee_id>')
def delete_employee(employee_id):
    try:
        cursor.execute("DELETE FROM Employees WHERE employee_id = :1", (employee_id,))
        conn.commit()
        flash("Employee deleted successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error deleting employee: {str(e)}", "error")
    return redirect(url_for('employees'))

@app.route('/edit_employee/<int:employee_id>')
def edit_employee(employee_id):
    try:
        cursor.execute("SELECT * FROM Employees WHERE employee_id = :1", (employee_id,))
        employee = cursor.fetchone()

        if employee:
            # Format the hire date in YYYY-MM-DD for the date input field
            formatted_employee = list(employee)
            if employee[7]:  # Assuming index 7 is the hireDate
                formatted_employee[7] = employee[7].strftime('%Y-%m-%d')
            return render_template('edit_employee.html', employee=formatted_employee)
        else:
            flash("Employee not found", "error")
            return redirect(url_for('employees'))
    except cx_Oracle.Error as e:
        flash(f"Error fetching employee details: {str(e)}", "error")
        return redirect(url_for('employees'))


@app.route('/update_employee', methods=['POST'])
def update_employee():
    try:
        employee_id = request.form['employeeId']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        job_position = request.form['jobPosition']
        salary = float(request.form['salary'])
        contact_number = request.form['contactNumber']
        email = request.form['email']
        hire_date = format_date_for_db(request.form['hireDate'])

        cursor.execute("""
            UPDATE Employees
            SET firstName = :1,
                lastName = :2,
                jobPosition = :3,
                salary = :4,
                contactNumber = :5,
                email = :6,
                hireDate = TO_DATE(:7, 'DD-MON-YYYY')
            WHERE employee_id = :8
        """, (first_name, last_name, job_position, salary, contact_number, email, hire_date, employee_id))

        conn.commit()
        flash("Employee updated successfully!", "success")
    except cx_Oracle.Error as e:
        flash(f"Error updating employee: {str(e)}", "error")

    return redirect(url_for('employees'))

# Procedure
@app.route('/get_product_details/<int:product_id>')
def get_product_details(product_id):
    try:
        # Call the procedure
        cursor.callproc('get_product_details', [product_id])

        # Fetch the results
        cursor.execute("SELECT product_id, productName, productCategory, price, supplier_id FROM products WHERE product_id = :product_id", [product_id])
        details = cursor.fetchone()

        if details:
            output = [
                f"Product ID: {details[0]}",
                f"Product Name: {details[1]}",
                f"Product Category: {details[2]}",
                f"Price: {details[3]}",
                f"Supplier ID: {details[4]}"
            ]
        else:
            output = [f"Product with ID {product_id} not found."]

        return render_template('product_details.html', details=output)
    except cx_Oracle.Error as e:
        flash(f"Error executing procedure: {str(e)}", "error")
        return redirect(url_for('products'))

# Function to calculate to discount
@app.route('/calculate_discount/<int:customer_id>')
def calculate_discount(customer_id):
    try:
        # Execute function
        result = cursor.callfunc('calculate_discount', cx_Oracle.NUMBER, [customer_id])
        return jsonify({"discount": float(result)})
    except cx_Oracle.Error as e:
        return jsonify({"error": str(e)}), 500

# Function to calculate total quantity purchased
@app.route('/total_quantity_purchased_ajax/<int:customer_id>')
def total_quantity_purchased_ajax(customer_id):
    try:
        # Functionality remains the same
        result = cursor.callfunc('total_quantity_purchased', cx_Oracle.NUMBER, [customer_id])
        return jsonify(success=True, result=result)
    except cx_Oracle.Error as e:
        return jsonify(success=False, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
