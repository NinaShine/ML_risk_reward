import pandas as pd
import argparse

def merge_and_refine(forms_file, responses_file, output_file):
    # Load the CSV files
    forms_df = pd.read_csv(forms_file)
    responses_df = pd.read_csv(responses_file)
    
    # Merge the forms with responses on sessionId, keeping only matching entries
    merged_df = forms_df.merge(responses_df, on="sessionId", how="inner")
    
    # Save the cleaned merged dataset
    merged_df.to_csv(output_file, index=False)
    print(f"Merged and refined data saved to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge and refine CSV files.")
    parser.add_argument("forms_file", help="Path to the forms CSV file.")
    parser.add_argument("responses_file", help="Path to the responses CSV file.")
    parser.add_argument("output_file", help="Path to save the merged and refined CSV file.")
    
    args = parser.parse_args()
    
    merge_and_refine(args.forms_file, args.responses_file, args.output_file)