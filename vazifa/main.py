from autosalon import DataBase

def main():
    db = DataBase()
    print("Autosalon dasturi ishga tushdi.")
    while True:
        print("\nBuyruqlar ro'yxati:")
        print("1. modellarni chiroyli ko'rinishda chiqarish")
        print("2. xodimlar va buyurtmachilarning emayilni birlashtirish")
        print("3. har bir davlatda buyurtmachilar sonini hisoblash")
        print("4. har bir davlatda xodimlar sonini hisoblash")
        print("5. har bir brandda modellarning sonini chiqarish")
        print("6. modellar soni 5 tadan ko'p bo'lgan brandlarni chiqarish")
        print("7. orders jadvalini boshqa jadvallar bilan birlashtirish")
        print("8. modellar umumiy narxini hisoblash")
        print("9. brandlar sonini chiqarish")
        print("10. yangi ma'lumot qo'shish")
        print("11. dasturni to'xtatish")

        buyruq_tanlash = input("\nBuyruq raqamini tanlang: ")

        if buyruq_tanlash == '1':
            sql = """select models.model_name, brands.brand_name, colors.color_name 
                     from models 
                     join brands on models.brand_id = brands.brand_id
                     join colors on models.color_id = colors.color_id"""
            results = db.manager(sql=sql, fetchall=True)
            for row in results:
                print(f"Model: {row[0]}, Brand: {row[1]}, Rang: {row[2]}")

        elif buyruq_tanlash == '2':
            sql = """select email from employees UNION select email from customers"""
            results = db.manager(sql=sql, fetchall=True)
            print("Barcha email adreslar:")
            for email in results:
                print(email[0])
                
        
        elif buyruq_tanlash == '3':
            sql = """select country, COUNT(*) from customers GROUP BY country ORDER BY COUNT(*) DESC"""
            results = db.manager(sql=sql, fetchall=True)
            for row in results:
                print(f"Country: {row[0]}, Customers: {row[1]}")
        
        elif buyruq_tanlash == '4':
            sql = """select country, COUNT(*) from employees GROUP BY country ORDER BY COUNT(*) DESC"""
            results = db.manager(sql=sql, fetchall=True)
            for row in results:
                print(f"Country: {row[0]}, Employees: {row[1]}")

        elif buyruq_tanlash == '5':
            sql = """select brands.brand_name, COUNT(models.model_id) from brands 
                     join models on brands.brand_id = models.brand_id 
                     GROUP BY brands.brand_name"""
            results = db.manager(sql=sql, fetchall=True)
            for row in results:
                print(f"Brand: {row[0]}, Models: {row[1]}")

        elif buyruq_tanlash == '6':
            sql = """select brands.brand_name, COUNT(models.model_id) from brands 
                     join models on brands.brand_id = models.brand_id 
                     GROUP BY brands.brand_name HAVING COUNT(models.model_id) > 5"""
            results = db.manager(sql=sql, fetchall=True)
            for row in results:
                print(f"Brand: {row[0]}, Models: {row[1]}")

        elif buyruq_tanlash == '7':
            sql = """select orders.order_id, customers.first_name || ' ' || customers.last_name AS customer, 
                            employees.first_name || ' ' || employees.last_name AS employee, 
                            models.model_name 
                     from orders
                     join customers on orders.customer_id = customers.customer_id
                     join employees on orders.employee_id = employees.employee_id
                     join models on orders.model_id = models.model_id"""
            results = db.manager(sql=sql, fetchall=True)
            for row in results:
                print(f"Order ID: {row[0]}, Customer: {row[1]}, Employee: {row[2]}, Model: {row[3]}")

        elif buyruq_tanlash == '8':
            sql = """select SUM(model_price) from models"""
            result = db.manager(sql=sql, fetchone=True)
            print(f"Barcha modellar umumiy narxi: {result[0]}")

        elif buyruq_tanlash == '9':
            sql = """select COUNT(*) from brands"""
            result = db.manager(sql=sql, fetchone=True)
            print(f"Jami brandlar soni: {result[0]}")

        elif buyruq_tanlash == '10':
            table = input("Qaysi jadvalga ma'lumot qo'shmoqchisiz? (customers, employees, models): ").strip()
            if table == 'customers':
                first_name = input("Ismi: ")
                last_name = input("Familiyasi: ")
                email = input("Email: ")
                country = input("Davlat: ")
                city = input("Shahar: ")
                phone_number = input("Telefon raqami: ")
                sql = """insert into customers (first_name, last_name, email, country, city, phone_number) 
                         values (%s, %s, %s, %s, %s, %s)"""
                db.manager(sql=sql, args=(first_name, last_name, email, country, city, phone_number), commit=True)
                print("Ma'lumot qo'shildi.")
            elif table == 'employees':
                first_name = input("Ismi: ")
                last_name = input("Familiyasi: ")
                email = input("Email: ")
                country = input("Davlat: ")
                city = input("Shahar: ")
                phone_number = input("Telefon raqami: ")
                sql = """insert into employees (first_name, last_name, email, country, city, phone_number) 
                         values (%s, %s, %s, %s, %s, %s)"""
                db.manager(sql=sql, args=(first_name, last_name, email, country, city, phone_number), commit=True)
                print("Ma'lumot qo'shildi.")
            elif table == 'models':
                model_name = input("Model nomi: ")
                model_price = float(input("Narxi: "))
                color_id = int(input("Color ID: "))
                brand_id = int(input("Brand ID: "))
                sql = """insert into models (model_name, model_price, color_id, brand_id) 
                         values (%s, %s, %s, %s)"""
                db.manager(sql=sql, args=(model_name, model_price, color_id, brand_id), commit=True)
                print("Ma'lumot qo'shildi.")


        elif buyruq_tanlash == '11':
            print("Dastur to'xtatildi.")
            break

        else:
            print("Noto'g'ri buyruq.")

if __name__ == "__main__":
    main()
