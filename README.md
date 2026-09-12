# pygame-stick-simulation
Python project simulating falling objects with gravity using Pygame.

## About

This project implements a simple interactive 2D simulation in which a stick falls under the influence of gravity. The program uses pygame to create a graphical window, display objects, process mouse and keyboard events, and manage the game loop. This project was developed as a university coursework project during the second year of university.

## Key Variables

* GRAVITY - gravity acceleration used for falling objects;
* screen - Pygame display surface;
* screen_width - width of the application window;
* screen_height - height of the application window;
* clock - object used to control the frame rate;
* running - flag controlling the main program loop;
* sticks - Pygame sprite group containing the falling sticks;
* pos_y - current vertical position of a stick;
* speed_y - current vertical speed of a stick;
* toolbar_color - toolbar background color;
* toolbar_height - height of the toolbar;
* toolbar_font - font used for toolbar text;
* btn_width - width of toolbar buttons;
* btn_height - height of toolbar buttons;
* btn_file - File button area;
* btn_save - Save button area;
* btn_open - Open button area;
* btn_help - Help button area.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/dolzhkris/pygame-stick-simulation.git
```

2. Install the required dependency:

```bash
pip install -r requirements.txt
```

3. Run the program with:

```bash
python main.py
```
