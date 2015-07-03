#终端天气预报脚本
使用Python编写的一款用于Linux/Unix终端下的查询天气预报的脚本。

基于另一个使用Go语言编写的天气预报脚本[schachmat/wego](https://github.com/schachmat/wego)改写而来。

支持简体中文。

支持使用urllib库和requests库两种查询方式，默认为使用urllib。

屏幕截图
![屏幕截图](https://github.com/smartczy/weather_py/raw/master/src/weather.png)
#使用方法
**注意：运行程序前，请先在Query类中写入你自己的API key。**

终端需要在全屏状态下，否则排版会被打乱。

在终端中输入的格式为：
```
~/weather_py/src$ python weather.py [CITY]
```
#测试环境
* Unbuntu 14.04 32bit
* Python 2.7

#TODO LIST
* 基于IP地址查询天气预报

#License(MIT)
Copyright (c) 2014-2015 smartczy
