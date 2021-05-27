import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter
import pandas as pd
pd.set_option('display.max_rows', None)


def removeNearDuplicates(df):
    df = df.reset_index(drop=True)
    delta = 15
    duplicates = []
    for rowA in df.itertuples(name='A'):
        da = rowA._asdict()
        for rowB in df.itertuples(name='B'):
            db = rowB._asdict()
            if db['Index'] <= da['Index']: continue
            if abs(da['cx'] - db['cx']) < delta and abs(da['cy'] - db['cy']) < delta:
                duplicates.append(db['Index'])
                
    # the above algorithm may detect a duplicate more than once; use set to correct
    for d in set(duplicates):
        df = df.drop(d)
    
    # drop=True discards the old index
    df = df.reset_index(drop=True)
    return df

# perform edge detection on grayscale image
image = io.imread("images/tablets.jpg", as_gray=True) * 256
edges = canny(image, sigma=4, low_threshold=0, high_threshold=30)


# radii range from 33 to 35
tablet_radii = [33, 34, 35]

# perform Hough transform on image
accumulators_for_every_pixel = hough_circle(edges, tablet_radii)

# select the most prominent circles
top_accumulators, cx, cy, radii = hough_circle_peaks(accumulators_for_every_pixel, tablet_radii, total_num_peaks=200)

# form dataframe so we can remove "near" duplicates
df = pd.DataFrame(zip(cx, cy, radii))
df.columns = ['cx', 'cy', 'r']
df = df.sort_values(by=['cx', 'cy'])
df = removeNearDuplicates(df)
       
# display the original image with the circles highlighted
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4), dpi=72*2)
image = io.imread("images/tablets.jpg", as_gray=False)

for index, row in df.iterrows():
    # determine points on circle perimeters
    cy, cx = circle_perimeter(row['cy'], row['cx'], row['r'], shape=image.shape)
    # print ordinal number in eacg circle
    plt.text(row['cx']-18, row['cy']+9, f"{index+1:2}", color="red", fontsize=6)
    # highlight circle primeters (linewidth = 5 pixels)
    r = [-2,-1,0,1,2]
    for dx in r:
        for dy in r:
            image[cy+dy, cx+dx] = (0, 255, 0)    
ax.imshow(image, cmap=plt.cm.gray)
plt.show()
 
# display the final dataframe
print(df)



