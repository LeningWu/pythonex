#!/usr/bin/env/python
#!-*-coding:utf-8 -*-
#!@Time     :2018/10/10  16:05
#!@Author   :Lening

cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car=passengers/cars_driven

print("there are",cars,"cars available")
print("there are only",drivers,"drivers available")
print("ther will be ",cars_not_driven,"empty ars today")



