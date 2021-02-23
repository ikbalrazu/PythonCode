import pandas
import matplotlib.pyplot as plt


#DataFrame
mydataset = {
    "cars": ["BMW","TOYOTA","HYNDAI","TESLA","NISSAN"],
    "selles": [5000,2000,1500,1000,500]
}

myframe = pandas.DataFrame(mydataset)
print(myframe)

studata_set = {
    "Student Name": ["iqbal","arif","shafiur","rokibul","mokki"],
    "id": [1703,1632,1629,1631,1666]
}

stutable = pandas.DataFrame(studata_set,index=[1,2,3,4,5])
print(stutable)
print(stutable.loc[1])

#series
calories = {"day1":420,"day2":520,"day3":321}
seriesdata = pandas.Series(calories, index=["day1"])
print(seriesdata)

#read CSV

readcsv = pandas.read_csv("E:\Django-Works\csvdatafile.csv")
readjson_data = pandas.read_json("E:\Django-Works\jsondata.json")
print(readcsv)
#print(readjson_data.to_string())
print(readjson_data.head(10))
print(readjson_data.tail())
print(readjson_data.info())
print(readcsv.info())

#matplotlib
#readcsv.plot()
readjson_data.plot()
plt.show()

