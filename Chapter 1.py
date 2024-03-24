# Welcome back to another tutorial which is about Seaborn. It is used with matplotlib in order to create more advanced statistical graphs!
# Let's learn how to use it!
# First of all, in your terminal, type 'pip install seaborn' to install the package.
import seaborn as sns        # 'sns' is general alias used in data science field.
import matplotlib.pyplot as plt             # sns uses matplotlib, so import it too
from matplotlib import style        # For themes

# We use datasets in order to create visualizations but before that, we need to a dataset. So, seaborn provides sample datasets which you can directly import here and use for your own work!

style.use("ggplot")

# Run the below command in order to see which datasets are there in seaborn.
print(sns.get_dataset_names())

# For the tutorial, we will work with the planets dataset
df = sns.load_dataset("planets")

# Let's see what columns it consists of
print(df.columns)

# Now, to plot a basic scatter plot, we will do this 'scatterplot(data, x, y)'
sns.scatterplot(data=df,x="mass", y="orbital_period")
plt.show()

plt.figure(1)
# To represent categories in colors and size 
sns.scatterplot(data=df, x="mass", y="orbital_period", hue="method", size="year")

plt.figure(2)
# You can also give a color pallete for your dataset
sns.scatterplot(data=df, x="mass", y="orbital_period", hue="method", size="year", palette="YlGnBu")         # Yellow, Green & Blue


# To get the graph, we use the function of matplotlib
plt.show()  