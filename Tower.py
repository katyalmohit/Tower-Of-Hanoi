import tkinter as tk
from tkinter import messagebox
import turtle

screen = turtle.Screen()
screen.setup(width=1200, height=600)
screen.title("Tower Of Hanoi")
screen.bgcolor("white")
# Create move count turtle
move_count_turtle = turtle.Turtle()
move_count_turtle.hideturtle() 
move_count_turtle.penup()
move_count_turtle.goto(0,250)
move_count_turtle.write("Move Count: 0", align="center", font=("consolas", 16, "bold"))

# Create three stacks as lists
stacks = [[], [], []]

# Set up the three towers
def setup_towers():
    tower_width = 10
    tower_height = 450
    tower_spacing = 300

    for i in range(3):
        tower = turtle.Turtle()
        tower.shape("square")
        tower.color("black")
        tower.shapesize(stretch_wid=tower_height/20, stretch_len=tower_width/20)
        tower.penup()
        tower.goto((i - 1) * tower_spacing, 0)
        tower.pendown()
        stacks[i].append(tower)

# Create and initialize move count
move_count = 0

# Create and initialize disks on the first tower
def setup_disks(num_disks):
    disk_width = 100
    disk_height = 10
    disk_spacing = 20

    for i in range(num_disks):
        disk = turtle.Turtle()
        disk.shape("square")
        disk.color("blue")
        disk.shapesize(stretch_wid=disk_height/20, stretch_len=(num_disks - i) * disk_width/40)
        disk.penup()
        disk.goto(-((num_disks - i) * disk_width)/2, (i - num_disks/2) * disk_spacing - 200)
        disk.pendown()
        stacks[0].append(disk)

# Move disk from one tower to another
def move_disk(from_tower, to_tower):
    global move_count
    disk = stacks[from_tower].pop()
    disk.penup()
    disk.goto((to_tower - 1) * 300, len(stacks[to_tower]) * 15 - 200)
    disk.pendown()
    stacks[to_tower].append(disk)
    move_count += 1
    move_count_turtle.clear()
    move_count_turtle.write(f"Move Count: {move_count}", align="center", font=("consolas", 16, "bold"))

# Solve the Tower of Hanoi recursively
def solve_hanoi(n, from_tower, to_tower, aux_tower):
    if n > 0:
        solve_hanoi(n-1, from_tower, aux_tower, to_tower)
        move_disk(from_tower, to_tower)
        solve_hanoi(n-1, aux_tower, to_tower, from_tower)

# Function to handle the solve button click
def solve_button_click():
    global move_count
    num_disks = int(entry.get())
    if num_disks <= 0:
        messagebox.showerror("Invalid Input", "Number of disks must be a positive integer.")
    else:
        window.withdraw()
        setup_towers()
        setup_disks(num_disks)
        solve_hanoi(num_disks, 0, 2, 1)
        messagebox.showinfo("Tower of Hanoi", f"Solved in {2**num_disks - 1} moves.")
        screen.clear()
        screen.bye()  # Close the turtle graphics window
        window.destroy()  # Destroy the "Enter Number of Disks" window
        

# Create the main GUI window
window = tk.Tk()
window.title("Enter Number of Disks")
window.geometry("300x200")

# Create and configure the label and entry for number of disks
label = tk.Label(window, text="Enter the number of disks:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Create and configure the solve button
solve_button = tk.Button(window, text="Solve", command=solve_button_click)
solve_button.pack()

# Run the main GUI loop
window.mainloop()
