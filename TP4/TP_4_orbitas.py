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
from alive_progress import alive_bar
plt.style.use('dark_background')

""" Use of scipy library (https://docs.scipy.org/doc/scipy/reference/constants.html)
Is restricted due to possible overlapping of variables. """

" Declaration of global variables"
AU = 149597870700  # astronomical units au in meters
universal_G = 6.67 * 10 ** -11  # Gravitational constants. Units: N*m^2/kg^2
M_Sun = 1988500 * 10 ** 24  # Sun's mass, units=kg
r_sun = [0, 0]  # Sun's position: we consider it a fixed constant (approximation, see Solar System Barycenter)
earth1y = 375  # Simulated Earth's Days
std_size = 2  # earth size for plots
sun_size = std_size  # size relative to earth for plots, should be *109 but *1 is used instead for visualization
# planetary sizes will be relative to earth


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


def calculate_orbit(planet_dicc, tag, days):
    # Assign variables in local scope
    r_anterior = planet_dicc["day0coord"+tag]
    r_actual = planet_dicc["day1coord"+tag]
    actual_acc = calculate_acceleration(r_actual)
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
    planet_dicc["x_coord" + tag] = rx_list
    planet_dicc["y_coord" + tag] = ry_list
    planet_dicc["x_acc" + tag] = acc_x_list
    planet_dicc["y_acc" + tag] = acc_y_list
    return


""" Exercise 5
Graph: trajectory in (x,y) plane """


def picture_planet_track(planet_dicc, last_day, filename):
    plt.clf()
    # check that lists with coordinates have the same size
    if len(planet_dicc["x_coord"]) == len(planet_dicc["x_coord"]):
        plt.plot(planet_dicc["x_coord"][0:last_day-1],
                 planet_dicc["y_coord"][0:last_day-1],
                 color='grey')
        # generate Sun's position in the graph. ’yo ’ means a yellow dot, ms indicates its size
        plt.plot(r_sun[0], r_sun[1], 'yo', ms=sun_size)
        plt.title(planet_dicc["name"]+"'s trajectory")
        plt.xlabel('x coordinates (meters)')
        plt.ylabel('y coordinates (meters)')
        plt.savefig(filename, dpi=200)
        print("\n Plot saved as "+filename)
        # plt.show()
    else:
        print('Error: There is a discrepancy between the number of days and the quantity of coordinates')


""" Exercise 6
Graph: acceleration as a function of time (measured in days)
Later generate an animated video of the translational movement. We wil need to handle the images that compose it. """


def picture_planet_ACCvsTIME(x_or_y, planet_dicc, tag, filename):
    plt.clf()
    plt.plot(planet_dicc[x_or_y + "_coord"+tag][0:earth1y-1], color='cyan')
    plt.title(planet_dicc["name"]+ "'s acceleration on "+x_or_y+" axis")
    plt.xlabel('Days')
    plt.ylabel('Acceleration (meters/seconds^2)')
    plt.savefig(filename, dpi=200)
    print("\n Plot saved as " + filename)
    # plt.show()


""" Exercise 7
Elaborate a function that receives positions and a day and makes a graphic of the planet's trajectory
and pictures the Sun a a reference and the planet's positions as a small circle."""


def make_orbit_picture(planet_dicc, tag, dia):
    list_x = planet_dicc["x_coord" + tag]
    list_y = planet_dicc["y_coord" + tag]
    # generate a trajectory graph (x,y)
    orbit1y = planet_dicc["period in days"]+1
    plt.plot(list_x[0:orbit1y],
             list_y[0:orbit1y],
             'grey')
    plt.title("Earth's orbit around the Sun. Day: " + str(dia))
    plt.xlabel('x coordinates (meters)')
    plt.ylabel('y coordinates (meters)')

    # generate Sun's position in the graph. ’yo ’ means a yellow dot, ms indicates its size
    plt.plot(r_sun[0], r_sun[1], 'yo', ms=sun_size)

    # planet marker
    plt.plot(list_x[dia], list_y[dia],
             marker='o',
             markeredgecolor="white",
             markeredgewidth=0.5,
             color=planet_dicc['color'],
             ms=planet_dicc['relative size'],
             label=planet_dicc['name'])

    # plt.show()  # remove comment to show plot
    return


