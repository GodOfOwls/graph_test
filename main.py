# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import plotly.express as px
import pandas
import psutil
import requests
import kaleido

def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    data_y = [1, 2, 3, 6, 5, 8, 9, 6, 7, 156, 8, 10]
    data_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    fig = px.line(x=data_x, y=data_y)
    #fig.show()
    import os
    if not os.path.exists("images"):
        os.mkdir("images")
    fig.write_image("images/fig1.png", engine='kaleido')


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
