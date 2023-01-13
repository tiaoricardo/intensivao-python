from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score as r2
import pandas as pd
import seaborn as sns

df = pd.read_csv('input/aula4/advertising.csv')

corr = df.corr()

print(corr)

#sns.heatmap(corr, cmap='Blues', annot=True)

y = df["Vendas"]
x = df[["TV", "Jornal", "Radio"]]

train_x, test_x, train_y, test_y = tts(x, y, test_size=0.3)

regression = LinearRegression()
regression.fit(train_x, train_y)

random = RandomForestRegressor()
random.fit(train_x, train_y)

reg_predict = regression.predict(test_x)
rand_predict = random.predict(test_x)

reg_score = r2(test_y, reg_predict)
rand_score = r2(test_y, rand_predict)

print(reg_score, rand_score)

#pdf = pd.DataFrame()

#pdf["test_y"] = test_y
#pdf["Regressão Linear"] = reg_predict
#pdf["Random Forest"] = rand_predict

#print(pdf)

#sns.lineplot(data=pdf)

#plt.show()

data = pd.read_csv("input/aula4/novos.csv")

result = regression.predict(data[["TV", "Jornal", "Radio"]])

dfp = pd.DataFrame()


dfp["Vendas"] = result

#sns.lineplot(data=dfp)

sns.histplot(dfp)

plt.show()

#plt.show()

#print(df)

#print(df.info())