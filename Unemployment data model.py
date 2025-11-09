import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#reading the twwwo csv's
df1 = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
df2 = pd.read_csv('Unemployment in India.csv')


print('df1.columns')
print("- \n -" *4)
print('df2.columns')

#concatenating the two csvs since they have the same columns

new_df = pd.concat([df1, df2], ignore_index =True)

new_df.to_csv('faith.csv', index = False)
print("New csv generated from joining the above two dataframes")

#faith.csv is ready, let's remove empty rows
fth =  pd.read_csv('faith.csv')
kk =",".join('fth.columns')

# print(f"the headers of the new csv is {kk}")
print("- \n -"*4)

print(fth.columns)

print("\n printed columns of now file")
print("- \n -"*4)


#removing empty rows
fth.dropna(how="all", inplace = True)

#now what is the most logical way to visualize this data
fth.drop_duplicates(inplace= True)


numerical_cols = [' Estimated Unemployment Rate (%)', ' Estimated Employed', ' Estimated Labour Participation Rate (%)', 'longitude', 'latitude']
fth_numerical = fth[numerical_cols]

corr_matrix = fth_numerical.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.savefig("Faith's Matrix.png")
print("Saved correlation matrix!")
print("- \n -"*4)


fth.set_index('Region.1')
fth_to_plot = fth[[' Estimated Unemployment Rate (%)', ' Estimated Labour Participation Rate (%)']]
fth_to_plot.plot(kind='bar', figsize=(10, 6), rot=0)

plt.title("Chart shaa")
plt.xlabel("Parama")
plt.ylabel("Region")
plt.legend(title='Class')

# Show the plot
plt.savefig('faith-bar.png')
print("Saved bar chart!")
print("- \n -"*4)


fth[' Date'] = pd.to_datetime(fth[' Date'])

# Sort the data by date to ensure the plot is in chronological order
fth = fth.sort_values(' Date')
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot the unemployment rate on the first y-axis (ax1)
ax1.set_xlabel('nDate')
ax1.set_ylabel('Estimated Unemployment Rate (%)', color='tab:red')
ax1.plot(fth[' Date'], fth[' Estimated Unemployment Rate (%)'], color='tab:red', label='Unemployment Rate')
ax1.tick_params(axis='y', labelcolor='tab:red')

# Create a second y-axis that shares the same x-axis
ax2 = ax1.twinx()

# Plot the number of employed on the second y-axis (ax2)
ax2.set_ylabel('Estimated Employed', color='tab:blue')
ax2.plot(fth[' Date'], fth[' Estimated Employed'], color='tab:blue', label='Estimated Employed')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Add titles and legends
plt.title('Unemployment Rate and Employment Over Time')
fig.tight_layout() # Adjusts plot to fit labels
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.savefig('faith-graph.png')
print("Saved Graph!")
print("- \n -"*4)
print("@Fluxx 21-10-25")
print("Closing program.........")
print("\n")