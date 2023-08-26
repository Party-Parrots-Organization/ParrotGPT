import pandas as pd

# Convert the XLXS file to a pd dataframe
df = pd.read_csv('chat_transcript_2023.csv')

# Drop unnecessary columns
columns_to_drop = ['Chat ID', 'Email domain', 'Browser', 'Operating System', 'User Agent', 'Referrer', 'Widget',
'Department', 'Timestamp', 'Comment', 'Wait Time (seconds)', 'Duration (seconds)', 'Screensharing',
'User Field 1', 'User Field 2', 'User Field 3', 'Initial Question', 'Transfer History', 'Message Count',
'Internal Note', 'Tags', 'Ticket ID'
]
df = df.drop(columns=columns_to_drop)

# Define the condition
condition = df['Rating (0-4)'] > 3

# Drop rows that do not meet the condition
df = df[condition]

# See the first few rows
print(df.head())

# Drop the Rating column
df = df.drop("Rating (0-4)", axis=1)

df.to_csv('processed_dataframe.csv', index=False)