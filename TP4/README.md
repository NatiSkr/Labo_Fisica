*Activity #4 'Órbitas'* from the virtual course of "Mecanica y Termodinamica", Departamento de Fisica, Facultad de Ciencias Exactas y Naturales, Universidad de Buenos Aires.

Guide available in pdf format (Spanish only). The practice's objective was to simulate a planetary orbit in two dimensions both as a picture and as an animation.

Original format: Jupyter notebook .ipynb

*Packages needed*
- numpy
- matplotlib
- iamgeio
- alive_progress

*Planet's coordinates* taken from NASA'S webpage at https://ssd.jpl.nasa.gov/horizons.cgi with the following settings:

- Ephemeris Type: VECTORS
- Target Body: choose from list
- Coordinate Origin: Solar System Barycenter (SSB) (also kwown as the Sun)
- Time Span: two continuos day (Step = 1d), where Start = day0 and Stop = day1

At results check the vector's X and Y dimensions of each day. Remember they are on astronomical units.

The resulting objects with the trajectory won't start at day0 buy at day1. Nevertheless day0 is needed for computation


*Fixed problems*

- Video scale becomes dinamic when adding an acceleration vector


*Unsolved problems*

- Singular images of Earth's trajectory have poor resolution and don't use esthetic values given by dicctionary

- Returned and saved figure given by make_system_pic mantain resolution. However when implemented in make_system_video they get re-sized to 3000x3000 giving error and/or distorting the frame.

- Orbits needed by make_system_video are remade at each pass when I only wish the position to change. A possible solution would be to save each orbit separately as an object

- Making the System animation seems to consume too many resources (related to previous issues)
