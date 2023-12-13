# Clock Project: Static & Animated Analog Clocks (Python Closures)

## Description: 

This project showcases the implementation of two analog clocks in Python using closures: a static clock displaying the current time and an animated clock that updates in real-time. Both clocks utilize trigonometric calculations and matplotlib visualization to accurately represent the positions of the hour, minute, and second hands.

## Files:

analogClock.py: Implements the static analog clock.

dynamicClock.py: Implements the animated analog clock.
## Key Features:

Closures: Both files leverage closures to encapsulate the logic for calculating the hand positions based on the hand length and current angle. This promotes modularity and reusability.
Matplotlib: The project uses matplotlib to create the clock face, hands, and labels.
Real-time animation: The animated clock continuously updates the hand positions based on the system time, providing a dynamic representation of the current time.

## How to Run:

Save both analogClock.py and dynamicClock.py in the same directory.
To run the static clock, open a terminal in the directory and execute python P5a.py. A static clock image will be generated as analogClock.png.
To run the animated clock, execute python dynamicClock.py in the terminal. The clock will run continuously, updating the hand positions every second.

## Further Exploration:

Modify the hand lengths and clock face size to customize the appearance of the clocks.
Experiment with different closure implementations for the hand calculations.
Add additional features like alarm functionality or different clock styles.
