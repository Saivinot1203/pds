# Assuming 'data' is already defined; create a DataFrame
df = pd.DataFrame(data)

# Create a regression plot for Height vs Weight
plt.figure(figsize=(10, 6))
sns.regplot(x='Height', y='Weight', data=df, scatter_kws={'s': 100}, line_kws={"color": "red"})

# Add title and labels
plt.title('Height vs Weight with Regression Line', fontsize=16)
plt.xlabel('Height (inches)', fontsize=14)
plt.ylabel('Weight (lbs)', fontsize=14)

# Save the regression plot to the specified directory
plt.savefig(r"C:\Users\saivi\Downloads\height_vs_weight_regression.png")

# Display the plot
plt.show()


# Assuming 'data' is already defined; create a DataFrame
df = pd.DataFrame(data)

# Create a hexbin plot for Height vs Weight
plt.figure(figsize=(10, 6))
plt.hexbin(df['Height'], df['Weight'], gridsize=30, cmap='Blues', mincnt=1)

# Add a color bar
plt.colorbar(label='Count in hexagon')

# Add title and labels
plt.title('Height vs Weight Hexbin Plot', fontsize=16)
plt.xlabel('Height (inches)', fontsize=14)
plt.ylabel('Weight (lbs)', fontsize=14)

# Save the hexbin plot to the specified directory
plt.savefig(r"C:\Users\saivi\Downloads\height_vs_weight_hexbin.png")

# Display the plot
plt.show()


# Load your data
data = pd.read_csv(r"/content/raw_frailty_dataa.csv")  # Replace with your actual file path

# Strip any whitespace from column names
data.columns = data.columns.str.strip()

# Create a histogram with KDE overlay
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], kde=True, color='green', bins=50, stat='density')

# Add title and labels
plt.title('Age Distribution with KDE', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Density', fontsize=14)

# Save the plot as a PNG file
plt.savefig(r"C:\Users\saivi\Downloads\Age_Distribution_with_KDE.png")

# Display the plot
plt.show()
