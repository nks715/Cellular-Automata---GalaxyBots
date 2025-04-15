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
def reproduction():
    for ind, row in enumerate(matrix):
        for index, cell in enumerate(row):
            global count
            count = 0
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
            if count == 3:
                dbg_print("Worked")#, 1)
                matrix[ind][index] = 1
            #print(ind, index)
    image.set_data(matrix)
    plt.draw()
timer = fig.canvas.new_timer(interval=1000)
timer.add_callback(reproduction)
timer.start()
cid = fig.canvas.mpl_connect('button_press_event', onpress)
plt.show()