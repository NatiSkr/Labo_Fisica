*Activity #4 'Órbitas'* from the virtual course of "Mecanica y Termodinamica", Departamento de Fisica, Facultad de Ciencias Exactas y Naturales, Universidad de Buenos Aires.

Guide available in pdf format (Spanish only). The practice's objective was to simulate a planetary orbit in two dimensions both as a picture and as an animation.

Original format: Jupyter notebook .ipynb

**Packages needed**
- numpy
- matplotlib
- imageio
- alive_progress

*Planet's coordinates* taken from NASA'S webpage at https://ssd.jpl.nasa.gov/horizons.cgi with the following settings:

- Ephemeris Type: VECTORS
- Target Body: choose from list
- Coordinate Origin: Solar System Barycenter (SSB)
- Time Span: two continuos day (Step = 1d), where Start = day0 and Stop = day1

At results check the vector's X and Y dimensions of each day. Remember they are on astronomical units.

The resulting objects with the trajectory won't start at day0 buy at day1. Nevertheless day0 is needed for computation


**Fixed problems**

- Video scale becomes dinamic when adding an acceleration vector

- Singular images of a planet now have better resolution


**Unsolved problems**

- Returned and saved figure given by make_system_pic mantain resolution. However when implemented in make_system_video they get re-sized to giving errors:

IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (2979, 2979) to (2992, 2992) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).

[swscaler @ 000002847d4d0000] Warning: data is not aligned! This can lead to a speed loss

- Orbits needed by make_system_video are remade at each pass when I only wish the position to change. A possible solution would be to save each orbit separately as an object

- Making the System animation may consume too many resources (related to previous issues)
