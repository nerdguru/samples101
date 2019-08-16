# Samples 101
Provides a function with no dependencies (reverse), one with a public package dependency (starwars), and one with a public package dependency as well as a REST API call (weather).

## Usage
Using the sample is simple and demonstrated in `usage.py`:
```
import samples101
import sys

print(samples101.reverse('hello'))
print(samples101.starwars('hello'))
print(samples101.weather('New Orleans', sys.argv[1]))
```
And to execute:
```
python usage.py XXXXXXX
```
where `XXXXXXX` represents your [OpenWeather API key](https://openweathermap.org/api).  That execution should yield:
```
olleh
 __    __   _______  __       __        ______   
|  |  |  | |   ____||  |     |  |      /  __  \  
|  |__|  | |  |__   |  |     |  |     |  |  |  |
|   __   | |   __|  |  |     |  |     |  |  |  |
|  |  |  | |  |____ |  `----.|  `----.|  `--'  |
|__|  |__| |_______||_______||_______| \______/  


light intensity drizzle
```
