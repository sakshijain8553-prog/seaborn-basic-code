import seaborn as sns
import matplotlib.pyplot as plt

tips = sns . load_dataset("tips")

print(tips.head())

sns.scatterplot(data=tips , x="total_bill",y="tip")
plt.title("Bill vs Tip")
plt.savefig("sea.png")
plt.show()

sns.histplot(tips['total_bill'],bins = 10,kde=False)
plt.title("Bill vs Tip")
plt.savefig("sea2.png")
plt.show()


sns.boxplot(data=tips,x='day',y='total_bill')
plt.title("Bill vs Days")
plt.savefig("box.png")
plt.show()

sns.countplot(data=tips , x='day')
plt.title("no.of customers per day")
plt.savefig("sea.png")
plt.show()
