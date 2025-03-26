import pandas as pd
import argparse
import matplotlib.pyplot as plt
import seaborn as sns

def merge_and_refine(forms_file, responses_file, output_file):
    # Load the CSV files
    forms_df = pd.read_csv(forms_file)
    responses_df = pd.read_csv(responses_file)
    
    # Merge the forms with responses on sessionId, keeping only matching entries
    merged_df = forms_df.merge(responses_df, on="sessionId", how="inner")
    
    # Save the cleaned merged dataset
    merged_df.to_csv(output_file, index=False)
    print(f"Merged and refined data saved to: {output_file}")
    
    return merged_df

def visualize_data(df):
    # Set style
    sns.set_style("whitegrid")
    
    # Histogram of Age Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df['age'], bins=20, kde=True, color='blue')
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()
    
    # Gender Count
    plt.figure(figsize=(6, 4))
    sns.countplot(x='genre', data=df, palette='coolwarm')
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.show()
    
    # Education Level Distribution
    plt.figure(figsize=(10, 5))
    sns.countplot(y='niveauEtudes', data=df, order=df['niveauEtudes'].value_counts().index, palette='viridis')
    plt.title("Education Level Distribution")
    plt.xlabel("Count")
    plt.ylabel("Education Level")
    plt.show()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge and refine CSV files.")
    parser.add_argument("forms_file", help="Path to the forms CSV file.")
    parser.add_argument("responses_file", help="Path to the responses CSV file.")
    parser.add_argument("output_file", help="Path to save the merged and refined CSV file.")
    
    args = parser.parse_args()
    
    merged_df = merge_and_refine(args.forms_file, args.responses_file, args.output_file)
    visualize_data(merged_df)