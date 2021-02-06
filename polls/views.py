from django.shortcuts import render


def profiling(project_id):
    """
        Functions does profiling on the data
    """
    print(project_id)
    df = pd.read_csv('/home/ubuntu/deduper/Project_1.csv')
    df_cols = pd.DataFrame(df.isnull().sum())
    df_cols['Data_Type'] = df.dtypes.to_frame('dtypes')
    df_cols = df_cols.replace({'Data_Type': "object"}, {'Data_Type': 'string'}, regex=False)
    df_cols = df_cols.rename(columns={0: "Null_Count"})
    df_cols['Percentage_Of_Nulls'] = df_cols["Null_Count"]*100/df.shape[0]
    df_cols['Min_Value'] = df.min(numeric_only=True)
    df_cols['Max_Value'] = df.max(numeric_only=True)
    df_cols['Distinct_Count'] = pd.DataFrame(df.nunique())
    df_cols['Distinct_Count%'] = df_cols["Distinct_Count"]*100/df.shape[0]
    df_cols['Total_Count'] = df.count()
    df_cols = df_cols.reset_index()
    df_cols = df_cols.rename(columns={"index": "Column_Name"})
    df_cols = df_cols.fillna(0)
    df_cols = df_cols.to_json(orient="records")
    return df_cols
