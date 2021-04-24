import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv

df = pd.read_csv("data.csv")
# fig = ff.create_distplot([df["temp"].tolist()], ["Average Temperature"], show_hist = False)
# fig.show()

data = df["temp"].tolist()

mean = statistics.mean(df["temp"])
std_dev = statistics.stdev(df["temp"])

# print(f"The mean of the average temperatures is: {mean:.2f}")
# print(f"The standard deviation of the average temperatueres is: {std_dev:.2f}")

sample_data = []
sample_deviation = []
k = 0

def showfig(meanlist):
    df = meanlist
    fig = ff.create_distplot([df], ["Temp"], show_hist = False)
    mean = statistics.mean(meanlist)
    std_dev = statistics.stdev(meanlist)
    print(f"The mean of the standard deviations is: {mean:.2f}")
    print(f"The standard deviation of the standard deviations is: {std_dev:.2f}")
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "Mean"))
    # fig.add_trace(go.Scatter(x = [std_dev, mean], y = [0, 1], mode = "lines", name = "Mean"))
    fig.show()

def randomsetofmean(counter):
    ds = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        ds.append(value)
    mean = statistics.mean(ds)
    return mean
    
def setup():
    meanlist = []
    for i in range(0, 1000):
        setofmeans = randomsetofmean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)

setup()

for i in range(0, 100):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        sample_data.append(value)
    
# fig = ff.create_distplot([sample_deviation], ["Standard Deviation of Sample"], show_hist = False)
# fig.show()

std_dev_sample = statistics.stdev(sample_data)
mean_sample = statistics.mean(sample_data)

print(f"The mean of the sample data is: {mean:.2f}")
print(f"The standard deviation of the sample data is: {std_dev_sample:.2f}")