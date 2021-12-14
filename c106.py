import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    icecream=[]
    temperature=[]
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            icecream.append(float(row["Ice-cream Sales"]))
            temperature.append(float(row["Temperature"]))

    return{"y":icecream,"x":temperature}


def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between icecream sale and temp is :-",correlation[0,1])

def setup():
    data_path="icecreamdata.csv"  
    datasource=getDataSource(data_path)
    findCorrelation(datasource)  



setup()