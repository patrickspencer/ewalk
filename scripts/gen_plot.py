# Python
import pandas as pd
import numpy as np
from fbprophet import Prophet

# Python
df = pd.read_csv('data/peyton.csv')
df['y'] = np.log(df['y'])

#fbprohpet throws a TypeError if we don't clear duplicates first
df=df.drop_duplicates(['ds'], keep='last')
print(df.head())
m = Prophet()
m.fit(df);
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)
m.plot(forecast);
print(type(m))


