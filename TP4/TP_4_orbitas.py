# ---- GUIDE 4 - ORBITS ----

"""  EXERCISE 1
Consider that at a given moment the Earth starts moving on the direction of the y axis
Let's first define some positions as lists and constants.
Be sure to explicit the magnitude of vectors as the type "float" in order for np.sqrt() to work.

*   `r_x_earth = [-147095000000.0, -147095000000.0]`
*   `r_y_earth = [0.0, 2617920000.0]`
*   `dt = 60 * 60 * 24` (Earth day in seconds).
*   `total_earth_days = 400` (simulate a bit more than 1 Earth Year)
*   `x_sol = 0, y_sol = 0` (Suppose that the center of the system , the Sun, is fixed)

To simulate the movement of the planet around the Sun, define some functions that return the acceleration
Use the positions of both celestial bodies (refer to the doc to see formulas)
"""

# Libraries
import numpy as np
import matplotlib.pyplot as plt
import imageio

""" Use of scipy library (https://docs.scipy.org/doc/scipy/reference/constants.html)
Is restricted due to possible overlapping of variables. """

# Declaration of variables
G_Earth = 6.693 * 10 ** -11  # Gravitational constants. Units: N*m^2/kg^2
M_Earth = 1.98 * 10 ** 30  # Earth's mass, units=kg

earth_day_sec = 60 * 60 * 24  # Duration of a day on Earth measured in seconds
total_earth_days = 400  # Simulated Earth's Days

"Earth's first position vectors (measured in meters) must contain (x,y) data of two days."
# Position of Earth on Day 0 in R2 plane
earth_r_day0 = [-147095000000.0, 0.0]
# Position of Earth on Day 1 in R2 plane
earth_r_day1 = [-147095000000.0, 2617920000.0]

# Sun's position: we consider it a fixed constant
r_sun = [0, 0]


def calculate_acceleration(planet_position):
    # Input must be a list with x and y coordinates of planet

    # Calculate coordinates and vector module of planet
    x = r_sun[0] - planet_position[0]
    y = r_sun[1] - planet_position[1]

    # Check if provided coordinates are in the same vector space or else notify a discrepancy
    if len(r_sun) == len(planet_position) == 2:
        d = np.sqrt(x**2 + y**2)
        # Calculate gravitational acceleration
        acceleration_x = ((G_Earth * M_Earth) / d ** 2) * (x / d)
        acceleration_y = ((G_Earth * M_Earth) / d ** 2) * (y / d)
        acceleration_2Dlist = [acceleration_x, acceleration_y]
        return acceleration_2Dlist
        # Returns a list of two elements with the x and y coordinates of acceleration vector
    else: return print('The coordinates are in different vector spaces')


# Test function
print('Test calculate_acceleration Day0 ', calculate_acceleration(earth_r_day0))
print('Test calculate_acceleration Day1 ', calculate_acceleration(earth_r_day1))

""" Exercise 2
Define variables and functions as necessary in order to calculate the first two acceleration vectors
This will allow the use of Verlet's algorithm to generate more vectors"""

# Lists that will contain the x and y coordinates of calculated accelerations
earth_x_accelerations = []
earth_y_accelerations = []

day_acc = calculate_acceleration(earth_r_day0)
earth_x_accelerations.append(day_acc[0])
earth_y_accelerations.append(day_acc[1])

day_acc = calculate_acceleration(earth_r_day1)
earth_x_accelerations.append(day_acc[0])
earth_y_accelerations.append(day_acc[1])

print('Accelerations on x (m/s^2)', earth_x_accelerations)
print('Accelerations on y (m/s^2)', earth_y_accelerations)
print('Measured day: [0,1]')

""" Exercise 3
Define a function that uses Verlet's algorithm.
It should receive two subsequent positions as a list type of 2D each as well as the acceleration for those positions.
Then it must return the next position vector for the following Earth's day
"""


def int_verlet_calc(pos_anterior, pos_actual, acceleration_actual, dt):
    # New position in x
    pos_x = 2 * pos_actual[0] - pos_anterior[0] + acceleration_actual[0] * dt ** 2
    # New position in y
    pos_y = 2 * pos_actual[1] - pos_anterior[1] + acceleration_actual[1] * dt ** 2
    pos_posterior = [pos_x, pos_y]
    return pos_posterior  # returns list with new planet positions


# test int_verlet_calc
test_acc = calculate_acceleration(earth_r_day1)
int_verlet_calc(earth_r_day0, earth_r_day1, test_acc, earth_day_sec)

""" Exercise 4
Make a cycle that uses int_verlet_calc to calculate and save the position, acceleration and Earth day in lists"""

initial_acc = [earth_x_accelerations[1], earth_y_accelerations[1]]


