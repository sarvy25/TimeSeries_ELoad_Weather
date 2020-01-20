# Data incubator project proposal 
## By Sarvenaz Memarzadeh 
### Ph.D. candidate in Electrical Engineering at University of Maryland - College Park


### Topic of proposal:
- Prediction of the future electricity load based on the temporal patterns (time series analysis) and available weather features.

## Introduction 

Forcasting is one of the major challenges in datascience and often providing a reasonable prediction is not an easy task. Specifically, forcasting the energy load and price from historical data benefits a wide range of spectrum; from researchers and engineers in power agencies, transportation systems, vehicle manufacturer, consulting managements, to the local and national governments, energy forcast is the most vauable data. Furthermore, tackling the climate change is another main concerns of the recent world.  The effect of the climate change can impact on many industries; therefore, before any critical conditions happen we need to think of a way to tackle the situation. <br>
The interesting problem  arises when we think of these two factors all together,that is, the energy forcast and the climate change. For this proposal, I am interested in studying the combination of these two parameters together. I want to investigate the machine learning approaches to successfully forcast the power demand and price based on the metrological variables such as temperature, humidity, wind and so on. Finally, this will open up versatile research directions on application of the machine learning for tackling the climate change.


## Analysis and results 

For the data incubator project in summer 2020, I am interested in implementation of the time series forcasting methods to predict the electrical load and market price by considering the effect of the  metrological conditions. <br>
To start, I have dowloaded two available datasets from Kaggle website.  <br>
1) Energy dataset: Consist of the hourly electric load generation from different energy resources such as fossil, solar, nuclear, wind, hydro and etc over the years of 2015 to 2018 in 5 largest cities of spain Barcelona, Bilbao, Madrid, Seville, Valencia. However, for the analysis part, I have only focused on one city, Valencia. <br>
2) Weather dataset: Consists of the hourly weather conditions for the same cities over the past 4 years.  The weather conditions are pretty much versatile which can result into the more general interpretation, and prediction of the electric load (or market price) at the end.   
For the data analysis, especifically manipulations and visualziation part, I have used Python's software packages such as Pandas and Seaborn. <br>

# Data visualization
For data visualization, I have ploted three figures.  The first figure shows the electrical load demand curves and the actual electrical price during the first week of months January ,April, August, and Decemeber of 2015.  
![](images/loadpricevshour.png)

Based on this figure, we can clearly see the oscillations of the load plots over different hours of the days. Acoording to that, there are 7 oscillations each related to one day of the week, starting from Monday. Also, It apprears that there are two peaks indicating two main intervals for the electric load consumption every day over the period of one week. Plus, the load trend looks independent and approximately similar all over the months of January, April, July, and October. <br>
One interesting point is that, the two load peaks that are distigushable during weekdays, merge into one over the weekends. This denotes the high and approximately uniform load distribution over morning to evening hours of the weekends (especially on Sundays). In the second subplot, I have plotted the electric price over the same interval over the months of January, April, July, and October.  There seems to be a correlation between the two plots as the electric load increases,also price increases and vice versa. <br>  

For the second visualization, I have plotted a pie chart showing the mean percentage value of electric generation due to all different types of the available energy resources over the past 4 years.  To further simply, as there are multiple methods for genertion of electric load through fossil(e.g. brown coal,coald derived gas, hard coil, ...), wind (e.g. onshore, off shore), and hydro (e.g. pumped storage,run-of-river and poundage,..), I have grouped them each individually in one list as the total_hydro, total_fossil, and wind; and then calculated the mean values of the **total** of the fossil, wind and hydro.
From pie chart below you can see the majority of the electric load generation is due to the nuclear energy.  Since, a In the pie chart you can see the mean values correposing to each type of the resource. 

![](images/piechart.png)

Lastly, to show the effect of the weather features on the electric loads, I have employed seaborn library and plotted the probability distribution of the total electric load based on each weather features over the selected hours (i.e. 7am, 1pm, 6pm, and 10 pm). Some of the results and observations are:

- The probability of load distributions (even at specific time of the day) are compeletly different and it depends on the weather conditions.
- The varience of the distibutions are different.  The data is more spread between (2000MW - 4000MW) for the morning and afternoon hours, and it shifts down to (2000 MW - 3000 MW) for the late night hours.
- It's interesting that the thunderstorm weather makes the total load higher compared to the other weather conditions. Also, the distribution has a smaller standarad deviation compared to the other features.
![](images/probdist_0.png)
![](images/probdist_1.png)
![](images/probdist_2.png)
![](images/probdist_3.png)




# Time series prediction


To start with the available time series models, I have download and employed the open source software of the "Prophet Forcasting Model" released in Python by Facebook research teams. The core algorithm behind the Propher is the "Additive regression model". Advantage of the Prophet package is that the forcast can be slightly tweaked using the easily-interpretable parameters.  Another main component of this model is the user-provided list of important holidays. First, I imported and fitted the model over the mask that only covers year of 2015. The year selection was completely arbitarary. Then, time series cross validation is performed for the error prediction. To do so, from "Prophet Forcasting Model", I have imported the cross_validation function to assess the prediction performance by specifying the "forcast horizon" and the "initial training period" as the input parameters. Then, the cross validation procedure can be done for a range of the historical cutoffs. <br>
The output of cross_validation function is a dataframe with the true values y and the forecast value yhat, at each simulated forecast date and for each cutoff date. In particular, a forecast is made for every observed point between cutoff and cutoff + horizon. This dataframe can then be used to compute error measures of yhat vs. y. I made the prediction (yhat) of the total load actual using the first 180 days in 2015 as the training samples and 5 days as the horizon value.  Since model training procedure took about a day, I have saved the cross validated output in a .pkl format (df_cv.pkl) for the further analysis.  <br>   
Finally, for the error prediction, I have used the Prophet performance_metrics function which calculate MSE, RMSE, and MAPE.  I have then plotted the Mean Absolute Percentage Error (MAPE) over the horizon period (5 days = 120 Hours). The blue line shows the MAPE (~ 8%), where the mean is taken over a rolling window of the dots which are the absolute percent error for each prediction in the cross validate data.  

![](images/fig_cv.png)



cutoff).   The -->