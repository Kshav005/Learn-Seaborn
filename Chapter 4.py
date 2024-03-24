# The previous chapters taught some of the basic plots which we already knew. In this chapter, we will look at some of the advanced graphs which are really helpful in the field of data science.

import matplotlib.pyplot as plt, seaborn as sns

df = sns.load_dataset("planets")

# The joint plot involves the use of scatter and bar plots. The bar actually represents the frequency distribution while the scatter plot has the usual use.
sns.jointplot(data=df, x="mass", y="distance")
plt.show()

# To make it look more beautiful, you can add 'kind', 'fill' (for coloring it) and 'cmap' (for setting a color map). 
sns.jointplot(data=df, x="mass", y="distance", kind="kde", fill=True,cmap="YlGnBu")
plt.show()

# Hex kind is extremely beautiful, to use it, just change the kind and remove 'fill'
sns.jointplot(data=df, x="mass", y="distance", kind="hex",cmap="YlGnBu")
plt.show()

# Let's learn about heat plot now.
# For this we will be using the correlation values from the titanic dataset. We will select only the numerical values in order to avoid any errors. Heat maps are extremely helpful in order to make prediction models.
df = sns.load_dataset("titanic").select_dtypes("number")

# Let's plot a beautiful heatmap
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")           # annot is used for writing values
plt.show()

# In correlation, if the value falls below 0.0, then it means that there is no relation between two fields while above 0 is considered as relational.

# The color maps are actually like themes, you can have a color combination in your graphs using cmaps. It can have values like - 'YlGnBu', 'coolwarm', 'icefire', etc.

