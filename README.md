# Clock Project: Static & Animated Analog Clocks (Python Closures)

## Description: 

This project showcases the implementation of two analog clocks in Python using closures: a static clock displaying the current time and an animated clock that updates in real-time. Both clocks utilize trigonometric calculations and matplotlib visualization to accurately represent the positions of the hour, minute, and second hands.

## Files:

analogueClock.py: Implements the static analog clock.

dynamicClock.py: Implements the animated analog clock.

## Packages Used
* numpy: Handles calculations like trigonometry for hand positions and arrays for plotting.
* matplotlib: Visualizes the clock face, hands, and labels with customizable colors, sizes, and styles.
* datetime: Retrieves the current system time for both static and animated clocks, ensuring accurate hand positions.
## Key Features:

* Closures: Both files leverage closures to encapsulate the logic for calculating the hand positions based on the hand length and current angle. This promotes modularity and reusability.
* Matplotlib: The project uses matplotlib to create the clock face, hands, and labels.
* Real-time animation: The animated clock continuously updates the hand positions based on the system time, providing a dynamic representation of the current time.

## How to Run:

Save both analogueClock.py and dynamicClock.py in the same directory.
To run the static clock, open a terminal in the directory and execute python analogueClock.py. A static clock image will be generated as analogueClock.png.
To run the animated clock, execute python dynamicClock.py in the terminal. The clock will run continuously, updating the hand positions every second.

