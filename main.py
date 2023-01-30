import numpy as np
import pandas as pd
from metalog import metalog

salmon = pd.read_csv("Chinook and forage fish lengths.csv")

# Filtered data for eelgrass vegetation and chinook salmon
salmon = salmon[(salmon['Vegetation'] == 'Eelgrass') &
                (salmon['Species'] == 'Chinook_salmon')]
salmon = np.array(salmon['Length'])

salmon = np.ndarray.tolist(salmon)
metalog_salmon = metalog.fit(x=salmon, boundedness='b', bounds=[
                             0, 200], term_limit=8)
# metalog.summary(m=metalog_salmon)
# metalog.plot(m=metalog_salmon)


# print(metalog.p(m=metalog_salmon, q=[0.1, 0.5, 0.9], term=8))
# print(metalog.r(m=metalog_salmon, n=100, term=8))
print(metalog)
