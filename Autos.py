import pandas as pd
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
df = pd.read_csv(url, header = None)
df.columns= headers

# replace Nan for true
df.replace("?", np.nan, inplace = True)

avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)

df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

#print("Average peak rpm:", avg_peakrpm)

missing_data = df.isnull()

#describe data type numeric and "all" its used to obtain the statistic
#print(df.describe(include='all'))

# get type of data 
print(df.dtypes)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    missing_data.head(5)
    print("") 
    missing_data = df.isnull()
    missing_data.head(5)

    avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
   # print("Average of normalized-losses:", avg_norm_loss)

    df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

#export data to .csv
#path = ".\Automovile.csv"
#df.to_csv(path)


#convert data types to proper format 

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")


plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")