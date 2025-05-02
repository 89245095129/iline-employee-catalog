
from mimesis import Person, Business, Datetime
from mimesis.enums import Gender
import random
from database import connect

def generate_employees(num_employees=50000):
    person = Person('ru')
    business = Business()
    datetime = Datetime()
    
    positions = [
        "CEO", "CTO", "CFO", 
        "Manager", "Senior Manager", 
        "Team Lead", "Senior Team Lead",
        "Senior Developer", "Developer",
        "Junior Developer", "Intern"
    ]
    
    hierarchy = {
        "CEO": [],
        "CTO": ["CEO"],
        "CFO": ["CEO"],
        "Manager": ["CTO", "CFO"],
        "Senior Manager": ["Manager"],
        "Team Lead": ["Senior Manager"],
        "Senior Team Lead": ["Team Lead"],
        "Senior Developer": ["Senior Team Lead"],
        "Developer": ["Senior Developer"],
        "Junior Developer": ["Developer"],
        "Intern": ["Junior Developer"]
    }
    
    conn = connect()
    cur = conn.cursor()
    
    # Сначала создаем верхний уровень иерархии
    ceo = (
        person.first_name(),
        person.last_name(),
        "CEO",
        datetime.date(start=2010, end=2015),
        round(random.uniform(300000, 500000), 2),
        None
    )
    cur.execute("""
        INSERT INTO employees 
        (first_name, last_name, position, hire_date, salary, manager_id) 
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
    """, ceo)
    ceo_id = cur.fetchone()[0]
    
    # Генерируем остальных сотрудников
    for i in range(1, num_employees):
        position = random.choice(positions)
        possible_managers = hierarchy[position]
        
        # Находим ID возможных менеджеров
        cur.execute("""
            SELECT id FROM employees 
            WHERE position IN %s 
            ORDER BY RANDOM() LIMIT 1
        """, (tuple(possible_managers),))
        manager = cur.fetchone()
        manager_id = manager[0] if manager else None
        
        employee = (
            person.first_name(),
            person.last_name(),
            position,
            datetime.date(start=2015, end=2023),
            round(random.uniform(30000, 200000), 2),
            manager_id
        )
        
        cur.execute("""
            INSERT INTO employees 
            (first_name, last_name, position, hire_date, salary, manager_id) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, employee)
        
        if i % 1000 == 0:
            print(f"Inserted {i} employees")
            conn.commit()
    
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    generate_employees()