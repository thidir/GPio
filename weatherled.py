from gpiozero import LED
from time import sleep
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

def weather_condition(place):
    Owm = OWM('')
    mgr = Owm.weather_manager()
    observation=mgr.weather_at_place(place)
    w=observation.weather

    




