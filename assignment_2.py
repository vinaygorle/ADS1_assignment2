""" Importing libraries"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

""" Reading data set  """
 
data = pd.read_csv('london_weather.csv')

""" Using head we take first 150 data values"""

print(data.head(150))

"""mean meadian mode of the data set"""

print(data.describe())

""" printing the transpose of the data """

print(data.transpose())

""" Taking first 150 days of data"""

data=data.head(150)

"""# Preprocessing for date and month """

data['date'] = pd.to_datetime(data['date'], format = '%Y%m%d')

""""line graph for Temperature Variation """
#using a function to call variables for line plot
def Lineplot(dt, max_t, mean, min_t, heading):
    """line plots for london 150 days and the temperature by taking parameters
    dt = date we take first 150 days in the data sheet
    max_t = Maximum temperature in london data
    mean = mean temperature in the taken data
    min_t = minimum temperature in data sheet
    """
    plt.figure(figsize = (12, 6))
    #line pot for maximum temperature with 150 days data
    plt.plot(data[dt], data[max_t], label = max_t)
    #line pot for mean temperature with 150 days data
    plt.plot(data[dt], data[mean], label = mean)
    #line pot for minimum temperature with 150 days data
    plt.plot(data[dt], data[min_t], label = min_t)
    #Adding labels for the plot
    plt.title(heading)
    plt.xlabel('date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.show()

"""# Histogram for Precipitation"""
#using a function to call
def Histogram(precip, heading):
    """Histogram plot for precipition
    by taking precipition data from data file """
    plt.figure(figsize = (8, 6))
    # syntax for histogram plot
    sns.histplot(data[precip], bins = 30, kde = True)
    #Adding lables for plots
    plt.title(heading)
    plt.xlabel('Precipitation')
    plt.ylabel('Frequency')
    plt.show()

"""# scatter plot between Global Radiation and  Max Temperature"""
#using a function to call
def Scatterplot(radiation, max_t, heading):
    """scatterplot betweeen radiation and maximum temperature 
    by taking datas from data file 
    x-axis = radiation
    y-axix = maximum temperature"""
    plt.figure(figsize = (8, 6))
    #syntax for scatterplot taking radion and maximum temperature data
    sns.scatterplot(x = data[radiation], y = data[max_t])
    #Adding lables for plots
    plt.title(heading)
    plt.xlabel('Global Radiation')
    plt.ylabel('Maximum Temperature')
    plt.show()
    
    
"""# Pressure Variation by Month""" 
#using a function to call
def violinplot(mon, date, press, heading):
    """violiplot for the pressure variation by month
    mon = month from the data file
    date = date coloum from the data
    pess = pressure in the climate"""
    data[mon] = data[date].dt.month
    #syntax for the plot
    plt.figure(figsize = (10, 6))
    sns.violinplot(x = mon, y = press, data = data)
    #Adding lables for plots
    plt.title(heading)
    plt.xlabel('Month')
    plt.ylabel('Pressure')
    plt.show()
    
    
"""Heatmap for the complete data"""
#using a function to call       
def Heatmap(heading):
    """Heatmap for the first 150 climate data"""
    plt.figure(figsize = (10, 8))
    #syntax for heatmap
    sns.heatmap(data.corr(), annot = True, cmap = 'coolwarm', fmt ='.2f')
    #Adding lables for plots
    plt.title(heading)
    plt.show()

         
"""calling all the variables used in the above functions"""
Lineplot('date', 'max_temp', 'mean_temp', 'min_temp', 'Temperature Variation')
Histogram('precipitation', 'Precipitation Distribution')
Scatterplot('global_radiation', 'max_temp', 'Global Radiation vs Max Temperature')
violinplot('month', 'date', 'pressure', 'Pressure Variation by Month')
Heatmap('Correlation Heatmap')
