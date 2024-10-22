# library visualization data
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# ....
def lineplot(dataset, x, y, title):

  # create figure
  fig, ax = plt.subplots(figsize=(8,4))
  
  # create barplot
  sns.lineplot(data=dataset, x=x, y=y, linewidth=2.5)

  # set labels
  ax.set_title(title)
  ax.set_xlabel('')
  ax.set_ylabel('')
  ax.grid(True)

  # display plot
  fig.tight_layout()
  return fig
  # ----------------------------------------------------------------------------------------------------------------------

# ....
def barplot(dataset, x, y, hue, title):

  # create figure
  fig, ax = plt.subplots(figsize=(8,4))
  
  # create barplot
  sns.barplot(data=dataset, x=x, y=y, hue=hue)

  # set labels
  ax.set_title(title)
  ax.set_xlabel('')
  ax.set_ylabel('')
  ax.grid(True)

  # display plot
  fig.tight_layout()
  return fig
  # ----------------------------------------------------------------------------------------------------------------------