""" Exercise 8
Make a function that generates and saves an animation with imageio, following the library's webpage suggestions
"""


def make_orbit_video(planet_dicc, tag, last_day, name_of_video):
    list_x = planet_dicc["x_coord" + tag]
    list_y = planet_dicc["y_coord" + tag]
    print('\n Preparing video, please wait ...')
    photos_list = []  # list with saves images
    for i in range(last_day):
        # clear the figure as precaution
        plt.clf()
        if i % 2 == 0:  # Save one out of two images
            make_orbit_picture(planet_dicc, tag, i)
            plt.savefig(name_of_video + '.png', dpi=200)
            photos_list.append(imageio.imread(name_of_video + '.png'))
        # Verification test to corroborate saving
        # print (str(i) + ' out of ' +str(len( list_x ) ) + ' saves images')
    imageio.mimsave(name_of_video + '.mp4', photos_list)  # create video
    print('\n Video saved as ' + name_of_video + '.mp4')


""" Exercise 9
How would Earth's trajectory change if it moved twice as fast?
Hint: to reflect this modification, me must double the value of list_y[1] and calculate it all over again
Answer: initially we would have a circular orbit but then it follows a somewhat linear trajectory
Remember that previously in the code list_y[1] = earth['day1coord'][1]
"""


""" Exercise 10 What if instead Earth went half as fast? Should a day be shorter?
Answer: now the Earth moves too close or too far from the Sun
"""


""" Exercise 11
Modify the functions 'make_orbit_picture' and 'make_orbit_video' so they can receive acceleration's lists
Add them to the images.
The matplotlib function (x1,y1,x2,y2) may be useful, where 1 is the origin and 2 the destination of the vector.
"""


def trajectory_plus_acc_picture(planet_dicc, tag, dia):
    # local variables
    list_x = planet_dicc["x_coord" + tag]
    list_y = planet_dicc["y_coord" + tag]
    acceleration_x = planet_dicc["x_acc" + tag]
    acceleration_y = planet_dicc["y_acc" + tag]

    # clear the plotted figure
    plt.clf()

    # display trajectory
    orbit1y = planet_dicc["period in days"]+1
    plt.plot(list_x[0:orbit1y],
             list_y[0:orbit1y],
             'grey')
    plt.title("Earth's trajectory around the Sun. Day: " + str(dia))

    # display Sun's position
    plt.plot(r_sun[0], r_sun[1], 'yo', ms=sun_size)

    # display acceleration vector
    plt.arrow(list_x[dia], list_y[dia],
              acceleration_x[dia+1] * 10 ** 12.5,
              acceleration_y[dia+1] * 10 ** 12.5,
              width=10 ** 9.5,
              color='green')

    # display Earth's position as a marker
    plt.plot(list_x[dia], list_y[dia],
             marker='o',
             markeredgecolor="white",
             markeredgewidth=0.5,
             color=planet_dicc['color'],
             ms=planet_dicc['relative size'],
             label=planet_dicc['name'])
    return


def trajectory_plus_acc_video(planet_dicc, tag, days, name_of_video):
    # local variables
    list_x = planet_dicc["x_coord" + tag]
    list_y = planet_dicc["y_coord" + tag]
    acceleration_x = planet_dicc["x_acc" + tag]
    acceleration_y = planet_dicc["y_acc" + tag]

    print('\n Preparing video, please wait ...')
    photos_list = []  # save images in a list
    for i in range(days):
        if i % 2 == 0:  # save one out of two pictures
            trajectory_plus_acc_picture(planet_dicc, tag, i)
            plt.savefig(name_of_video + '.png', dpi=200)
            photos_list.append(imageio.imread(name_of_video + '.png'))
        # print (str(i) + ' out of ' +str(len( list_x ) ) + 'saves pictures') # test saving
    imageio.mimsave(name_of_video + '.mp4', photos_list)  # create video
    print('\n Video saved as ' + name_of_video + '.mp4')


