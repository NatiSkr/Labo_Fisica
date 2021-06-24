# ---- GUIDE 4 - ORBITS ----

"""  EXERCISE 1
Consider that at a given moment the Earth starts moving on the direction of the y axis
Let's first define some positions as lists and constants.
Be sure to explicit the magnitude of vectors as the type "float" in order for np.sqrt() to work.

*   `r_x_earth = [-147095000000.0, -147095000000.0]`
*   `r_y_earth = [0.0, 2617920000.0]`
*   `dt = 60 * 60 * 24` (Earth day in seconds).
*   `earth1y = 400` (simulate a bit more than 1 Earth Year)
*   `x_sol = 0, y_sol = 0` (Suppose that the center of the system , the Sun, is fixed)

To simulate the movement of the planet around the Sun, define some functions that return the acceleration
Use the positions of both celestial bodies (refer to the doc to see formulas)
"""

# Libraries
import numpy as np
import matplotlib.pyplot as plt
import imageio
import imshow
plt.style.use('dark_background')

""" Use of scipy library (https://docs.scipy.org/doc/scipy/reference/constants.html)
Is restricted due to possible overlapping of variables. """

def calculate_acceleration(planet_position):
    # Input must be a list with x and y coordinates of planet

    # Calculate coordinates and vector module of planet
    x = r_sun[0] - planet_position[0]
    y = r_sun[1] - planet_position[1]
    d = np.sqrt(x ** 2 + y ** 2)
    # Check if provided coordinates are in the same vector space or else notify a discrepancy
    if len(r_sun) == len(planet_position) == 2:
        # Calculate gravitational acceleration
        acceleration_x = ((universal_G * M_Sun) / d ** 2) * (x / d)
        acceleration_y = ((universal_G * M_Sun) / d ** 2) * (y / d)
        acceleration_2Dlist = [acceleration_x, acceleration_y]
        return acceleration_2Dlist
        # Returns a list of two elements with the x and y coordinates of acceleration vector
    else:
        return print('The coordinates are in different vector spaces')


""" Exercise 2
Define variables and functions as necessary in order to calculate the first two acceleration vectors
This will allow the use of Verlet's algorithm to generate more vectors"""


""" Exercise 3
Define a function that uses Verlet's algorithm.
It should receive two subsequent positions as a list type of 2D each as well as the acceleration for those positions.
Then it must return the next position vector for the following Earth's day
"""


def int_verlet_calc(pos_anterior, pos_actual, acceleration_actual):
    # New position in x
    # dt is the day on earth in seconds 60*60*24=86400s
    pos_x = 2 * pos_actual[0] - pos_anterior[0] + acceleration_actual[0] * 86400 ** 2
    # New position in y
    pos_y = 2 * pos_actual[1] - pos_anterior[1] + acceleration_actual[1] * 86400 ** 2
    pos_posterior = [pos_x, pos_y]
    return pos_posterior  # returns list with new planet positions


""" Exercise 4
Make a cycle that uses int_verlet_calc to calculate and save the position, acceleration and Earth day in lists"""


def calculate_orbit(planet_position_dia, planet_position_ant, actual_acc, days):
    # Assign variables in local scope
    r_anterior = planet_position_ant
    r_actual = planet_position_dia
    # Assign 'actual' positions and accelerations as those of day 1
    dias_list = [1]
    rx_list = [planet_position_dia[0]]
    ry_list = [planet_position_dia[1]]
    acc_x_list = [actual_acc[0]]
    acc_y_list = [actual_acc[1]]
    for i in range(2, days + 1):
        # Save day number
        dias_list.append(i)
        # Calculate acceleration of current day
        acc_xy_list = calculate_acceleration(r_actual)
        # Calculate next position
        r_posterior = int_verlet_calc(r_anterior, r_actual, acc_xy_list)
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
    return rx_list, ry_list, acc_x_list, acc_y_list


