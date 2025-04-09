import pandas as pd
import matplotlib.pyplot as plt

df_pct_poverty['poverty_rate'] = pd.to_numeric(df_pct_poverty['poverty_rate'], errors='coerce')

state_poverty = df_pct_poverty.groupby("Geographic Area")["poverty_rate"].mean().sort_values()

plt.figure(figsize=(12, 6))
state_poverty.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title("Average Poverty Rate by U.S. State")
plt.xlabel("State")
plt.ylabel("Poverty Rate (%)")
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()