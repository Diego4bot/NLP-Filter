import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Create a Tkinter window
root = tk.Tk()
root.title("Robot Player")

# Create a Matplotlib figure and axes
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Define the initial position and size of the first bar
bar_height = 0.9
bar_left = 2
bar_width = 2

# Create the first horizontal bar
bar = ax.barh(1, bar_width, height=bar_height, left=bar_left, align='edge')
bars = [bar]
dragging = [False]

# Define the allowed y-axis values where bars can be drawn
allowed_y_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Set the y-axis ticks to match the allowed y-axis values
ax.set_yticks(allowed_y_values)
# Function to handle the mouse click event
def on_click(event):
    if event.button == 1:
        # Get the x and y coordinates of the mouse click event
        x = event.xdata
        y = round(event.ydata)

        # Check if the y position of the new bar is within the allowed y-axis values
        if y not in allowed_y_values:
            return

        # Create a new horizontal bar
        new_bar = ax.barh(y, bar_width, height=bar_height, left=x, align='edge')
        bars.append(new_bar)
        dragging.append(True)

# Function to update the position and width of the bar during dragging
def on_motion(event):
    for i, bar in enumerate(bars):
        if dragging[i]:
            # Calculate the new width of the bar
            new_width = bar[0].get_width() + (bar[0].get_x() - event.xdata)

            # Update the position and width of the bar
            bar[0].set_width(new_width)
            bar[0].set_x(event.xdata)

            # Redraw the figure
            canvas.draw()

# Function to start dragging when mouse button is pressed
def on_press(event):
    for i, bar in enumerate(bars):
        if bar[0].contains(event)[0]:
            dragging[i] = True

# Function to stop dragging when mouse button is released
def on_release(event):
    for i in range(len(bars)):
        dragging[i] = False

# Connect the mouse click, press, motion, and release events to the corresponding functions
fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('button_release_event', on_release)

# Set the x-axis limits
ax.set_xlim(0, 365)

# Set the y-axis limits
ax.set_ylim(-0.5, 16.5)

# Create a canvas to display the Matplotlib figure in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Create the Matplotlib toolbar
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

# Pack the canvas and toolbar into the Tkinter window
canvas.get_tk_widget().pack()
toolbar.pack()

# Run the Tkinter main loop
root.mainloop()
