#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud  # Importing WordCloud module


# In[2]:


data = pd.read_csv('nyka_top_brands_cosmetics_product_reviews.csv')


# In[3]:


# Exploratory Data Analysis (EDA)
# Visualize distribution of review ratings
plt.figure(figsize=(8, 6))
sns.countplot(x='review_rating', data=data)
plt.title('Distribution of Review Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()


# In[4]:


# Analyze top beauty brands by review count
top_brands = data['brand_name'].value_counts().head(10)
print("Top Beauty Brands by Review Count:")
print(top_brands)


# In[5]:


# Visualize top brands by review count
plt.figure(figsize=(10, 6))
sns.barplot(x=top_brands.index, y=top_brands.values)
plt.title('Top Beauty Brands by Review Count')
plt.xlabel('Brand Name')
plt.ylabel('Review Count')
plt.xticks(rotation=45)
plt.show()


# In[6]:


# Analyze top-rated products
top_rated_products = data.groupby('product_title')['review_rating'].mean().sort_values(ascending=False).head(10)
print("\nTop-Rated Products:")
print(top_rated_products)


# In[7]:


# Visualize top-rated products
plt.figure(figsize=(10, 6))
sns.barplot(x=top_rated_products.values, y=top_rated_products.index, palette='viridis')
plt.title('Top-Rated Products')
plt.xlabel('Average Rating')
plt.ylabel('Product Title')
plt.show()


# In[8]:


# Sort the dataset by 'review_rating' column in ascending order to get the worst-rated products
worst_rated_products = data.sort_values(by='review_rating', ascending=True)

# Display the products with the lowest ratings
print("Products with the Lowest Ratings:")
print(worst_rated_products[['product_title', 'review_rating']].head(10))


# In[9]:


# Sort the dataset by 'review_rating' column in ascending order to get the worst-rated products
worst_rated_products = data.sort_values(by='review_rating', ascending=True)

# Sort the dataset by 'review_rating' column in descending order to get the best-rated products
best_rated_products = data.sort_values(by='review_rating', ascending=False)

# Plotting the distribution of review ratings for worst and best-rated products
plt.figure(figsize=(10, 6))
sns.histplot(data=worst_rated_products, x='review_rating', bins=10, color='red', alpha=0.5, label='Worst Rated Products')
sns.histplot(data=best_rated_products, x='review_rating', bins=10, color='blue', alpha=0.5, label='Best Rated Products')
plt.title('Distribution of Review Ratings for Worst and Best Rated Products')
plt.xlabel('Review Rating')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




