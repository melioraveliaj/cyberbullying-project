import pandas as pd

tweets_data = pd.read_csv("cyberbullying_tweets.csv")

# Removing tweets with conflicting labels and duplicate tweets
conflicting_labels = tweets_data.groupby("tweet_text")["cyberbullying_type"].nunique()
conflicting_tweets = conflicting_labels[conflicting_labels > 1].index.tolist()
tweets_data_clean = tweets_data[~tweets_data["tweet_text"].isin(conflicting_tweets)]
tweets_data_clean = tweets_data_clean

# Create cyberbullying and non-cyberbullying datasets
tweets_data_clean = tweets_data_clean.copy()
tweets_data_clean["label"] = (tweets_data_clean["cyberbullying_type"] != "not_cyberbullying").astype(int)

# Save the cleaned dataset to a new CSV file
tweets_data_clean.to_csv("cleaned_cyberbullying_tweets.csv", index=False)