""" Exercise 5
Graph: trajectory in (x,y) plane """


def picture_planet_track(data_x_earth, data_y_earth, planet_name, filename):
    plt.clf()
    # check that lists with coordinates have the same size
    if len(data_x_earth) == len(data_y_earth):
        plt.plot(data_x_earth, data_y_earth, color='grey')
        # generate Sun's position in the graph. ’yo ’ means a yellow dot, ms indicates its size
        plt.plot(r_sun[0], r_sun[1], 'yo', ms=20)
        plt.title(planet_name+"'s trajectory")
        plt.xlabel('x coordinates (meters)')
        plt.ylabel('y coordinates (meters)')
        plt.savefig(filename)
        print("\n Plot saved as "+filename)
        # plt.show()
    else:
        print('Error: There is a discrepancy between the number of days and the quantity of coordinates')


""" Exercise 6
Graph: acceleration as a function of time (measured in days)
Later generate an animated video of the translational movement. We wil need to handle the images that compose it. """


def picture_planet_ACCvsTIME(x_or_y, data_1d_acc, planet_name, filename):
    plt.clf()
    plt.plot(data_1d_acc, color='cyan')
    plt.title(planet_name+"'s acceleration on "+x_or_y+" axis")
    plt.xlabel('Days')
    plt.ylabel('Acceleration (meters/seconds^2)')
    plt.savefig(filename)
    print("\n Plot saved as " + filename)
    # plt.show()



""" Exercise 7
Elaborate a function that receives positions and a day and makes a graphic of the planet's trajectory
and pictures the Sun a a reference and the planet's positions as a small circle."""


def make_orbit_picture(list_x, list_y, dia, planet_color):
    # generate a trajectory graph (x,y)
    plt.plot(list_x, list_y, 'grey')
    plt.title("Earth's orbit around the Sun. Day: " + str(dia))
    plt.xlabel('x coordinates (meters)')
    plt.ylabel('y coordinates (meters)')

    # generate Sun's position in the graph. ’yo ’ means a yellow dot, ms indicates its size
    plt.plot(r_sun[0], r_sun[1], 'yo', ms=20)

    # generate planet's positions as a smaller blue dot
    plt.plot(list_x[dia + 1], list_y[dia + 1], planet_color, ms=10)

    # plt.show()  # remove comment to show plot
    return


""" Exercise 8
Make a function that generates and saves an animation with imageio, following the library's webpage suggestions
"""


def make_orbit_video(list_x, list_y, name_of_video):
    print('\n Preparing video, please wait ...')
    photos_list = []  # list with saves images
    for i in range(len(list_x)):
        # clear the figure as precaution
        plt.clf()
        if i % 2 == 0:  # Save one out of two images
            make_orbit_picture(list_x, list_y, i, 'blue')
            plt.savefig(name_of_video + '.png')
            photos_list.append(imageio.imread(name_of_video + '.png'))
        # Verification test to corroborate saving
        # print (str(i) + ' out of ' +str(len( list_x ) ) + ' saves images')
    imageio.mimsave(name_of_video + '.mp4', photos_list)  # create video
    print('\n Video saved as ' + name_of_video + '.mp4')


""" Exercise 9
How would Earth's trajectory change if it moved twice as fast?
Hint: to reflect this modification, me must double the value of list_y[1] and calculate it all over again
Answer: initially we would have a circular orbit but then it follows a somewhat linear trajectory
Remember that previously in the code list_y[1] = dicc_earth['day1coord'][1]
"""


""" Exercise 10 What if instead Earth went half as fast? Should a day be shorter?
Answer: now the Earth moves too close or too far from the Sun
"""


""" Exercise 11
Modify the functions 'make_orbit_picture' and 'make_orbit_video' so they can receive acceleration's lists
Add them to the images.
The matplotlib function (x1,y1,x2,y2) may be useful, where 1 is the origin and 2 the destination of the vector.
"""


