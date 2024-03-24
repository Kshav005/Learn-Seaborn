# Let's look at more of the functionalities provided by the seaborn module
import seaborn as sns, matplotlib.pyplot as plt

# Let's plant a histogram this time.
df = sns.load_dataset("planets")
sns.histplot(df["method"], kde=True)        # kde is used to draw a line along with bars
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Similiar to histogram but the only difference is that the bars have more height than histogram's.
sns.displot(df["method"], kde=True)
plt.xticks(rotation=45)
plt.figure(1)

# Another one that you can plot using sns is bar graph which is of course really helpful in order to get insights.
plt.figure(2)
sns.barplot(data=df[:10], x="mass", y="orbital_period")
plt.show()