" --- Mercury's data ------------------"
mercury = {'name': 'Mercury',
           'color': 'chocolate',
           'relative size': std_size*0.3,
           'period in days': int(0.25 * earth1y),
           'day0coord': [3.527194038524470 * (10 ** -1) * AU, -3.992007990089807 * (10 ** -2) * AU],
           'day1coord': [3.496966842279213 * (10 ** -1) * AU, -1.064190753450797 * (10 ** -2) * AU]
           }

" --- Venus's trajectory data ------------------"
venus = {'name': 'Venus',
         'color': 'sandybrown',
         'relative size': std_size*0.9,
         'period in days': int(0.7 * earth1y),
         'day0coord': [6.699101302128549 * (10 ** -1) * AU, -2.590495337952708 * (10 ** -1) * AU],
         'day1coord': [6.769025185681680 * (10 ** -1) * AU, -2.402092653508008 * (10 ** -1) * AU]
         }

" --- Earth's trajectory data ------------------"
earth = {'name': 'Earth',
         'color': 'limegreen',
         'relative size': std_size,
         'period in days': int(earth1y),
         'day0coord': [-9.893730268079107 * (10 ** -1) * AU, 1.525312641360373 * (10 ** -1) * AU],
         'day1coord': [-9.920501473347642 * (10 ** -1) * AU, 1.354183249761766 * (10 ** -1) * AU]
         }

" --- Mars's trajectory data ------------------"
mars = {'name': 'Mars',
        'color': 'orangered',
        'relative size': std_size*0.5,
        'period in days': int(1.9 * earth1y),
        'day0coord': [-1.655510318528293 * AU, 1.657061664751504 * (10 ** -1) * AU],
        'day1coord': [-1.656291363095773 * AU, 1.529609327727200 * (10 ** -1) * AU]
        }

" --- Jupyter's trajectory data ------------------"
jupyter = {'name': 'Jupyter',
           'color': 'khaki',
           'relative size': std_size*11,
           'period in days': int(12 * earth1y),
           'day0coord': [2.849574432688381 * AU, -4.234571266057721 * AU],
           'day1coord': [2.855729459244833 * AU, -4.229999656426285 * AU]
           }

" --- Saturn's trajectory data ------------------"
saturn = {'name': 'Saturn',
          'color': 'goldenrod',
          'relative size': std_size*9,
          'period in days': int(29 * earth1y),
          'day0coord': [9.302046396124146 * AU, 1.588305128062075 * AU],
          'day1coord': [9.300809480419099 * AU, 1.593792603601794 * AU]
          }

" --- Uranus's trajectory data ------------------"
uranus = {'name': 'Uranus',
          'color': 'lightskyblue',
          'relative size': std_size*4,
          'period in days': int(84 * earth1y),
          'day0coord': [1.140614787022116 * 10 * AU, -1.618102574730362 * 10 * AU],
          'day1coord': [1.140933328188972 * 10 * AU, -1.617894211828149 * 10 * AU]
          }

" --- Neptune's trajectory data ------------------"
neptune = {'name': 'Neptune',
           'color': 'royalblue',
           'relative size': std_size*3.5,
           'period in days': int(165 * earth1y),
           'day0coord': [1.406373989566836 * 10 * AU, -2.666345412015452 * 10 * AU],
           'day1coord': [1.406649648193033 * 10 * AU, -2.666197143806701 * 10 * AU]
           }

" Calculate Mercury's orbit"
calculate_orbit(mercury, "",
                neptune['period in days'])

" Calculate Venus's orbit"
calculate_orbit(venus, "",
                neptune['period in days'])

" Calculate Earth's orbit"
calculate_orbit(earth, "",
                neptune['period in days'])

" Calculate Mars's orbit"
calculate_orbit(mars, "",
                neptune['period in days'])

" Calculate Jupyter's orbit"
calculate_orbit(jupyter, "",
                neptune['period in days'])

" Calculate Saturn's orbit"
calculate_orbit(saturn, "",
                neptune['period in days'])

