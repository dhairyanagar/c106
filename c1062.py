import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    coffee =[]
    sleep=[]
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return{"y":coffee,"x":sleep}


def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between icecream sale and temp is :-",correlation[0,1])

def setup():
    data_path="coffeedata.csv"  
    datasource=getDataSource(data_path)
    findCorrelation(datasource)  



setup()