import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans

# Import data about fires
# path = input("Please enter your folder address")
# path += '/Data.csv'
path = 'Traffic_Collision_Data_from_2010_to_Today.csv'
frame = pd.read_csv(path)
print(frame)

# Filter variables to remove useless, duplicate variables.
frame.drop(['DR Number', 'Date Reported', 'Area ID', 'Crime Code',
            'Crime Code Description', 'Premise Code'], axis=1, inplace=True)
print(frame)
# Remove missing values
frame.dropna(inplace=True, how='all')
# Preprocessing is over

# Split date data
frame['Time Occurred'] = pd.to_datetime(frame['Date Occurred']+' '+frame['Time Occurred'])
frame['Date Occurred'] = pd.to_datetime(frame['Date Occurred'])
print('Time Occurred',frame['Time Occurred'])
frame['year'] = frame['Date Occurred'].dt.year
frame['day_of_week'] = frame['Date Occurred'].dt.dayofweek
# frame['Time Occurred'] = frame['Time Occurred'].astype(str)
# frame['hour'] = [hour[:2] if len(hour) == 4 else (hour[0] if len(hour) == 3 else '0')
#                  for hour in frame['Time Occurred']]
frame['hour'] = frame['Time Occurred'].dt.hour
# frame['Time Occurred'] = frame['Time Occurred'].astype(int)
frame['Date'] = frame['Date Occurred']
frame.index = pd.DatetimeIndex(frame['Date'])
frame.drop(['Date'], axis=1, inplace=True)

# question 1     Total collisions per day

# mean and standard deviation
collisions_each_day = pd.DataFrame(frame.resample('D').size())
collisions_each_day['mean'] = frame.resample('D').size().mean()
collisions_each_day['std'] = frame.resample('D').size().std()
print(collisions_each_day['mean'])

# upper control limit and lower control limit
upper_control_limit = collisions_each_day['mean'] + 3 * collisions_each_day['std']
lower_control_limit = collisions_each_day['mean'] - 3 * collisions_each_day['std']
plt.figure(figsize=(15, 6))
frame.resample('D').size().plot(label='Collisions each day', color='chocolate')
upper_control_limit.plot(color='red', ls='--', linewidth='1.5', label='UCL')
lower_control_limit.plot(color='red', ls='--', linewidth='1.5', label='LCL')
collisions_each_day['mean'].plot(color='red', linewidth='2', label='Average')
plt.title('Total collisions per day', fontsize='16')
plt.xlabel('Day')
plt.ylabel('The count of collision')
plt.tick_params(labelsize='14')
plt.legend()
plt.show()

# question 2     Total collisions per month
collisions_each_month = frame.resample('M').size()
print(collisions_each_month)
plt.figure(figsize=(15, 6))
collisions_each_month.plot(label='Collisions each month', color='chocolate')
collisions_each_month.rolling(window=12, min_periods=1).mean().plot(color='red', linewidth='4', label='Months Average')
plt.title('Total collisions per month', fontsize='16')
plt.legend()
plt.show()

# question 3   Total collisions for each day of the week
total_week_collisions = frame['day_of_week'].value_counts().sort_index()
total_week_collisions = total_week_collisions.to_frame()
total_week_collisions.columns = ['Counts']
total_week_collisions['Week day'] = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(total_week_collisions)
plt.figure(figsize=(15, 6))
plt.bar(data=total_week_collisions, x=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        height='Counts', color='chocolate')
plt.show()

# question 4   Total collision by descent and month
collisions_months_descent = frame.pivot_table(index='Date Occurred', columns='Victim Descent', aggfunc='size')
collisions_months_descent = collisions_months_descent.resample('M').sum()
print(collisions_months_descent)
collisions_months_descent.drop(['Filipino', 'Chinese', 'Hawaiian', 'Japanese', 'Vietnamese', 'Pacific Islander',
                                'American Indian', 'Asian Indian', 'Guamanian', 'Samoan', 'Cambodian', 'Laotian'],
                               axis=1, inplace=True)
print(collisions_months_descent)
collisions_months_descent.rolling(window=12, min_periods=1).mean().plot(linewidth=3, cmap='Set1', figsize=(15, 6))
plt.xlabel('Year')
plt.title('Moving Average of Collisions per Month')
plt.show()

# question 5   Total collision by age
plt.figure(figsize=(15, 6))
sns.distplot(frame['Victim Age'], color='chocolate')
plt.ylabel('Age Density')
plt.show()

# question 6
frame_2022 = frame[frame['year'] == 2022]
frame_new = pd.concat([frame_2022[frame_2022['Victim Descent'] == 'Hispanic'],
                       frame_2022[frame_2022['Victim Descent'] == 'White'],
                       frame_2022[frame_2022['Victim Descent'] == 'Black'],
                       frame_2022[frame_2022['Victim Descent'] == 'Other Asian']],
                      ignore_index=True)
print(frame_new['Victim Descent'])
plt.figure(figsize=(16, 20))
sns.scatterplot(data=frame_new, x='Long_DD', y='Lat_DD', hue='Victim Descent', palette='deep')
plt.title('Location of Collision in 2022')
plt.show()

# question 7
frame_2022 = frame[frame['year'] == 2022]
frame_2022_xy = frame_2022[['Lat_DD','Long_DD']]
frame_2022_xy = np.array(frame_2022_xy)
plt.scatter(frame_2022_xy[:,0],frame_2022_xy[:,1],s=1)
kmeans2 = KMeans(n_clusters=3,random_state=10000).fit(frame_2022_xy)
label_pred = kmeans2.labels_
print(kmeans2.cluster_centers_)
frame_2022_xy = np.array(frame_2022_xy)
plt.scatter(frame_2022_xy[:,0],frame_2022_xy[:,1],s=1,c='red')
plt.show()
x0 = frame_2022_xy[label_pred == 0]
x1 = frame_2022_xy[label_pred == 1]
x2 = frame_2022_xy[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c = "red", marker='o', label='High-incidence area one')
plt.scatter(x1[:, 0], x1[:, 1], c = "green", marker='*', label='High-incidence area two')
plt.scatter(x2[:, 0], x2[:, 1], c = "blue", marker='+', label='High-incidence area three')
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.legend(loc=2)
plt.show()