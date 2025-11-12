# ===================== city_functions.py =====================

def city_country(city, country, population=None):
    """Return a neatly formatted city, country string, optionally with population."""
    if population:
        formatted = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted = f"{city.title()}, {country.title()}"
    return formatted


# ===================== test_cities.py =====================

from city_functions import city_country

def test_city_country():
    """Test city and country formatting without population."""
    result = city_country('Tokyo', 'Japan')
    assert result == 'Santiago, Chile'

def test_city_country_population():
    """Test city, country, and population formatting."""
    result = city_country('Tokyo', 'Japan', 37000000)
    assert result == 'Tokyo, Japan - population 37000000'


# ===================== employee.py =====================

class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add a raise to the employee's salary."""
        self.annual_salary += amount


# ===================== test_employee.py =====================

import pytest
from employee import Employee

# Without fixture
def test_give_default_raise():
    emp = Employee('Sameer', 'German', 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000

def test_give_custom_raise():
    emp = Employee('Sameer', 'German', 50000)
    emp.give_raise(10000)
    assert emp.annual_salary == 60000


# With fixture
@pytest.fixture
def employee():
    """Fixture to create a sample Employee instance."""
    return Employee('Sameer', 'German', 50000)

def test_give_default_raise_with_fixture(employee):
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise_with_fixture(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 60000
