from my_project.weather import *

'''def test_check_weather1():
    assert check_weather(21.00) == "hot", 'le temperature devono essere considerate calde'

def test_check_weather2():
    assert check_weather(5.00) == "average", 'le temerature sono ok'

def test_check_weather3():
    assert check_weather(5.00) == "cold", 'le temerature sono fredde'

def test_check_weather4():
    assert check_weather(13.00) == "average", 'le temerature sono yeah'

def test_check_weather5():
    assert check_weather(30.00) == "hot", 'le temerature sono calde'
    assert check_weather(11.00) == "cold",'temerature calde'
'''
from my_project.weather import check_weather
import pytest

@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])
def test_check_weather(temperature, expected):
    ae: str = ''
    if temperature > 20:
        ae = ' temperatura sono 20 è hot'
    elif 10 < temperature <= 20:
        ae = 'temeprature è alta'
    else:
        ae = 'temperatura sotto i 10 freddo'
    assert check_weather(temperature) == expected,ae