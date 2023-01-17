from persistence import *

def main():
    activities = repo.activities.find_all()
    print(repo.activities._table_name.capitalize())
    for a in sorted(activities, key=lambda x: x.date):
        print(a.__str__())

    branches = repo.branches.find_all()
    print(repo.branches._table_name.capitalize())
    for b in sorted(branches, key=lambda x: x.id):
        print(b.__str__())

    employees = repo.employees.find_all()
    print(repo.employees._table_name.capitalize())
    for e in sorted(employees, key=lambda x: x.id):
        print(e.__str__())

    products = repo.products.find_all()
    print(repo.products._table_name.capitalize())
    for p in sorted(products, key=lambda x: x.id):
        print(p.__str__())

    suppliers = repo.suppliers.find_all()
    print(repo.suppliers._table_name.capitalize())
    for s in sorted(suppliers, key=lambda x: x.id):
        print(s.__str__())

    employees_report = repo.execute_command("""
    WITH employees_location AS(
    SELECT e.id, e.name, e.salary, b.location
    FROM employees as e LEFT JOIN branches as b ON e.branche=b.id
    ), employees_activity AS(
    SELECT a.activator_id, SUM(p.price * -a.quantity) as profit
    FROM activities as a INNER JOIN products as p ON a.product_id=p.id
    GROUP BY a.activator_id 
    )
    
    SELECT name, salary, location, coalesce(profit, 0) as profit
    FROM employees_location as el LEFT JOIN employees_activity as ea ON ea.activator_id=el.id
    """)

    print("\nEmployees report")
    for t in sorted(employees_report, key=lambda x: x[0]):
        print(f"{t[0].decode()} {t[1]} {t[2].decode()} {t[3]}")

    activities_report = repo.execute_command("""
        WITH activities_desc AS(
        SELECT a.*, p.description
        FROM activities as a INNER JOIN products as p ON a.product_id=p.id
        )
        
        SELECT ad.date, ad.description, ad.quantity, e.name as employee_name, s.name as supplier_name
        FROM activities_desc as ad
        LEFT JOIN employees as e ON ad.activator_id=e.id LEFT JOIN suppliers as s ON ad.activator_id=s.id 
        """)
    print("\nActivities report")
    for t in sorted(activities_report, key=lambda x: x[0]):
        if t[3] is None:
            print(f"({str(t[0])[1:]}, {str(t[1])[1:]}, {t[2]}, {t[3]}, {str(t[4])[1:]})")
        else:
            print(f"({str(t[0])[1:]}, {str(t[1])[1:]}, {t[2]}, {str(t[3])[1:]}, {t[4]})")


if __name__ == '__main__':
    main()