#program calculates the probablity of a passenger surviving the titanic crash
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df= pd.read_csv(url)



#handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

#remove duplicates
df= df.drop_duplicates()

#filter data: passengers in first class
first_class= df[df["Pclass"]==1]


#survival rate by class
survival_by_class= df.groupby("Pclass")["Survived"].mean()  
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival by class")
plt.ylabel("Survival rate")
plt.show()

#histogram: age distribution
survival_by_age= df.groupby("Age")["Survived"].mean()  
survival_by_age.plot(kind="bar", color="skyblue")
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Survival rate")
plt.show()

#survival by gender
survival_by_sex= df.groupby("Sex")["Survived"].mean()
survival_by_sex.plot(kind="bar", color="skyblue")
plt.title("Survival by gender")
plt.ylabel("Survival rate")
plt.show()

#scatter plot : age vs fare
plt.scatter(df["Age"], df["Fare"],alpha =0.5, color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()