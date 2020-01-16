# Data incubator project proposal 
## By Sarvenaz Memarzadeh 
### Ph.D. candidate in Electrical Engineering at University of Maryland - College Park


### Topic of proposal:
- Prediction of the future electricity load based on the temporal patterns (time series analysis) and available weather features (temperature, wind, humidity and ...).

## Introduction 

Forcasting is one of the major challenges of the data scientists and often providing a reasonable prediction is not an easy task. Realibility, evaluation, efficiency, automation are some examples of the concerns researchers are facing while developing a new algorithm. To start with the available time series models, I have download and employed the open source software of the "Prophet Forcasting Model" released in Python by Facebook research teams. Advantage of the Prophet package is that the forcast can be slightly tweaked using the easily-interpretable parameters. The core algorithm behind the Propher is the "Additive regression model". This model consists of the main components such as:

- A piecewise linear or logistic growth curve trend.
- A weekly seasonal component using dummy variables.
- A yearly seasonal component modeled using Fourier series.
- A user-provided list of important holidays.



## Analysis and results 

For the data incubator project in summer 2020, I am interested in implementation of the time series forcasting methods to predict the electrical load and market price by considering the metrological conditions. <br>
To start, I have dowloaded two available datasets from Kaggle website.  <br>
1) Energy dataset : Consist of the hourly electric load generation from different energy resources such as fossil, solar, nuclear, wind, hydro and etc over the years of 2015 to 2018 in different cities of spain such as Barcelona, Bilbao, Madrid, Seville, Valencia. However, for the analysis part, I have only focused on one city (Valencia). <br>
2) Weather dataset : Consists of the hourly weather conditions for the same cities over the past 4 years.  The weather conditions are pretty much versatile which lead into the more general interpretation and prediction of the electric load (or market price) at the end.   
For the data analysis, especifically manipulations and visualziation part, I have used Python's packages such as Pandas and Seaborn. <br>

For data visualization, I have ploted two figures.  The first figure shows the electrical load demand curves and the actual electrical price for the first week of January , April, August, and Decemeber of 2015.  
![](images/loadpricevshour.png)

Based on this figure, we can clearly see the oscillation of the load over the hours of the day.  It appreas that there are two peaks indicating that there are two main interval for the electric load consumption for every day over one week.  The trend is approximatly is the same for months of January, April, July, and October.  One interesting point is that, on Fridays and weakends the two load peaks merge into one, denote the approximately high load distribution for those days. In the second subplot, I have plotted the electric price over the same interval for months of January, April, July, and October.  There seems to be correlation between the two plots as the electric load increases, price also increases and vice versa.   


From pie chart below you can see the majority of the electric load generation is due to the nuclear energy.  Since, according to dataset, there are multiple methods for  genertion of electric load thorugh fossil(brown coal,coald derived gas, hard coil, ...), wind (onshore, off shore), and hydro (pumped storage,run-of-river and poundage,..) resources, I have included them all in one dictionary and calculated the mean value for the total fossil, wind and hydro. In the pie chart you can see the mean values correposing to each type of the resource. 

![](images/piechart.png)


# Time series prediction

Time series cross validation is performed for the error prediction of the model. To do so, from "Prophet Forcasting Model", I have imported the cross_validation function to assess the prediction performance by specifying the "forcast horizon" and the "initial training period" as the input parameters. Then, the cross validation procedure can be done for a range of the historical cutoffs. 

The output of cross_validation function is a dataframe with the true values y and the forecast value yhat, at each simulated forecast date and for each cutoff date. In particular, a forecast is made for every observed point between cutoff and cutoff + horizon. This dataframe can then be used to compute error measures of yhat vs. y. I made the prediction (yhat) of the total load actual using the first 180 days in 2015 as the training samples and 5 days as the horizon value.  Since model training procedure took about a day, I have saved the cross validated output in a .pkl format (df_cv.pkl) for the further analysis.  <br>   Finally, for the error prediction, I have used the Prophet performance_metrics function which calculate MSE, RMSE, and MAPE.  I have then plotted the Mean Absolute Percentage Error (MAPE) over the horizon period (5 days = 120 Hours). The blue line shows the MAPE (~ 8%), where the mean is taken over a rolling window of the dots which are the absolute percent error for each prediction in the cross validate data.  




---------------------

<!-- 
Using time series forcasting, explicitly additive model , to predic the electricla price over time by cosidering different metrologcal features such as temperature.
- Additive model is deployed for the financial time series data modeling used in this project. For this purpose, I employed the Prophet forcasting package developed by Facebook.  


Future Dataframe contains estimation of the future electrical price for the next two years which is visualized using the prorphet plot function.
# Time series cross validation using Prophet

To evaluate the performance of the model, we used the time seties cross validation by training the model on the intial 180 days (intial) and then forcasting the values on the following 5 days (cutoff).   The -->