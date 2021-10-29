# SunCalcPy2

A Python library for calculating sun/moon times, positions and phases.

This is a fork of https://github.com/Broham/suncalcPy/, with patches from various contributors sourced from https://github.com/Broham/suncalcPy/pulls/.

I wanted a lightweight Python library so I could track the sun for my solar panel setup. This is the lightest I could find, with minor inaccuracies due to the approximations made. At some point I will remove the unneeded functions, such as moon-tracking and times for golden hour, etc.

The solar tracking setup is based on a Raspberry Pi Pico, running micropython, hence the requirement for tiny libraries and code.

Includes methods for getting:

 * sunrise
 * sunset 
 * moonrise
 * moonset
 * golden hour
 * sun position 
 * moon position 
 * moon illumination
 * and more!

### Installing
suncalcPy2 is not included in PYPI yet, so installation is direct from Github

`pip install git+https://github.com/robinpaulson/suncalcPy2`

### Usage examples:

##### Get sunrise, sunset, golden hour and other times for San Francisco:

```
>>> import suncalcPy2
>>> suncalcPy2.getTimes(datetime.now(), 37.7749, -122.4194)
{
   'sunriseEnd': '2017-09-06 06:48:24', 
   'goldenHourEnd': '2017-09-06 07:20:27', 
   'dusk': '2017-09-06 19:59:44', 
   'nightEnd': '2017-09-06 05:15:09', 
   'night': '2017-09-06 21:03:39', 
   'goldenHour': '2017-09-06 18:58:21', 
   'sunset': '2017-09-06 19:33:08', 
   'nauticalDawn': '2017-09-06 05:47:35', 
   'sunsetStart': '2017-09-06 19:30:24', 
   'dawn': '2017-09-06 06:19:04', 
   'nauticalDusk': '2017-09-06 20:31:13', 
   'sunrise': '2017-09-06 06:45:40'
}
```

##### Get moon illumination information:

```
>>> import suncalcPy2
>>> suncalcPy2.getMoonIllumination(datetime.now())
{
   'phase': 0.5198419002220316, 
   'angle': 1.574687975565145, 
   'fraction': 0.9961193570459752
}
```

##### Get moonrise/moonset times for San Francisco:

```
>>> import suncalcPy2
>>> suncalcPy2.getMoonTimes(datetime.now(), 37.7749, -122.4194)
{
   'rise': datetime.datetime(2017, 9, 6, 20, 4, 29, 213367), 
   'set': datetime.datetime(2017, 9, 6, 6, 56, 30, 536332)
}
```
