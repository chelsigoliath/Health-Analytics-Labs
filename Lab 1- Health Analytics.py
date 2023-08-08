#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Loading CSV file
file_path = "C:/Users/CAU Student/Downloads/rows.csv"
data = pd.read_csv(file_path)

print(data.head())


# In[4]:


# Read in the first row of the CSV
df = pd.read_csv('C:/Users/CAU Student/Downloads/rows.csv', nrows=0)

# Get the column names
column_names = df.columns.tolist()

print(column_names)


# In[5]:


# Check if all required columns are present
required_columns = [
    'index', 'Year', 'LocationAbbr', 'LocationDesc', 'Class', 'Topic', 'Question', 
    'DataSource', 'Response', 'Data_Value_Unit', 'Data_Value_Type', 'Data_Value', 
    'Data_Value_Footnote_Symbol', 'Data_Value_Footnote', 'Data_Value_Std_Err', 
    'Low_Confidence_Limit', 'High_Confidence_Limit', 'Sample_Size', 'Break_Out',
    'Break_Out_Category', 'Geolocation', 'ClassId', 'TopicId', 'QuestionId', 'LocationId', 
    'BreakOutId', 'BreakOutCategoryid', 'ResponseId'
]

missing_columns = [col for col in required_columns if col not in data.columns]

if not missing_columns:
    print("All required columns are present!")
else:
    print(f"Missing columns: {', '.join(missing_columns)}")


# In[6]:


print(df.head())
print(df.describe())
print(df.info())


# In[10]:


# 1. Define the list of categorical columns
categorical_columns = [
    'LocationAbbr', 'Class', 'Topic', 'Question', 'DataSource', 'Response',
    'Data_Value_Unit', 'Data_Value_Type', 'Break_Out', 'Break_Out_Category'
]

# 2. Handle missing values

# For numerical columns
df.fillna(df.mean(), inplace=True)

# For categorical columns
for column in categorical_columns:
    if not df[column].mode().empty:
        df[column].fillna(df[column].mode()[0], inplace=True)
    else:
        df[column].fillna("Missing", inplace=True)  # replace with an appropriate placeholder value

# 3. One-hot encode categorical columns
df_encoded = pd.get_dummies(df, columns=categorical_columns)

# 4. Drop unnecessary columns
columns_to_drop = [
    'index', 'LocationDesc', 'Data_Value_Footnote_Symbol',
    'Data_Value_Footnote', 'Geolocation'
]
df_encoded.drop(columns=columns_to_drop, inplace=True)

# 5. Define X (features) and y (target)
X = df_encoded.drop('Data_Value', axis=1)
y = df_encoded['Data_Value']


# In[11]:


#splitting data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