def trajectory_plus_acc_picture(list_x, list_y, acceleration_x, acceleration_y, dia):
    # clear the plotted figure
    plt.clf()

    # display trajectory
    plt.plot(list_x, list_y, 'grey')
    plt.title("Earth's trajectory around the Sun. Day: " + str(dia))

    # display Sun's position
    plt.plot(r_sun[0], r_sun[1], 'yo', ms=20)

    # display Earth's position
    plt.plot(list_x[dia + 1], list_y[dia + 1], 'bo', ms=10)

    # display acceleration vector
    plt.arrow(list_x[dia], list_y[dia],
              acceleration_x[dia] * 10 ** 12.5,
              acceleration_y[dia] * 10 ** 12.5,
              width=10 ** 9.5,
              color='green')
    return


def trajectory_plus_acc_video(list_x, list_y, acceleration_x, acceleration_y, name_of_video):
    print('\n Preparing video, please wait ...')
    photos_list = []  # save images in a list
    for i in range(len(list_x)):
        if i % 2 == 0:  # save one out of two pictures
            trajectory_plus_acc_picture(list_x, list_y, acceleration_x, acceleration_y, i)
            plt.savefig(name_of_video + '.png')
            photos_list.append(imageio.imread(name_of_video + '.png'))
        # print (str(i) + ' out of ' +str(len( list_x ) ) + 'saves pictures') # test saving
    imageio.mimsave(name_of_video + '.mp4', photos_list)  # create video
    print('\n Video saved as ' + name_of_video + '.mp4')


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

# Declaration of global variables
AU = 149597870700  # astronomical units au in meters
universal_G = 6.67 * 10 ** -11  # Gravitational constants. Units: N*m^2/kg^2
M_Sun = 1988500 * 10 ** 24  # Sun's mass, units=kg
r_sun = [0, 0]  # Sun's position: we consider it a fixed constant
earth1y = 375  # Simulated Earth's Days
std_size = 3 # earth size for plots

" --- Mercury's data ------------------"
dicc_mercury = {'name': 'Mercury',
                'color': 'chocolate',
                'relative size': std_size*0.3,
                'period in days': int(0.25 * earth1y),
                'day0coord': [3.527194038524470 * (10 ** -1) * AU, -3.992007990089807 * (10 ** -2) * AU],
                'day1coord': [3.496966842279213 * (10 ** -1) * AU, -1.064190753450797 * (10 ** -2) * AU]
                }

" --- Venus's trajectory data ------------------"
dicc_venus = {'name': 'Venus',
              'color': 'sandybrown',
              'relative size': std_size*0.9,
              'period in days': int(0.7 * earth1y),
              'day0coord': [6.699101302128549 * (10 ** -1) * AU, -2.590495337952708 * (10 ** -1) * AU],
              'day1coord': [6.769025185681680 * (10 ** -1) * AU, -2.402092653508008 * (10 ** -1) * AU]
              }

" --- Earth's trajectory data ------------------"
dicc_earth = {'name': 'Earth',
              'color': 'limegreen',
              'relative size': std_size,
              'period in days': int(earth1y),
              'day0coord': [-9.893730268079107 * (10 ** -1) * AU, 1.525312641360373 * (10 ** -1) * AU],
              'day1coord': [-9.920501473347642 * (10 ** -1) * AU, 1.354183249761766 * (10 ** -1) * AU]
              }

" --- Mars's trajectory data ------------------"
dicc_mars = {'name': 'Mars',
             'color': 'orangered',
             'relative size': std_size*0.5,
             'period in days': int(1.9 * earth1y),
             'day0coord': [-1.655510318528293 * AU, 1.657061664751504 * (10 ** -1) * AU],
             'day1coord': [-1.656291363095773 * AU, 1.529609327727200 * (10 ** -1) * AU]
             }

