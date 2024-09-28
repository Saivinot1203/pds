# Create a box plot to visualize the distribution of Percentage by gender
plt.figure(figsize=(6, 6))  # Adjust the size as needed
sns.boxplot(x='gender', y='Percentage', data=df, palette='pastel')

# Add labels and title
plt.xlabel('Gender')
plt.ylabel('Percentage')
plt.title('Distribution of Percentage by Gender')

# Save the plot as a PNG file
plt.savefig(r"C:\Users\saivi\Downloads\percentage_distribution_by_gender.png")

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Count the occurrences of each lunch type
lunch_count = df['lunch'].value_counts()

# Create a bar plot for lunch distribution
plt.figure(figsize=(6, 4))  # Adjust the size as needed
sns.barplot(x=lunch_count.index, y=lunch_count.values, palette='pastel')

# Add labels and title
plt.xlabel('Lunch Type')
plt.ylabel('Count')
plt.title('Types of Lunch Distribution')

# Save the plot as a PNG file
plt.savefig(r"C:\Users\saivi\Downloads\lunch_distribution.png")

# Display the plot
plt.show()

# Create a scatter plot with a regression line
plt.figure(figsize=(6, 6))  # Adjust the size as needed
sns.regplot(x='reading score', y='writing score', data=df, marker='o', color='blue')

# Add labels and title
plt.xlabel('Reading Score')
plt.ylabel('Writing Score')
plt.title('Reading vs Writing Scores with Regression Line')

# Save the plot as a PNG file
plt.savefig(r"C:\Users\saivi\Downloads\reading_vs_writing_regression.png")

# Display the plot
plt.show()

# Create a combined histogram and KDE plot for writing scores
plt.figure(figsize=(6, 4))  # Adjust the size as needed
sns.histplot(df['writing score'], bins=25, color='blue', kde=True, edgecolor='black', stat='density', alpha=0.5)

# Add labels and title
plt.xlabel('Writing Score')
plt.ylabel('Density')
plt.title('Distribution of Writing Scores with KDE')

# Save the plot as a PNG file
plt.savefig(r"C:\Users\saivi\Downloads\writing_score_distribution.png")

# Display the plot
plt.show()

# Create a violin plot for writing scores by gender
plt.figure(figsize=(6, 6))  # Adjust the size as needed
sns.violinplot(x='gender', y='writing score', data=df, palette='pastel')

# Add labels and title
plt.xlabel('Gender')
plt.ylabel('Writing Score')
plt.title('Writing Score Distribution by Gender')

# Save the plot as a PNG file
plt.savefig(r"C:\Users\saivi\Downloads\writing_score_violin_plot.png")

# Display the plot
plt.show()

# Create a histogram with KDE overlay for Percentage
plt.figure(figsize=(6, 4))  # Adjust the size as needed
sns.histplot(df['Percentage'], bins=20, color='red', kde=True, stat='density', edgecolor='black', alpha=0.5)

# Add labels and title
plt.xlabel('Percentage')
plt.ylabel('Density')
plt.title('Distribution of Percentage with KDE')

# Save the plot as a PNG file
plt.savefig(r"C:\Users\saivi\Downloads\percentage_distribution_with_kde.png")

# Display the plot
plt.show()

# Create a pair plot to visualize relationships
plt.figure(figsize=(6, 6))  # Adjust the size as needed
sns.pairplot(df, vars=['Percentage', 'reading score', 'writing score'], kind='scatter', diag_kind='kde', palette='Set1')

# Save the plot as a PNG file
plt.savefig(r"C:\Users\saivi\Downloads\pair_plot.png")

# Display the plot
plt.show()