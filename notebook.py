import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

df = pd.read_csv('./data/EPL/g-and-ga-EPL.csv')
df.head()

df['path'] = df['Team'] + '.png'
df.head()

fig, ax = plt.subplots(figsize=(6, 4), dpi=120)
ax.scatter(df['G'], df['GA'])

fig, ax = plt.subplots(figsize=(6, 4), dpi=120)
ax.scatter(df['G'], df['GA'], color='white')

def getImage(path):
    return OffsetImage(plt.imread('images/' + path), zoom=.5, alpha = 1)

for index, row in df.iterrows():
    ab = AnnotationBbox(getImage(row['path']), (row['G'], row['GA']), frameon=False)
    ax.add_artist(ab)

plt.show()

# Set font and background colour
plt.rcParams.update({'font.family':'Arial'})
bgcol = '#fafafa'

# Create initial plot
fig, ax = plt.subplots(figsize=(6, 4), dpi=120)
fig.set_facecolor(bgcol)
ax.set_facecolor(bgcol)
ax.scatter(df['G'], df['GA'], c=bgcol)

# Change plot spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('#ccc8c8')
ax.spines['bottom'].set_color('#ccc8c8')

# Change ticks
plt.tick_params(axis='x', labelsize=12, color='#ccc8c8')
plt.tick_params(axis='y', labelsize=12, color='#ccc8c8')

# Plot badges
def getImage(path):
    return OffsetImage(plt.imread('images/' + path), zoom=.5, alpha = 1)

for index, row in df.iterrows():
    ab = AnnotationBbox(getImage(row['path']), (row['G'], row['GA']), frameon=False)
    ax.add_artist(ab)

# Add average lines
# plt.hlines(df['GA'].mean(), df['G'].min(), df['G'].max(), color='#c2c1c0')
# plt.vlines(df['G'].mean(), df['GA'].min(), df['GA'].max(), color='#c2c1c0')

# Text

## Title & comment
fig.text(.15,.98,'G Performance',size=20)
fig.text(.15,.93,'Turns out some teams good, others bad', size=12)

## Avg line explanation
fig.text(.06,.14,'G Against', size=9, color='#575654',rotation=90)
fig.text(.12,0.05,'G For', size=9, color='#575654')

## Axes titles
# fig.text(.76,.535,'Avg. G Against', size=6, color='#c2c1c0')
# fig.text(.325,.17,'Avg. G For', size=6, color='#c2c1c0',rotation=90)

plt.show()

## Save plot
plt.savefig('GChart.png', dpi=1200, bbox_inches = "tight")