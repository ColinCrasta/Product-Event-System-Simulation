import numpy
from controller import *  # imports all methods from controller.py


def servinsp1(iterations):
    #This part finds the mean from the data file service times
    sum = 0
    minutes_array = open('servinsp1.dat').read().splitlines()
    counter = 0
    while (counter < 300):
        sum += float(minutes_array[counter])*60
        counter += 1
    datafile_mean = sum / 300

    #This part gets a certain amount of randomly generated numbers
    generated_sum = 0
    generated_counter = 0
    while (generated_counter < iterations):
        #print(generate_random_number('servinsp1.dat'))
        generated_sum += generate_random_number('servinsp1.dat')
        generated_counter += 1

    generated_mean = generated_sum / iterations

    print('Service time comparison for inspector one')
    print('Mean from the data file in seconds:', datafile_mean)
    print('Mean from random number generation in seconds:', generated_mean)
    print('Comparison in percentage: ', (abs(datafile_mean - generated_mean) / datafile_mean) * 100, '\n')


def servinsp2c2(iterations):
    #This part finds the mean from the data file service times
    sum = 0
    minutes_array = open('servinsp22.dat').read().splitlines()
    counter = 0
    while (counter < 300):
        sum += float(minutes_array[counter])*60
        counter += 1
    datafile_mean = sum / 300

    #This part gets a certain amount of randomly generated numbers
    generated_sum = 0
    generated_counter = 0
    while (generated_counter < iterations):
        #print(generate_random_number('servinsp1.dat'))
        generated_sum += generate_random_number('servinsp22.dat')
        generated_counter += 1

    generated_mean = generated_sum / iterations

    print('Service time comparison for inspector two (component two)')
    print('Mean from the data file in seconds:', datafile_mean)
    print('Mean from random number generation in seconds:', generated_mean)
    print('Comparison in percentage: ', (abs(datafile_mean - generated_mean) / datafile_mean) * 100, '\n')


def servinsp2c3(iterations):
    #This part finds the mean from the data file service times
    sum = 0
    minutes_array = open('servinsp23.dat').read().splitlines()
    counter = 0
    while (counter < 300):
        sum += float(minutes_array[counter])*60
        counter += 1
    datafile_mean = sum / 300

    #This part gets a certain amount of randomly generated numbers
    generated_sum = 0
    generated_counter = 0
    while (generated_counter < iterations):
        #print(generate_random_number('servinsp1.dat'))
        generated_sum += generate_random_number('servinsp23.dat')
        generated_counter += 1

    generated_mean = generated_sum / iterations

    print('Service time comparison for inspector two (component three)')
    print('Mean from the data file in seconds:', datafile_mean)
    print('Mean from random number generation in seconds:', generated_mean)
    print('Comparison in percentage: ', (abs(datafile_mean - generated_mean) / datafile_mean) * 100, '\n')


def ws1(iterations):
    #This part finds the mean from the data file service times
    sum = 0
    minutes_array = open('ws1.dat').read().splitlines()
    counter = 0
    while (counter < 300):
        sum += float(minutes_array[counter])*60
        counter += 1
    datafile_mean = sum / 300

    #This part gets a certain amount of randomly generated numbers
    generated_sum = 0
    generated_counter = 0
    while (generated_counter < iterations):
        #print(generate_random_number('servinsp1.dat'))
        generated_sum += generate_random_number('ws1.dat')
        generated_counter += 1

    generated_mean = generated_sum / iterations

    print('Service time comparison for workstation one')
    print('Mean from the data file in seconds:', datafile_mean)
    print('Mean from random number generation in seconds:', generated_mean)
    print('Comparison in percentage: ', (abs(datafile_mean - generated_mean) / datafile_mean) * 100, '\n')

def ws2(iterations):
    #This part finds the mean from the data file service times
    sum = 0
    minutes_array = open('ws2.dat').read().splitlines()
    counter = 0
    while (counter < 300):
        sum += float(minutes_array[counter])*60
        counter += 1
    datafile_mean = sum / 300

    #This part gets a certain amount of randomly generated numbers
    generated_sum = 0
    generated_counter = 0
    while (generated_counter < iterations):
        #print(generate_random_number('servinsp1.dat'))
        generated_sum += generate_random_number('ws2.dat')
        generated_counter += 1

    generated_mean = generated_sum / iterations

    print('Service time comparison for workstation two')
    print('Mean from the data file in seconds:', datafile_mean)
    print('Mean from random number generation in seconds:', generated_mean)
    print('Comparison in percentage: ', (abs(datafile_mean - generated_mean) / datafile_mean) * 100, '\n')

def ws3(iterations):
    #This part finds the mean from the data file service times
    sum = 0
    minutes_array = open('ws3.dat').read().splitlines()
    counter = 0
    while (counter < 300):
        sum += float(minutes_array[counter])*60
        counter += 1
    datafile_mean = sum / 300

    #This part gets a certain amount of randomly generated numbers
    generated_sum = 0
    generated_counter = 0
    while (generated_counter < iterations):
        #print(generate_random_number('servinsp1.dat'))
        generated_sum += generate_random_number('ws3.dat')
        generated_counter += 1

    generated_mean = generated_sum / iterations

    print('Service time comparison for workstation three')
    print('Mean from the data file in seconds:', datafile_mean)
    print('Mean from random number generation in seconds:', generated_mean)
    print('Comparison in percentage: ', (abs(datafile_mean - generated_mean) / datafile_mean) * 100, '\n')

if __name__ == '__main__':
    servinsp1(5000)
    servinsp2c2(5000)
    servinsp2c3(5000)
    ws1(5000)
    ws2(5000)
    ws3(5000)