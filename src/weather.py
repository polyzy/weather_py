# -*- coding: utf-8 -*-
# import requests
import urllib
import json
import sys
from datetime import datetime, timedelta


base_url = "http://api.worldweatheronline.com/free/v2/weather.ashx"

codes = {'113': 'iconSunny',
         '116': 'iconPartlyCloudy',
         "119": 'iconCloudy',
         '122': 'iconVeryCloudy',
         '143': 'iconFog',
         '176': 'iconLightShowers',
         '179': 'iconLightSleetShowers',
         '182': 'iconLightSleet',
         '185': 'iconLightSleet',
         '200': 'iconThunderyShowers',
         '227': 'iconLightSnow',
         '230': 'iconHeavySnow',
         '248': 'iconFog',
         '260': 'iconFog',
         '263': 'iconLightShowers',
         '266': 'iconLightRain',
         '281': 'iconLightSleet',
         '284': 'iconLightSleet',
         '293': 'iconLightRain',
         '296': 'iconLightRain',
         '299': 'iconHeavyShowers',
         '302': 'iconHeavyRain',
         '305': 'iconHeavyShowers',
         '308': 'iconHeavyRain',
         '311': 'iconLightSleet',
         '314': 'iconLightSleet',
         '317': 'iconLightSleet',
         '320': 'iconLightSnow',
         '323': 'iconLightSnowShowers',
         '326': 'iconLightSnowShowers',
         '329': 'iconHeavySnow',
         '332': 'iconHeavySnow',
         '335': 'iconHeavySnowShowers',
         '338': 'iconHeavySnow',
         '350': 'iconLightSleet',
         '353': 'iconLightShowers',
         '356': 'iconHeavyShowers',
         '359': 'iconHeavyRain',
         '362': 'iconLightSleetShowers',
         '365': 'iconLightSleetShowers',
         '368': 'iconLightSnowShowers',
         '371': 'iconHeavySnowShowers',
         '374': 'iconLightSleetShowers',
         '377': 'iconLightSleet',
         '386': 'iconThunderyShowers',
         '389': 'iconThunderyHeavyRain',
         '392': 'iconThunderySnowShowers',
         '395': 'iconHeavySnowShowers'
         }

