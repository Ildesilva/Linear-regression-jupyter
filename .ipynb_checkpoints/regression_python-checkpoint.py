#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using [Python/R] to model Salary based on Years of Experience.
# 

# In[3]:


import pandas as pd
dataset = pd.read_csv("regression_data.csv")


# In[5]:


import matplotlib.pyplot as plt
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


# In[6]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[7]:


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[8]:


model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared


# In[ ]:




