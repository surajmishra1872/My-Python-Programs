import numpy as np
from matplotlib import pyplot as plt
####x = np.linspace(0, 2, 100)
##### Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
####fig, ax = plt.subplots() # Create a figure and an axes.
####ax.plot(x, x, label='linear') # Plot some data on the axes.
####ax.plot(x, x**2, label='quadratic') # Plot more data on the axes...
####ax.plot(x, x**3, label='cubic') # ... and some more.
####ax.set_xlabel('x label') # Add an x-label to the axes.
####ax.set_ylabel('y label') # Add a y-label to the axes.
####ax.set_title("Simple Plot") # Add a title to the axes.
####ax.legend() # Add a legend
##def my_plotter(ax, data1, data2):
####    """
####    A helper function to make a graph
####    Parameters
####    ----------
####    ax : Axes
####    The axes to draw to
####    data1 : array
####    The x data
####    data2 : array
####    The y data
####    param_dict : dict
####    Dictionary of kwargs to pass to ax.plot
####    Returns
####    -------
####    out : list
####    list of artists added
####    """
##    out = ax.plot(data1, data2)
##    return out
###which you would then use as:
##data1, data2, data3, data4 = np.random.randn(4, 100)
##fig, ax = plt.subplots(1, 1)
##my_plotter(ax, data1, data2 )
##plt.show()

##import numpy as np
### evenly sampled time at 200ms intervals
##t = np.arange(0., 5., 0.2)
### red dashes, blue squares and green triangles
##plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
##plt.show()
##data = {'a': np.arange(50),
##'c': np.random.randint(0, 50, 50),
##'d': np.random.randn(50)}
##data['b'] = data['a'] + 10 * np.random.randn(50)
##data['d'] = np.abs(data['d']) * 100
##plt.scatter('a', 'b',c='d', s='d', data=data)
##plt.xlabel('entry a')
##plt.ylabel('entry b')
x=[1,2,3]
y=[5,6,7]
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(False)
plt.show()
