'''
This will enabed me to do more math after wards.
'''
# pylint: disable=import-error
# imports
import os
import matplotlib.pyplot as plt
import numpy as np
import settings
from pandas import DataFrame

# variables
ALL_FRAMES = []
CURRENT_FILE = None
NEW_FOLDER = None

def make_file():
    '''
    Writes a new file called sevens.txt which contains only
    letters that are exactly seven letters long.
    '''
    global CURRENT_FILE, NEW_FOLDER

    os.chdir('./assets/Stats')
    file_names = []

    for filename in os.listdir('.'):
        file_names.append(filename)
    NEW_FOLDER = "Frame_rates_" + str((len(file_names) + 1))
    os.mkdir(NEW_FOLDER)
    os.chdir('./' + str(NEW_FOLDER))

    CURRENT_FILE = "Frame_rates_" + str((len(file_names) + 1)) + ".txt"
    with open(CURRENT_FILE, "a") as _f:
        for word in settings.FRAME_RATE:
            _f.write(str(word) + "\n")

    os.chdir("..")
    os.chdir("..")
    os.chdir("..")


def analyst():
    '''
    This will do the analyst.
    '''
    global ALL_FRAMES, NEW_FOLDER

    os.chdir('./assets/Stats/' + str(NEW_FOLDER))

    with open(CURRENT_FILE, "r") as _f:
        for number in _f:
            number = number.replace("\n", '')
            number = int(number)
            if number != 0:
                ALL_FRAMES.append(number)
    average = np.average(ALL_FRAMES)
    median = np.median(ALL_FRAMES)
    min_ = np.min(ALL_FRAMES)
    max_ = np.max(ALL_FRAMES)

    os.chdir("..")
    os.chdir("..")
    os.chdir("..")

    return average, median, min_, max_


def graph():
    '''
    Shows graph of the frame rate/
    '''
    global ALL_FRAMES, NEW_FOLDER

    tenth_frame = []
    for index in range(0, len(ALL_FRAMES), 10):
        index10 = index+10
        ten_digets = ALL_FRAMES[index:index10]
        avg = np.average(ten_digets)
        tenth_frame.append(avg)


    plt.plot(tenth_frame, 'go', label='points', linewidth=.1)
    plt.plot(tenth_frame, 'b-', label='line', linewidth=.1)

    plt.title('Frame Rate Over Time')
    plt.ylabel('Frame Rate')
    plt.xlabel('Frame Number')
    os.chdir("./assets/Stats/" + str(NEW_FOLDER))
    plt.savefig(str(CURRENT_FILE[0:-4]))
    plt.show()


def tabel(stats):
    '''
    Table of stats.
    '''
    average = stats[0]
    median = stats[1]
    min_ = stats[2]
    max_ = stats[3]
    table_contents = {'header':['average', 'median', 'min', 'max'],
                      'number':[np.ceil(average), int(median), int(min_), int(max_)]
                     }
    d_f = DataFrame(table_contents, columns=['header', 'number'])
    print(d_f)