" Calculate Uranus's orbit"
calculate_orbit(uranus, "",
                neptune['period in days'])

"Calculate Neptune's orbit"
calculate_orbit(neptune, "",
                neptune['period in days'])


" The following resolves exercises 5 to 11 of assignment --------------------"

# Exercise 5
picture_planet_track(earth, earth1y, "EarthOrbit.jpg")

# Exercise 6
picture_planet_ACCvsTIME("x", earth, "", "Earth_x_acceleration.jpg")

picture_planet_ACCvsTIME("y", earth, "", "Earth_y_acceleration.jpg")

# Exercise 8
make_orbit_video(earth, "", 400, 'Normal translational movement')


# Exercise 9: if Earth moved twice as fast
earth["day0coordfaster"] = earth["day0coord"]
earth["day1coordfaster"] = [earth['day1coord'][0], earth['day1coord'][1] * 2]
calculate_orbit(earth, "faster",
                earth1y)

picture_planet_track(earth, earth1y, "EarthOrbit_TwiceVel.jpg")


# Exercise 10: if Earth moved half as fast
earth["day0coordslower"] = earth["day0coord"]
earth["day1coordslower"] = [earth['day1coord'][0], earth['day1coord'][1] * 0.5]
calculate_orbit(earth, "slower",
                earth1y)

picture_planet_track(earth, earth1y, "EarthOrbit_HalfVel.jpg")

# Exercise 11: normal trajectory with acceleration vector (video)
trajectory_plus_acc_video(earth, "", 400, 'Normal orbit with acceleration')



plt.close('all')


def planetary_orbit(day, planet_dicc):
    # trajectory plot
    last_day = planet_dicc['period in days']
    plt.plot(planet_dicc["x_coord"][0:last_day],
             planet_dicc["y_coord"][0:last_day],
             color=planet_dicc['color'], linewidth=0.5)
    # planet marker
    plt.plot(planet_dicc["x_coord"][day-1], planet_dicc["y_coord"][day-1],
             marker='o',
             markeredgecolor="white",
             markeredgewidth=0.5,
             color=planet_dicc['color'],
             ms=planet_dicc['relative size'],
             label=planet_dicc['name'])


def make_system_pic(show_day, star_system):
    plt.clf()
    plt.close('all')
    figure = plt.figure(figsize=[15, 15], dpi=200, edgecolor=None, tight_layout=True)

    # Plot each planet
    for planet in star_system:
        planetary_orbit(show_day, planet)

    # Plot Sun's position in the graph.
    plt.plot(r_sun[0], r_sun[1], 'yo', ms=sun_size)
    plt.legend(loc='upper left', markerscale=0.1, title='Sol System at day '+str(show_day),
               facecolor='midnightblue', edgecolor='darkmagenta', framealpha=1)
    plt.axis("off")
    return figure


sol_system = mercury, venus, earth, mars, jupyter, saturn, uranus, neptune


sol_figure= make_system_pic(1, sol_system)
plt.show()
sol_figure.savefig(fname='SolSystem.jpg', dpi=200)
plt.close(sol_figure)



def make_system_video(last_day, star_system):
    print('\n Preparing video of star system, please wait ...')
    photos_list = []  # list with saved images
    # clear the figure as precaution
    plt.clf()
    with alive_bar(last_day) as bar:
        for day in range(last_day):
            if day % 10 == 0:  # Save one out of ten images
                system_fig = make_system_pic(day, star_system)
                system_fig.savefig(fname='SystemFrame.png', dpi=system_fig.dpi, bbox_inches='tight')
                photos_list.append(imageio.imread('SystemFrame.png'))
                plt.clf()
                plt.close(system_fig)
            bar()
    #kargs = {'macro_block_size': None}
    imageio.mimwrite('SystemVideo.mp4', photos_list)  # create video
    print('\n Video saved as SystemVideo.mp4')


make_system_video(mars["period in days"], sol_system)

# There's an issue with the size of the frames in the animation
# Also the orbits should be saved as objects instead of being remade at each pass, given the array's size
