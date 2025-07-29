
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

ZODIAC = {
    'ARIES': 'Beran',
    'TAURUS': 'Býk',
    'GEMINI': 'Blíženci',
    'CANCER': 'Rak',
    'LEO': 'Lev',
    'VIRGO': 'Panna',
    'LIBRA': 'Váhy',
    'SCORPIO': 'Štír',
    'SAGITTARIUS': 'Střelec',
    'CAPRICORN': 'Kozoroh',
    'AQUARIUS': 'Vodnář',
    'PISCES': 'Ryby'
}

def get_sign(obj):
    return ZODIAC.get(obj.sign, obj.sign)

def calculate_positions(date_str, time_str, place):
    pos = GeoPos('50.0755', '14.4378')  # Praha
    dt = Datetime(date_str, time_str, '+01:00')
    chart = Chart(dt, pos)
    sun = chart.get('SUN')
    moon = chart.get('MOON')
    asc = chart.get('ASC')
    return get_sign(sun), get_sign(moon), get_sign(asc)
