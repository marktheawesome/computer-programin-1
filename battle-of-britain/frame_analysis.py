'''
This will enabed me to do more math after wards.
'''
# imports
import os
import matplotlib.pyplot as plt
import numpy as np
import settings

# variables
all_frames = []
currentFile = None


def make_file():
    '''
    Writes a new file called sevens.txt which contains only
    letters that are exactly seven letters long.
    '''
    global currentFile, new_folder

    os.chdir('./assets/Stats')
    fileNames = []

    for filename in os.listdir('.'):
        fileNames.append(filename)
    new_folder = "Frame_rates_" + str((len(fileNames) + 1))
    os.mkdir(new_folder)
    os.chdir('./' + str(new_folder))

    currentFile = "Frame_rates_" + str((len(fileNames) + 1)) + ".txt"
    with open(currentFile, "a") as f:
        for word in settings.FRAME_RATE:
            f.write(str(word) + "\n")

    os.chdir("..")
    os.chdir("..")
    os.chdir("..")


def analyst():
    '''
    This will do the analyst.
    '''
    global all_frames, new_folder

    os.chdir('./assets/Stats/' + str(new_folder))

    with open(currentFile, "r") as f:
        for number in f:
            number = number.replace("\n", '')
            number = int(number)
            if number != 0:
                all_frames.append(number)
    average = np.average(all_frames)
    median = np.median(all_frames)
    min_ = np.min(all_frames)
    max_ = np.max(all_frames)

    print(average, median, min_, max_)

    os.chdir("..")
    os.chdir("..")
    os.chdir("..")

def graph():
    '''
    Shows graph of the frame rate/
    '''
    global all_frames, new_folder

    tenth_frame = []
    for index in range(len(all_frames)):
        if index % 10 == 0:
            tenth_frame.append(all_frames[index])


    plt.plot(tenth_frame, 'go', label='points', linewidth=.1)
    plt.plot(tenth_frame, 'b-', label='line', linewidth=.1)

    plt.title('Fram Rate Over Time')
    plt.ylabel('Frame Rate')
    plt.xlabel('Frame Number')
    os.chdir("./assets/Stats/" + str(new_folder))
    plt.savefig(str(currentFile[0:-4]))
    plt.show()
