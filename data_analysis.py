import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Logical_AI_Survey_Responses__45_Participants_.xlsx'
df = pd.read_excel(file_path)

#counting missing values
#print(df.isnull().sum())

# iterating over missing values
# for index, row in df.iterrows():
#     for col in df.columns:
#         if pd.isna(row[col]):
#             if row["Used Chatbot"] == "No":
#                 df.at[index, col] = "Not Applicable"
#             elif row["Use AI for Psychological Counseling"] == "No":
#                 df.at[index, col] = "Not Applicable"
#             else:
#                 df.at[index, col] = "Unknown"

#saving the changes back to the excel file
# df.to_excel("Logical_AI_Survey_Responses__45_Participants_.xlsx", index=False)

# Function to analyze user demographics
def analyze_user_demographics(df):
    # Count distributions
    age_counts = df["Age"].value_counts().sort_index() #sorting in ascending order
    gender_counts = df["Gender"].value_counts()
    country_counts = df["Country of Residence"].value_counts().head(10)  # Show top 10
    education_counts = df["Education Level"].value_counts()

    # Print summary statistics
    print("### User Demographics Summary ###\n")
    print("Age Distribution:\n", age_counts, "\n")
    print("Gender Distribution:\n", gender_counts, "\n")
    print("Top 10 Countries:\n", country_counts, "\n")
    print("Education Level Distribution:\n", education_counts, "\n")

    # Visualizations
    plt.figure(figsize=(8, 4))
    age_counts.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.xlabel("Age Group")
    plt.ylabel("Count")
    plt.title("Age Distribution of Participants")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(6, 4))
    gender_counts.plot(kind="bar", color="lightcoral", edgecolor="black")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.title("Gender Distribution of Participants")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 5))
    country_counts.plot(kind="bar", color="lightgreen", edgecolor="black")
    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.title("Top 10 Countries of Participants")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(8, 4))
    education_counts.plot(kind="bar", color="gold", edgecolor="black")
    plt.xlabel("Education Level")
    plt.ylabel("Count")
    plt.title("Education Level Distribution of Participants")
    plt.xticks(rotation=45)
    plt.show()

analyze_user_demographics(df) #runs the analysis function

# Function to analyze AI Chatbot Usage & Frequency
def analyze_chatbot_usage(df):
    # Count distributions
    chatbot_usage_counts = df["Used Chatbot"].value_counts()
    chatbot_types_counts = df["Chatbots Used"].value_counts().drop("Not Applicable", errors='ignore')  # Remove "Not Applicable"
    interaction_frequency_counts = df["AI Interaction Frequency"].value_counts().drop("Not Applicable", errors='ignore')
    ai_motivation_separated_counts = df.explode("AI Motivation")["AI Motivation"].value_counts()

    # Print summary statistics
    print("### AI Chatbot Usage & Frequency Summary ###\n")
    print("Chatbot Usage:\n", chatbot_usage_counts, "\n")
    print("Chatbots Used:\n", chatbot_types_counts, "\n")
    print("AI Interaction Frequency:\n", interaction_frequency_counts, "\n")
    print("AI Motivation Breakdown:\n", ai_motivation_separated_counts, "\n")

    # Visualizations
    plt.figure(figsize=(6, 4))
    chatbot_usage_counts.plot(kind="bar", color="cornflowerblue", edgecolor="black")
    plt.xlabel("Used AI Chatbot")
    plt.ylabel("Count")
    plt.title("AI Chatbot Usage")
    plt.xticks(rotation=0)
    plt.show()

    plt.figure(figsize=(8, 4))
    chatbot_types_counts.plot(kind="bar", color="mediumseagreen", edgecolor="black")
    plt.xlabel("Chatbot Type")
    plt.ylabel("Count")
    plt.title("Chatbots Used")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(8, 4))
    interaction_frequency_counts.plot(kind="bar", color="tomato", edgecolor="black")
    plt.xlabel("Interaction Frequency")
    plt.ylabel("Count")
    plt.title("AI Chatbot Interaction Frequency")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 5))
    ai_motivation_separated_counts.plot(kind="bar", color="royalblue", edgecolor="black")
    plt.xlabel("Motivation for Using AI Chatbots")
    plt.ylabel("Count of Participants")
    plt.title("Separated AI Motivation Distribution")
    plt.xticks(rotation=45)
    plt.show()


analyze_chatbot_usage(df) # Runs the analysis function

