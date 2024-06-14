import pandas as pd


data = {
    "Product Name" : ["Name1","Name2","Name3"],
    "Product Dmart Price" : ["Price1","Price2","Price3"],
    "Product MRP Price" : ["MRP1","MRP2","MRP3"],
    "Product Image" : ["URL1","URL2","URL3"]
}

df = pd.DataFrame(data)
# df = pd.concat([pd.DataFrame([['Dmart - Grocery Report', '', '', '']], columns=df.columns), df], ignore_index=True)

# Create a DataFrame for the heading row with empty strings for data
heading_row = pd.DataFrame(columns=df.columns)
heading_row.loc[0] = ['Dmart - Grocery Report'] + [''] * (len(df.columns) - 1)

# Concatenate the heading row and the original DataFrame
df = pd.concat([heading_row, df], ignore_index=True)

df.to_excel("Test.xlsx", index=False)

