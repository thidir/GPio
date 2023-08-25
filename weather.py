from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


# OWM = OWM('835dca77bed51255016c207ab11850cd')
# mgr = OWM.weather_manager()


# observation=mgr.weather_at_place('London,GB')
# w=observation.weather

# print(w.detailed_status)
# print(w.wind())
# print(w.humidity)
# print(w.temperature('celsius'))
# print(w.rain)
# print(w.heat_index)
# print(w.clouds)

def weather_condition(place):
    Owm = OWM('API key is here')
    mgr = Owm.weather_manager()
    observation=mgr.weather_at_place(place)
    w=observation.weather



    print(w.detailed_status)
    print(w.wind())
    print(w.humidity)
    print(w.temperature('celsius'))
    print(w.rain)
    print(w.heat_index)
    print(w.clouds)
    print(w.air_pressure)

print('Hong Kong, China')
weather_condition('Hong Kong, China')
print('Accra, Ghana')
weather_condition('Accra, Ghana')





