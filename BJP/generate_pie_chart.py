import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import csv

## open up your csv file with the sentiment results
with open('graph_bjp.csv', 'r') as csvfile:


    df = pd.read_csv(csvfile)
    sent = df["Sentiment"]

## use Counter to count how many times each sentiment appears
## and save each as a variable
    counter = Counter(sent)
    positive = counter['positive']
    print "postive -->", positive
    negative = counter['negative']
    print "negative -->",negative

    pos_perce= positive*100.00/(positive+negative)
    neg_perce = negative * 100.00 / (positive+negative)
    print "Positive For party -->",pos_perce,'%'
    print "Negative For party -->", neg_perce,'%'



labels = 'Positive', 'Negative'
sizes = [positive, negative]
colors = ['green', 'red']
yourtext = "Your Search Query from Step 2"

## use matplotlib to plot the chart
plt.pie(sizes, labels = labels, colors = colors, shadow = True, startangle = 90)
plt.title("Sentiment of Tweets about CNG")
plt.show()