icons = {
    'iconSunny': [
        '\033[38;5;226m    \\   /    \033[0m',
        '\033[38;5;226m     .-.     \033[0m',
        '\033[38;5;226m  ― (   ) ―  \033[0m',
        '\033[38;5;226m     `-’     \033[0m',
        '\033[38;5;226m    /   \\    \033[0m'],
    'iconPartlyCloudy': [
        "\033[38;5;226m   \\  /\033[0m      ",
        "\033[38;5;226m _ /\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m   \\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "             "],
    'iconCloudy': [
        "             ",
        "\033[38;5;250m     .--.    \033[0m",
        "\033[38;5;250m  .-(    ).  \033[0m",
        "\033[38;5;250m (___.__)__) \033[0m",
        "             "],
    'iconVeryCloudy': [
        "             ",
        "\033[38;5;240;1m     .--.    \033[0m",
        "\033[38;5;240;1m  .-(    ).  \033[0m",
        "\033[38;5;240;1m (___.__)__) \033[0m",
        "             "],
    'iconLightShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;111m     ‘ ‘ ‘ ‘ \033[0m",
        "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m"],
    'iconHeavyShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;240;1m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;240;1m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;240;1m(___(__) \033[0m",
        "\033[38;5;21;1m   ‚‘‚‘‚‘‚‘  \033[0m",
        "\033[38;5;21;1m   ‚’‚’‚’‚’  \033[0m"],
    'iconLightSnowShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;255m     *  *  * \033[0m",
        "\033[38;5;255m    *  *  *  \033[0m"],
    'iconHeavySnowShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;240;1m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;240;1m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;240;1m(___(__) \033[0m",
        "\033[38;5;255;1m    * * * *  \033[0m",
        "\033[38;5;255;1m   * * * *   \033[0m"],
    'iconLightSleetShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;111m     ‘ \033[38;5;255m*\033[38;5;111m ‘ \033[38;5;255m* \033[0m",
        "\033[38;5;255m    *\033[38;5;111m ‘ \033[38;5;255m*\033[38;5;111m ‘  \033[0m"],
    'iconThunderyShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;228;5m    ⚡\033[38;5;111;25m‘ ‘\033[38;5;228;5m⚡\033[38;5;111;25m‘ ‘ \033[0m",
        "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m"],
    'iconThunderyHeavyRain': [
        "\033[38;5;240;1m     .-.     \033[0m",
        "\033[38;5;240;1m    (   ).   \033[0m",
        "\033[38;5;240;1m   (___(__)  \033[0m",
        "\033[38;5;21;1m  ‚‘\033[38;5;228;5m⚡\033[38;5;21;25m‘‚\033[38;5;228;5m⚡\033[38;5;21;25m‚‘   \033[0m",
        "\033[38;5;21;1m  ‚’‚’\033[38;5;228;5m⚡\033[38;5;21;25m’‚’   \033[0m"],
    'iconThunderySnowShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;255m     *\033[38;5;228;5m⚡\033[38;5;255;25m *\033[38;5;228;5m⚡\033[38;5;255;25m * \033[0m",
        "\033[38;5;255m    *  *  *  \033[0m"],
    'iconLightRain': [
        "\033[38;5;250m     .-.     \033[0m",
        "\033[38;5;250m    (   ).   \033[0m",
        "\033[38;5;250m   (___(__)  \033[0m",
        "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m",
        "\033[38;5;111m   ‘ ‘ ‘ ‘   \033[0m"],
    'iconHeavyRain': [
        "\033[38;5;240;1m     .-.     \033[0m",
        "\033[38;5;240;1m    (   ).   \033[0m",
        "\033[38;5;240;1m   (___(__)  \033[0m",
        "\033[38;5;21;1m  ‚‘‚‘‚‘‚‘   \033[0m",
        "\033[38;5;21;1m  ‚’‚’‚’‚’   \033[0m"],
    'iconLightSnow': [
        "\033[38;5;250m     .-.     \033[0m",
        "\033[38;5;250m    (   ).   \033[0m",
        "\033[38;5;250m   (___(__)  \033[0m",
        "\033[38;5;255m    *  *  *  \033[0m",
        "\033[38;5;255m   *  *  *   \033[0m"],
    'iconHeavySnow': [
        "\033[38;5;240;1m     .-.     \033[0m",
        "\033[38;5;240;1m    (   ).   \033[0m",
        "\033[38;5;240;1m   (___(__)  \033[0m",
        "\033[38;5;255;1m   * * * *   \033[0m",
        "\033[38;5;255;1m  * * * *    \033[0m"],
    'iconLightSleet': [
        "\033[38;5;250m     .-.     \033[0m",
        "\033[38;5;250m    (   ).   \033[0m",
        "\033[38;5;250m   (___(__)  \033[0m",
        "\033[38;5;111m    ‘ \033[38;5;255m*\033[38;5;111m ‘ \033[38;5;255m*  \033[0m",
        "\033[38;5;255m   *\033[38;5;111m ‘ \033[38;5;255m*\033[38;5;111m ‘   \033[0m"],
    'iconFog': [
        "             ",
        "\033[38;5;251m _ - _ - _ - \033[0m",
        "\033[38;5;251m  _ - _ - _  \033[0m",
        "\033[38;5;251m _ - _ - _ - \033[0m",
        "             "],
    'iconUnknown': [
        "    .-.      ",
        "     __)     ",
        "    (        ",
        "     `-’     ",
        "      •      "]
    }

windDir = {
    "N":   "\033[1m↓\033[0m",
    "NNE": "\033[1m↓\033[0m",
    "NE":  "\033[1m↙\033[0m",
    "ENE": "\033[1m↙\033[0m",
    "E":   "\033[1m←\033[0m",
    "ESE": "\033[1m←\033[0m",
    "SE":  "\033[1m↖\033[0m",
    "SSE": "\033[1m↖\033[0m",
    "S":   "\033[1m↑\033[0m",
    "SSW": "\033[1m↑\033[0m",
    "SW":  "\033[1m↗\033[0m",
    "WSW": "\033[1m↗\033[0m",
    "W":   "\033[1m→\033[0m",
    "WNW": "\033[1m→\033[0m",
    "NW":  "\033[1m↘\033[0m",
    "NNW": "\033[1m↘\033[0m",
}


