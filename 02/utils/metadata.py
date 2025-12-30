def get_meta_data(df):
    print("Columns:\n\n", df.columns.tolist())
    df = df.copy()
    df.columns = df.columns.str.strip()
    count_row = df.shape[0]
    count_col = df.shape[1]
    df["century"] = df["century"].astype(str)
    print(f"\nAmount of rows:\t {count_row}\nAmount of cols:\t {count_col}\n")
    if "File" in df.columns:
        #print(f"Unique Files:"+ len(df["File"].unique()) +"\n")
        print(f"Unique Files: {len(df['File'].unique())}\n")
    else:
        print("Col 'File' does not exist.")
    display(df.head())
    return df