def calculate_orbit(planet_position_dia, planet_position_ant, actual_acc, days):
    # Assign variables in local scope
    r_anterior = planet_position_ant  # = [r_x_earth[0], r_y_earth[0]] # position on day 0
    r_actual = planet_position_dia  # [r_x_earth[1], r_y_earth[1]] # position on day 1
    # Assign 'actual' positions and accelerations as those of day 1
    dias_list = [1]
    rx_list = [r_actual[0]]
    ry_list = [r_actual[1]]
    acc_x_list = [actual_acc[0]]
    acc_y_list = [actual_acc[1]]
    for i in range(2, days + 1):
        # Save day number
        dias_list.append(i)
        # Calculate acceleration of current day
        acc_xy_list = calculate_acceleration(r_actual)
        # Calculate next position
        r_posterior = int_verlet_calc(r_anterior, r_actual, acc_xy_list, earth_day_sec)
        # Save new positions
        rx_list.append(r_posterior[0])
        ry_list.append(r_posterior[1])
        # Save new accelerations
        acc_xy_list = calculate_acceleration(r_posterior)
        acc_x_list.append(acc_xy_list[0])
        acc_y_list.append(acc_xy_list[1])
        # Refresh last and current positions for next cycle
        r_anterior = r_actual
        r_actual = r_posterior
    return rx_list, ry_list, acc_x_list, acc_y_list, dias_list


x_positions, y_positions, x_accelerations, y_accelerations, Dias = calculate_orbit(earth_r_day1,
                                                                                   earth_r_day0,
                                                                                   initial_acc,
                                                                                   total_earth_days)

print('List of x coordinates, size =', len(x_positions), x_positions)
print('List of y coordinates, size=', len(y_positions), y_positions)
print('List of acceleration in x, size=', len(x_accelerations), x_accelerations)
print('List of acceleration in y, size=', len(y_accelerations), y_accelerations)
print('List of days, size=', len(Dias), Dias)

""" Exercise 5
Graph: trajectory in (x,y) plane """


def picture_planet_track(data_x_positions, data_y_positions, planet_name):
    plt.style.use('dark_background')
    # check that lists with coordinates have the same size
    if len(data_x_positions) == len(data_y_positions):
        plt.plot(data_x_positions, data_y_positions, color='grey')
        # generate Sun's position in the graph. ’yo ’ means a yellow dot, ms indicates its size
        plt.plot(r_sun[0], r_sun[1], 'yo', ms=20)
        plt.title(planet_name+"'s trajectory")
        plt.xlabel('x coordinates')
        plt.ylabel('y coordinates')
        plt.show()


picture_planet_track(x_positions, y_positions, "Earth")


""" Exercise 6
Graph: acceleration as a function of time (measured in days)
Later generate an animated video of the translational movement. We wil need to handle the images that compose it. """

if len(Dias) == len(x_accelerations):  # check that lists are equally sized
    plt.plot(Dias, x_accelerations, color='cyan')
    plt.title("Earth's acceleration on x axis")
    plt.xlabel('Days')
    plt.ylabel('x coordinates (meters)')
    plt.show()
else:
    print('Error: There is a discrepancy between the number days and the number of x coordinates')

if len(Dias) == len(y_accelerations):
    plt.plot(Dias, y_accelerations, color='cyan')
    plt.title("Earth's acceleration movement on y axis")
    plt.xlabel('Days')
    plt.ylabel('y coordinates (meters)')
    plt.show()
else:
    print('Error: There is a discrepancy between the number days and the number of y coordinates')

""" Exercise 7
Elaborate a function that receives positions and a day and makes a graphic of the planet's trajectory
and pictures the Sun a a reference and the planet's positions as a small circle."""


def make_orbit_picture(list_x, list_y, sun_position, dia):
    # clear the figure as precaution
    plt.clf()
    # generate a trajectory graph (x,y)
    plt.plot(list_x, list_y, 'grey')
    plt.title("Earth's orbit around the Sun. Day: " + str(dia))
    # generate Sun's position in the graph. ’yo ’ means a yellow dot, ms indicates its size
    plt.plot(sun_position[0], sun_position[1], 'yo', ms=20)
    # generate Earth's positions as a smaller blue dot
    plt.plot(list_x[dia + 1], list_y[dia + 1], 'bo', ms=10)
    # plt.show()  # test result if () removed
    return


# Test make_orbit_picture function
make_orbit_picture(x_positions, y_positions, r_sun, 60)

""" Exercise 8
Make a function that generates and saves an animation with imageio, following the library's webpage suggestions
"""


def make_orbit_video(list_x, list_y, sun_position, name_of_video):
    print('Preparing video, please wait ...')
    photos_list = []  # list with saves images
    for i in range(len(list_x)):
        if i % 2 == 0:  # Save one out of two images
            make_orbit_picture(list_x, list_y, sun_position, i)
            plt.savefig(name_of_video + '.png')
            photos_list.append(imageio.imread(name_of_video + '.png'))
        # Verification test to corroborate saving
        # print (str(i) + ' out of ' +str(len( list_x ) ) + ' saves images')
    imageio.mimsave(name_of_video + '.mp4', photos_list)  # create video
    print('Video saved as ' + name_of_video + '.mp4')


make_orbit_video(x_positions, y_positions, r_sun, 'Translational_movement')

