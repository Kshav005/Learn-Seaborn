# In this chapter, we are going to study about box plot and strip plots and let's look how are they useful and much easier to plot in seaborn.
import matplotlib.pyplot as plt, seaborn as sns


# Creating a small data for our work.
gender = ["A", "B", "A", "B", "A", "A", "B", "A", "A", "A"]
age = [12, 32, 50, 32, 31, 32, 34, 45, 32, 12]
# To plot box graph
sns.boxplot(x=gender, y=age)
plt.show()


# A strip plot is a graph which is equally useful like the box plot.
sns.stripplot(x=gender, y=age)
plt.show()

