#Using Pandas
import pandas as pd

df = pd.read_csv('Project1CPS.csv')
print(df)

#Adding all blue side and red side wins
print('')
sum_blue = df['WinsOnBlueSide'].sum()
print("The sum of Blue sided wins are:",sum_blue)
sum_red = df['WinsOnRedSide'].sum()
print("The sum of Red sided wins are:",sum_red)

#Add both blue and red side wins
sum_Both = sum_blue + sum_red
print('')
print("In total, the amount of wins are:", sum_Both)

#Display the blue side win percentage neatly 
WinPer_Blue = sum_blue / sum_Both
print("The win percentage of blue side is: %",format(WinPer_Blue,".3f"), "Percent")

#Displaying the team with the highest amount of wins on blue side
df = df[['TeamName','WinsOnBlueSide']][df.WinsOnBlueSide==df['WinsOnBlueSide'].max()]

print('')
print("The team with the highest amount of wins on blue side is: ")
print('')
print(df)