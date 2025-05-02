
import click
from prettytable import PrettyTable
from database import connect

@click.group()
def cli():
    pass

@cli.command()
@click.option('--limit', default=10, help='Number of employees to display')
def show_employees(limit):
    """Display employees in a table"""
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM employees LIMIT {limit}")
    rows = cur.fetchall()
    
    table = PrettyTable()
    table.field_names = ["ID", "First Name", "Last Name", "Position", "Hire Date", "Salary", "Manager ID"]
    
    for row in rows:
        table.add_row(row)
    
    print(table)
    cur.close()
    conn.close()

if __name__ == '__main__':
    cli()