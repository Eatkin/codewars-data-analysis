# https://www.codewars.com/kata/5962d557be3f8bb0ca000010
# 2023-05-22T18:46:35.096+0000
import numpy as np
def clean_mean(sample, cutoff):
    sample = np.array(sample)
    # Initial calculation
    mean = np.mean(sample)
    std = np.std(sample)
    
    lower = mean - std * cutoff
    upper = mean + std * cutoff
    while not np.all((sample >= lower) & (sample <= upper)):
        sample = sample[(sample >= lower) & (sample <= upper)]
        mean = np.mean(sample)
        std = np.std(sample)
        lower = mean - std * cutoff
        upper = mean + std * cutoff
        
    return round(mean, 2)