" --- Jupyter's trajectory data ------------------"
dicc_jupyter = {'name': 'Jupyter',
                'color': 'khaki',
                'relative size': std_size*11,
                'period in days': int(12 * earth1y),
                'day0coord': [2.849574432688381 * AU, -4.234571266057721 * AU],
                'day1coord': [2.855729459244833 * AU, -4.229999656426285 * AU]
                }

" --- Saturn's trajectory data ------------------"
dicc_saturn = {'name': 'Saturn',
               'color': 'goldenrod',
               'relative size': std_size*9,
               'period in days': int(29 * earth1y),
               'day0coord': [9.302046396124146 * AU, 1.588305128062075 * AU],
               'day1coord': [9.300809480419099 * AU, 1.593792603601794 * AU]
               }

" --- Uranus's trajectory data ------------------"
dicc_uranus = {'name': 'Uranus',
               'color': 'lightskyblue',
               'relative size': std_size*4,
               'period in days': int(84 * earth1y),
               'day0coord': [1.140614787022116 * 10 * AU, -1.618102574730362 * 10 * AU],
               'day1coord': [1.140933328188972 * 10 * AU, -1.617894211828149 * 10 * AU]
               }

" --- Neptune's trajectory data ------------------"
dicc_neptune = {'name': 'Neptune',
                'color': 'royalblue',
                'relative size': std_size*3.5,
                'period in days': int(165 * earth1y),
                'day0coord': [1.406373989566836 * 10 * AU, -2.666345412015452 * 10 * AU],
                'day1coord': [1.406649648193033 * 10 * AU, -2.666197143806701 * 10 * AU]
                }

" Calculate Mercury's orbit"
x_mercury, y_mercury, x_acc_mercury, y_acc_mercury = calculate_orbit(dicc_mercury['day1coord'],
                                                                     dicc_mercury['day0coord'],
                                                                     calculate_acceleration(dicc_mercury['day1coord']),
                                                                     dicc_neptune['period in days'])
" Calculate Venus's orbit"
x_venus, y_venus, x_acc_venus, y_acc_venus = calculate_orbit(dicc_venus['day1coord'],
                                                             dicc_venus['day0coord'],
                                                             calculate_acceleration(dicc_venus['day1coord']),
                                                             dicc_neptune['period in days'])
" Calculate Earth's orbit"
x_earth, y_earth, x_acc_earth, y_acc_earth = calculate_orbit(dicc_earth['day1coord'],
                                                             dicc_earth['day0coord'],
                                                             calculate_acceleration(dicc_earth['day1coord']),
                                                             dicc_neptune['period in days'])
" Calculate Mars's orbit"
x_mars, y_mars, x_acc_mars, y_acc_mars = calculate_orbit(dicc_mars['day1coord'],
                                                         dicc_mars['day0coord'],
                                                         calculate_acceleration(dicc_mars['day1coord']),
                                                         dicc_neptune['period in days'])
" Calculate Jupyter's orbit"
x_jupyter, y_jupyter, x_acc_jupyter, y_acc_jupyter = calculate_orbit(dicc_jupyter['day1coord'],
                                                                     dicc_jupyter['day0coord'],
                                                                     calculate_acceleration(dicc_jupyter['day1coord']),
                                                                     dicc_neptune['period in days'])
" Calculate Saturn's orbit"
x_saturn, y_saturn, x_acc_saturn, y_acc_saturn = calculate_orbit(dicc_saturn['day1coord'],
                                                                 dicc_saturn['day0coord'],
                                                                 calculate_acceleration(dicc_saturn['day1coord']),
                                                                 dicc_neptune['period in days'])
" Calculate Uranus's orbit"
x_uranus, y_uranus, x_acc_uranus, y_acc_uranus = calculate_orbit(dicc_uranus['day1coord'],
                                                                 dicc_uranus['day0coord'],
                                                                 calculate_acceleration(dicc_uranus['day1coord']),
                                                                 dicc_neptune['period in days'])
