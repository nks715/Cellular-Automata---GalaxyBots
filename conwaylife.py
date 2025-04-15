import matplotlib.pyplot as plt
import numpy as np
def dbg_print(msg, dlevel=0):
    if dlevel > 0:
        print(msg)
matrix = np.zeros((10, 10))

fig, ax = plt.subplots()
image = ax.imshow(matrix, cmap="gray", vmin=0, vmax=1)

# Function to toggle cell on click
def onpress(event):
    try:
        x = int(event.xdata)
        y = int(event.ydata)
        matrix[y][x] = 1 - matrix[y][x]  # Toggle between 0 and 1
        image.set_data(matrix)
        plt.draw()
    except(TypeError):
        print("Outside axes!")
def four_rules():

    for ind, row in enumerate(matrix):
        #Iterating through every cell
        for index, cell in enumerate(row):
            global count
            count = 0
            #Checking the amount of alive neighbors
            #print(ind, index)
            if ind-1 >=0:
                if matrix[ind-1][index] == 1:
                    count +=1
            #print(ind, index)
            if ind+1<=9:
                if matrix[ind+1][index] == 1:
                    count +=1
            #print(ind, index)
            if index+1 <=9:
                if matrix[ind][index+1] == 1:
                    count +=1
            #print(ind, index)
            if index-1 >=0:
                if matrix[ind][index-1] == 1:
                    count +=1
            #print(ind, index)
            #Reproduction
            if count == 3 and matrix[ind][index] != 1:
                dbg_print("Reproduction" + str(ind) + str(index), 1)
                matrix[ind][index] = 1
            if count == 4 and matrix[ind][index] != 0:
                dbg_print("Overpopulation" + str(ind) + str(index), 1)
                matrix[ind][index] = 0
            if count < 2 and matrix[ind][index] != 0:
                dbg_print("Underpopulation" + str(ind) + str(index), 1)
                matrix[ind][index] = 0
            #print(ind, index)
    image.set_data(matrix)
    plt.draw()
timer = fig.canvas.new_timer(interval=10000)
timer.add_callback(four_rules)
timer.start()
cid = fig.canvas.mpl_connect('button_press_event', onpress)
plt.show()