class Query(object):
        def __init__(self, day, city):
                self.day = day
                self.time = [3,4,5,6]
                self.weatherCode = ''
                self.weather = ''
                self.date = ''
                self.hourly = ''
                self.tempC = 0
                self.winddir16Point = ''
                self.windspeedKmph = 0
                self.humidity = 0
                self.chanceofwater = 0
                self.city = city
                # Please input your API key before you run this script.
                self.key = ""

        def query(self):
                # use resquests
                # p={"q":"%s"%self.city, "num_of_days":3, "format":"json",
                # "key": self.key, "lang":"zh"}
                # response=requests.get(base_url,params=p)
                # json_string = response.text
                #
                # user urllib
                url = base_url + "?key=%s&q=%s&num_of_days=3&format=json&lang=zh" % (self.key, self.city)
                response = urllib.urlopen(url)
                json_string = response.read()
                parsed_json = json.loads(json_string)
                data = parsed_json['data']              # acquire the whole data

                try:
                    # Acquire the weather data. The number in [] represent the
                    # day you want to query. '0' means today, and '1' means
                    # tomorrow.
                    self.weather = data['weather'][self.day]
                except KeyError:
                        print "\033[1;31;49m" + "请输入正确的城市或地区！" + "\033[0m"
                        sys.exit()
                self.date = self.weather['date']

        def detail(self, time):
                self.hourly = self.weather['hourly'][time]           # acquire the data in one hour.

                self.weatherCode = self.hourly['weatherCode']
                self.tempC = self.hourly['tempC']
                self.winddir16Point = self.hourly['winddir16Point']
                self.windspeedKmph = self.hourly['windspeedKmph']
                self.chanceofrain = self.hourly['chanceofrain']
                self.chanceofsnow = self.hourly['chanceofsnow']
                self.humidity = self.hourly['humidity']
                self.chanceofwater = int(self.chanceofrain) if int(self.chanceofrain) > int(self.chanceofsnow) else int(self.chanceofsnow)

        def printSingle(self):
                l1 = l2 = l3 = l4 = l5 = ''
                for time in self.time:
                        self.detail(time)
                        l1 += '│' + icons[codes[self.weatherCode]][0] + self.hourly['lang_zh'][0]['value'].encode("utf-8") + '\t\t' if len(self.hourly['lang_zh'][0]['value'].encode("utf-8")) <= 12 else '│' + icons[codes[self.weatherCode]][0] + self.hourly['lang_zh'][0]['value'].encode("utf-8") + '\t'
                        l2 += '│' + icons[codes[self.weatherCode]][1] + temp_color(self.tempC) + "°C"+'\t\t'
                        l3 += '│' + icons[codes[self.weatherCode]][2] + windDir[self.winddir16Point]+" "+ wind_color(self.windspeedKmph) + "km/h" + '\t\t'
                        l4 += '│' + icons[codes[self.weatherCode]][3] + "降水概率:" + str(self.chanceofwater) + "%" + '\t'
                        l5 += '│' + icons[codes[self.weatherCode]][4] + "湿度:" + str(self.humidity) + "%" + '\t\t'

                print l1+"│"
                print l2+"│"
                print l3+"│"
                print l4+"│"
                print l5+"│"

        def printDay(self, delta):
                date_time = datetime.strftime(datetime.today() + timedelta(days=delta),"%Y-%m-%d")
                line1 = "                                                         ┌─────────────┐                                                       "
                line2 = "┌───────────────────────────────┬──────────────────────────%s───────────────────────────┬───────────────────────────────┐" % date_time
                line3 = "│           Morning             │             Noon       └──────┬──────┘    Evening             │            Night              │"
                line4 = "├───────────────────────────────┼───────────────────────────────┼───────────────────────────────┼───────────────────────────────┤"
                endline= "└───────────────────────────────┴───────────────────────────────┴───────────────────────────────┴───────────────────────────────┘"
                print line1
                print line2
                print line3
                print line4
                self.printSingle()
                print endline


# change the temperature's color
def temp_color(temp):
        if temp >= 35 or temp <= -10:
                color = "\033[1;31;49m" + str(temp) + "\033[0m"
        elif (temp >= 25 and temp <35):
                color = "\033[1;33;49m" + str(temp) + "\033[0m"
        elif temp > 10 and temp < 25:
                color = "\033[1;32;49m" + str(temp) + "\033[0m"
        elif temp >-10 and temp <= 10:
                color = "\033[1;34;49m" + str(temp) + "\033[0m"
        return color


def wind_color(windspeed):
        if windspeed <= 5:
                color = "\033[1;32;49m" + str(windspeed) + "\033[0m"
        elif windspeed > 5 and windspeed <=10:
                color = "\033[1;33;49m" + str(windspeed) + "\033[0m"
        else:
                color = "\033[1;34;49m" + str(windspeed) + "\033[0m"
        return color


def main():
        try:
                city = sys.argv[1]
        except IndexError:
                print "\033[1;31;49m" + "请输入您要查询的城市或地区：" + "\033[0m"
                city = raw_input()
                if city == '':
                        sys.exit()
        
        with open('city2pinyin.json', 'r') as c2p:
                dic = json.load(c2p)
                city = dic[city.decode('utf-8')] if city.decode('utf-8') in dic else city

        day = [0,1,2]
        for i in day:
                query = Query(i,city)
                query.query()
                query.printDay(i)

if __name__ == "__main__":
        main()
