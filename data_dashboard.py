from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from datetime import datetime

now = datetime.now().strftime("%d%m%Y-%H%M%S")

sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1', pool_recycle=3600)

dbConnection = sqlEngine.connect()

NAME_LEAGUES = ["EPL", "La_liga", "Bundesliga" , "Serie_A", "Ligue_1"]


for league in NAME_LEAGUES:


    df = pd.read_sql(f"select * from leagues.{league};", dbConnection);

    pd.set_option('display.expand_frame_repr', False)

    df['path'] = df['Team'] + '.png'

    # Set font and background colour
    plt.rcParams.update({'font.family':'Arial'})
    bgcol = '#fafafa'

    # Create initial plot
    fig, ax = plt.subplots(figsize=(6, 4), dpi=120)
    fig.set_facecolor(bgcol)
    ax.set_facecolor(bgcol)
    ax.scatter(df['xG'], df['xGA'], c=bgcol)

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
        ab = AnnotationBbox(getImage(row['path']), (row['xG'], row['xGA']), frameon=False)
        ax.add_artist(ab)

    # Add average lines
    plt.hlines(df['xGA'].mean(), df['xG'].min(), df['xG'].max(), color='#c2c1c0')
    plt.vlines(df['xG'].mean(), df['xGA'].min(), df['xGA'].max(), color='#c2c1c0')

    # Text

    ## Title & comment
    fig.text(.15,.98,'xG Performance',size=20)
    fig.text(.15,.93,'Turns out some teams good, others bad', size=12)

    ## Avg line explanation
    fig.text(.06,.14,'xG Against', size=9, color='#575654',rotation=90)
    fig.text(.12,0.05,'xG For', size=9, color='#575654')

    ## Axes titles
    fig.text(.76,.535,'Avg. xG Against', size=6, color='#c2c1c0')
    fig.text(.325,.17,'Avg. xG For', size=6, color='#c2c1c0',rotation=90)

    # plt.show()

    ## Save plot
    plt.savefig(f'data\\images-xGchart\\xGChart{league}-{now}.png', dpi=1200, bbox_inches = "tight")

dbConnection.close()
