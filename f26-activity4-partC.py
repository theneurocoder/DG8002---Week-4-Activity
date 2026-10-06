# DG8002 - F26 - Activity 4
# Author Name: Abdullah Alhomoud
# Date: 2026-10-02

# SCENARIO
# A weather station has recorded temperatures over seven days. 
# Your task is to examine the data and produce a short weather report.

#                 M   T   W  Th  F   Sa  Su
temperatures  = [18, 22, 25, 19, 27, 24, 16]

# TODO 0: Create the variables you need for total temperature, # of days above 23 degrees, and hottest day
totalTemperature = 0
daysAbove23 = 0
hottestDay = -1

# TODO 1: Iterate through every recorded temperature
for temp in temperatures:

    # TODO 2: Print the recorded temperature
    print(temp)

    # TODO 3: Add the temperature to total
    totalTemperature = totalTemperature + temp

    # TODO 4: If temperature is above 23, add 1 to the day counter
    if temp > 23:
        daysAbove23 += 1


# TODO 5: Calculate and print the average temeprature for the week.
averageTemperature = totalTemperature / 7
print("Average temperature: " + format(averageTemperature, ".2f"))

# TODO 6: Print how many days exceeded 23 degrees
print("Days above 23: " + str(daysAbove23))

# TODO 7: Print the -> index <- of the highest temperature.
hottestDay = temperatures.index(max(temperatures))
print("Highest Temperature Index: " + str(hottestDay))

# EXPECTED OUTPUT
# Average Temperature: 21.57
# Days Above 23:  3
# Highest Temperature Index: 4  


