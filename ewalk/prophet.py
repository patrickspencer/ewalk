import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt
from IPython.display import display, HTML

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(np.random.randn(5),  index=['1', '2', '3', '4', '5'], columns=['y','ds'])
# display(df1)
# print(np.random.randn(5))
# m = Prophet()
# m.fit(df)  # df is a pandas.DataFrame with 'y' and 'ds' columns
# future = m.make_future_dataframe(periods=365)
# m.predict(future)
