dataset <- read.csv("regression_data.csv")

plot(dataset$YearsExperience, dataset$Salary, col="red")

model <- lm(Salary ~ YearsExperience, data=dataset)

library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$YearsExperience, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$YearsExperience, y = predict(model, newdata = dataset)), colour = 'blue') +
  ggtitle('Salary vs Experience') +
  xlab('Years of experience') +
  ylab('Salary')

summary(model)

x <- dataset$YearsExperience
y <- dataset$Salary
model <- lm(y ~ x)
slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(x, y)

mse <- mean((predict(model) - y)^2)



print("intercept")
print(intercept)
print ("slope")
print (slope)
print("r")
print(r)
print("mse")
print(mse)

library(ggplot2)

p <-ggplot(dataset, aes(x = YearsExperience, y = Salary)) +
  geom_point() +
  geom_smooth(method = 'lm', se = FALSE) +
  annotate(
    "text",
    x = max(x) * 0.6,
    y = max(y) * 0.9,
    label = paste(
      "y =", round(slope, 2), "x +", round(intercept, 2),
      "\nr =", round(r, 2)
    ),
    hjust = 0
  ) +
  xlab("Years of Experience") +
  ylab("Salary")
ggsave("regression_plot_r.png",
       plot = p,
       width = 4, height = 2.5,
       units = "in", dpi = 150)






