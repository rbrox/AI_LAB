
import pandas as pd
import numpy as np

def makedata():

# Define the array
    data = [[30.0, 'unemployed', 'married', 1787.0, 'no', 'no', 'cellular', 'oct'],
            [33.0, 'services', 'married', 4789.0, 'yes', 'yes', 'cellular', 'may'],
            [35.0, 'management', 'single', 1350.0, 'yes', 'no', 'cellular', 'apr'],
            [30.0, 'management', 'married', 1476.0, 'yes', 'yes', 'unknown', 'jun'],
            [59.0, 'blue-collar', 'married', 0.0, 'yes', 'no', 'unknown', 'may'],
            [35.0, 'management', 'single', 747.0, 'no', 'no', 'cellular', 'feb'],
            [36.0, 'self-employed', 'married', 307.0, 'yes', 'no', 'cellular', 'may'],
            [39.0, 'technician', 'married', 147.0, 'yes', 'no', 'cellular', 'may'],
            [41.0, 'entrepreneur', 'married', 221.0, 'yes', 'no', 'unknown', 'may'],
            [43.0, 'services', 'married', -88.0, 'yes', 'yes', 'cellular', 'apr'],
            [39.0, 'services', 'married', 9374.0, 'yes', 'no', 'unknown', 'may'],
            [43.0, 'admin.', 'married', 264.0, 'yes', 'no', 'cellular', 'apr'],
            [36.0, 'technician', 'married', 1109.0, 'no', 'no', 'cellular', 'aug'],
            [20.0, 'student', 'single', 502.0, 'no', 'no', 'cellular', 'apr'],
            [31.0, 'blue-collar', 'married', 360.0, 'yes', 'yes', 'cellular', 'jan'],
            [40.0, 'management', 'married', 194.0, 'no', 'yes', 'cellular', 'aug'],
            [56.0, 'technician', 'married', 4073.0, 'no', 'no', 'cellular', 'aug'],
            [37.0, 'admin.', 'single', 2317.0, 'yes', 'no', 'cellular', 'apr'],
            [25.0, 'blue-collar', 'single', -221.0, 'yes', 'no', 'unknown', 'may'],
            [31.0, 'services', 'married', 132.0, 'no', 'no', 'cellular', 'jul']]

    columns = ['age', 'job', 'marital', 'balance', 'loan', 'housing', 'contact', 'month']
    return pd.DataFrame(data, columns=columns)
df = makedata()
np.sum(df[:5,3])