""" Exercise 9
How would Earth's trajectory change if it moved twice as fast?
Hint: to reflect this modification, me must double the value of list_y[1] and calculate it all over again

Answer: initially we would have a circular orbit but then it follows a somewhat linear trajectory """

# Remember that previously in the code list_y[1] = earth_r_day1[1]
initial_r2 = [earth_r_day1[0], earth_r_day1[1] * 2]

# Calculate again the acceleration of Day 1:
initial_acc2 = calculate_acceleration(earth_r_day1)

x_positions2, y_positions2, x_accelerations2, y_accelerations2, Dias2 = calculate_orbit(initial_r2,
                                                                                        earth_r_day0,
                                                                                        initial_acc2,
                                                                                        total_earth_days)

print('Length of  x_positions2 ', len(x_positions2), x_positions2)
print('Length of  y_positions2 ', len(y_positions2), y_positions2)
print('Length of  x_accelerations2 ', len(x_accelerations2), x_accelerations2)
print('Length of  y_accelerations2 ', len(y_accelerations2), y_accelerations2)
print('Length of  list Dias ', len(Dias), Dias2)

if len(x_positions2) == len(y_positions2):  # check that lists have the same size
    plt.plot(x_positions2, y_positions2, color='grey')
    plt.title("Earth's trajectory if it moved twice as fast")
    plt.xlabel('x coordinates')
    plt.ylabel('y coordinates')
    plt.show()

make_orbit_picture(x_positions2, y_positions2, r_sun, 60)

""" Exercise 10
What if instead Earth went half as fast? Should a day be shorter?
Answer: now the Earth moves too close or too far from the Sun
"""

initial_r3 = [earth_r_day1[0], earth_r_day1[1] * 0.5]
# Calculate again the acceleration of Day 1:
initial_acc3 = calculate_acceleration(earth_r_day1)  # acceleration en x , acceleration en y en el primer dia

x_positions3, y_positions3, x_accelerations3, y_accelerations3, Dias3 = calculate_orbit(initial_r3,
                                                                                        earth_r_day0,
                                                                                        initial_acc3,
                                                                                        total_earth_days)

if len(x_positions3) == len(y_positions3):  # check that lists have the same size
    plt.plot(x_positions3, y_positions3, color='grey')
    plt.title("Earth's trajectory if it moved half as fast")
    plt.xlabel('x coordinates')
    plt.ylabel('y coordinates')
    plt.show()

make_orbit_picture(x_positions3, y_positions3, r_sun, 60)

""" Exercise 11
Modify the functions 'make_orbit_picture' and 'make_orbit_video' so they can receive acceleration's lists
Add them to the images.
The matplotlib function (x1,y1,x2,y2) may be useful, where 1 is the origin and 2 the destination of the vector.
"""


def trajectory_plus_acc_picture(list_x, list_y, sun_position, acceleration_x, acceleration_y, dia):
    # clear the plotted figure
    plt.clf()
    # display trajectory
    plt.plot(list_x, list_y, 'grey')
    plt.title("Earth's trajectory around the Sun. Day: " + str(dia))
    # display Sun's position
    plt.plot(sun_position[0], sun_position[1], 'yo', ms=20)
    # display Earth's position
    plt.plot(list_x[dia + 1], list_y[dia + 1], 'bo', ms=10)
    # display acceleration vector
    plt.arrow(list_x[dia], list_y[dia], acceleration_x[dia] * 10 ** 12.5, acceleration_y[dia] * 10 ** 12.5,
              width=10 ** 9.5, color='green')
    # plt.show
    return


trajectory_plus_acc_picture(x_positions3, y_positions3, r_sun, x_accelerations3, y_accelerations3, 300)


def trajectory_plus_acc_video(list_x, list_y, sun_position, acceleration_x, acceleration_y, name_of_video):
    print('Preparing video, please wait ...')
    photos_list = []  # save images in a list
    for i in range(len(list_x)):
        if i % 2 == 0:  # save one out of two pictures
            trajectory_plus_acc_picture(list_x, list_y, sun_position, acceleration_x, acceleration_y, i)
            plt.savefig(name_of_video + '.png')
            photos_list.append(imageio.imread(name_of_video + '.png'))
        # print (str(i) + ' out of ' +str(len( list_x ) ) + 'saves pictures') # test saving
    imageio.mimsave(name_of_video + '.mp4', photos_list)  # create video
    print('Video saved as ' + name_of_video + '.mp4')


trajectory_plus_acc_video(x_positions3, y_positions3, r_sun, x_accelerations3, y_accelerations3,
                          'Orbit_+_acceleration')

""" Exercise 12 (optional)
How would you calculate velocity of each day? Display as a function of time
"""

""" Exercise 13 (optional)
Explore NASA's web page to obtain positions and masses of more planets and add them to the animation
Note that units are astronomical and must be converted to meters
https://ssd.jpl.nasa.gov/horizons.cgi#results
"""

""" Exercise 14
Search on NASA's web page to obtain the position of Earth on your birthdate
Try to determine when was the first perihelion and aphelion of your life (min and max distance to the Sun)
See also https://www.timeanddate.com/date/dateadd.html
"""
