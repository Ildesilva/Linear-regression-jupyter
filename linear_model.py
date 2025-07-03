#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using [Python/R] to model Salary based on Years of Experience.
# 

# In[2]:


import pandas as pd
dataset = pd.read_csv("regression_data.csv")


# In[3]:


import matplotlib.pyplot as plt
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


# In[4]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[5]:


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[7]:


model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared


# **slope** and **intercept** of the fitted line 
# correlation coefficient

# In[ ]:


from scipy.stats import linregress
x = dataset["YearsExperience"]
y = dataset["Salary"]
slope, intercept, r_value, p_value, std_err = linregress(dataset["YearsExperience"], dataset["Salary"])
y_pred = slope * x + intercept


# **mse** between observed and predicted values

# In[ ]:





# In[7]:


from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y, y_pred)


# In[8]:


print(slope)
print(intercept)
print(r_value)
print(mse)


# In[16]:


plt.plot(x, y_pred, label='Fitted line')
plt.text(0.05, 0.95, f"y = {slope:.2f}x + {intercept:.2f}\nr = {r_value:.2f}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')
plt.legend()
plt.show()
plt.savefig("./linear_model.png")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