# Calculate orbit
x_neptune, y_neptune, x_acc_neptune, y_acc_neptune = calculate_orbit(dicc_neptune['day1coord'],
                                                                     dicc_neptune['day0coord'],
                                                                     calculate_acceleration(dicc_neptune['day1coord']),
                                                                     dicc_neptune['period in days'])


" The following resolves exercises 5 to 11 of assignment --------------------"
"""
# Exercise 5
picture_planet_track(x_earth, y_earth, "Earth", "EarthOrbit.jpg")

# Exercise 6
picture_planet_ACCvsTIME("x", x_earth, "Earth", "Earth_x_acceleration.jpg")

picture_planet_ACCvsTIME("y", y_earth, "Earth", "Earth_y_acceleration.jpg")

# Exercise 8
make_orbit_video(x_earth, y_earth, 'Normal translational movement')


# Exercise 9: if Earth moved twice as fast
initial_r2 = [dicc_earth['day1coord'][0], dicc_earth['day1coord'][1] * 2]

x_earth2, y_earth2, x_acc_earth2, y_acc_earth2 = calculate_orbit(initial_r2, dicc_earth['day0coord'], calculate_acceleration(initial_r2), earth1y)

picture_planet_track(x_earth2, y_earth2, "Earth", "EarthOrbit_TwiceVel.jpg")


# Exercise 10: if Earth moved half as fast
initial_r3 = [dicc_earth['day1coord'][0], dicc_earth['day1coord'][1] * 0.5]

x_earth3, y_earth3, x_acc_earth3, y_acc_earth3 = calculate_orbit(initial_r3, dicc_earth['day0coord'], calculate_acceleration(initial_r3), earth1y)

picture_planet_track(x_earth3, y_earth3, "Earth", "EarthOrbit_HalfVel.jpg")

# Exercise 11: normal trajectory with acceleration vector (video)
trajectory_plus_acc_video(x_earth,
                          y_earth,
                          x_acc_earth,
                          y_acc_earth,
                          'Normal orbit with acceleration')

"""

plt.close('all')

# Show picture of first four planets

def planetary_orbit(x_coord, y_coord, day, planet_dicc):
    # trajectory plot
    plt.plot(x_coord[0:planet_dicc['period in days']],
             y_coord[0:planet_dicc['period in days']],
             color=planet_dicc['color'], linewidth=0.5)
    # planet marker
    plt.plot(x_coord[day-1], y_coord[day-1],
             marker='o',
             markeredgecolor="white",
             markeredgewidth=0.5,
             color=planet_dicc['color'],
             ms=planet_dicc['relative size'],
             label=planet_dicc['name'])


show_day = 1
plt.clf()
plt.close('all')

fig_system = plt.figure(figsize=[15,15], dpi=200, edgecolor=None, tight_layout=True)

planetary_orbit(x_mercury, y_mercury, show_day, dicc_mercury)
planetary_orbit(x_venus, y_venus, show_day, dicc_venus)
planetary_orbit(x_earth, y_earth, show_day, dicc_earth)
planetary_orbit(x_mars, y_mars, show_day, dicc_mars)
planetary_orbit(x_jupyter, y_jupyter, show_day, dicc_jupyter)
planetary_orbit(x_saturn, y_saturn, show_day, dicc_saturn)
planetary_orbit(x_uranus, y_uranus, show_day, dicc_uranus)
planetary_orbit(x_neptune, y_neptune, show_day, dicc_neptune)

# generate Sun's position in the graph. ’yo ’ means a yellow dot, ms indicates its size
plt.plot(r_sun[0], r_sun[1], 'yo', ms=std_size)
plt.legend(loc='upper left', markerscale=0.1, title='Sol System',
           facecolor='midnightblue', edgecolor='darkmagenta', framealpha=1)
plt.axis("off")
plt.show()
fig_system.savefig(fname='SolSystem.jpg', dpi=200)
plt.close(fig_system)
