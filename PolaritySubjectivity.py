import pandas as pd

input_file = "Output Data Structure.csv"
df = pd.read_csv(input_file)

df["NEGATIVE SCORE"]=-df["NEGATIVE SCORE"]
df["POLARITY SCORE"] = (df["POSITIVE SCORE"] - df["NEGATIVE SCORE"]) / (df["POSITIVE SCORE"] + df["NEGATIVE SCORE"])
df["SUBJECTIVITY SCORE"] = (df["POSITIVE SCORE"] + df["NEGATIVE SCORE"]) / (df["WORD COUNT"])

df.to_csv(input_file, index=False)
