import keyboard
import matplotlib.pyplot as plt
import numpy as np
import keyboard as slsf
def dbg_print(msg, dlevel=0):
    if dlevel > 0:
        print(msg)
matrix = np.zeros((10, 10))

fig, ax = plt.subplots()
image = ax.imshow(matrix, cmap="gray", vmin=0, vmax=1)

paused = False

# Function to toggle cell on click
def onpress(event):
    try:
        x = int(event.xdata)
        y = int(event.ydata)
        matrix[y][x] = 1 - matrix[y][x]  # Toggle between 0 and 1
        image.set_data(matrix)
        plt.draw()
    except TypeError:
        print("Outside axes!")
def pausing(event):
    if slsf.is_pressed("space"):
        global paused
        paused = not paused
        print(paused)
def four_rules():
    if paused == False:
        matrix_temp = matrix.copy()
        for ind, row in enumerate(matrix_temp):
            #Iterating through every cell
            for index, cell in enumerate(row):
                global count
                count = 0
                #Checking the amount of alive neighbors
                #print(ind, index)
                if ind-1 >=0:
                    if matrix_temp[ind-1][index] == 1:
                        count +=1
                #print(ind, index)
                if ind+1<=9:
                    if matrix_temp[ind+1][index] == 1:
                        count +=1
                #print(ind, index)
                if index+1 <=9:
                    if matrix_temp[ind][index+1] == 1:
                        count +=1
                #print(ind, index)
                if index-1 >=0:
                    if matrix_temp[ind][index-1] == 1:
                        count +=1
                #print(ind, index)
                #Reproduction
                if count == 3 and matrix_temp[ind][index] != 1:
                    dbg_print("Reproduction" + str(ind) + str(index), 1)
                    matrix[ind][index] = 1
                #Overpopulation
                if count == 4 and matrix_temp[ind][index] != 0:
                    dbg_print("Overpopulation" + str(ind) + str(index), 1)
                    matrix[ind][index] = 0
                #Underpopulation
                if count < 2 and matrix_temp[ind][index] != 0:
                    dbg_print("Underpopulation" + str(ind) + str(index), 1)
                    matrix[ind][index] = 0
                #print(ind, index)
    image.set_data(matrix)
    plt.draw()
timer = fig.canvas.new_timer(interval=125)
timer.add_callback(four_rules)
timer.start()
cid = fig.canvas.mpl_connect("button_press_event", onpress)
cid = fig.canvas.mpl_connect("key_press_event", pausing)
plt.show()