# library manipulation data
import numpy as np
import pandas as pd

# func get_dataset
def get_dataset():
  
  # load dataset
  dataset = pd.read_csv("dataset/vgsales.csv")

  # return values
  return dataset
  # ----------------------------------------------------------------------------------------------------------------------

def time_series(dataset):

  # process aggregation
  df = dataset.groupby(by="Year")["Global_Sales"].aggregate("sum").reset_index()
  
  # rename columns
  df.columns = ["Year", "Sales"]
  
  # return values
  return df
  # ----------------------------------------------------------------------------------------------------------------------

def total_sales(dataset):

  # process aggregation
  df = dataset[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].aggregate("sum").reset_index()
  
  # rename columns
  df.columns = ["Region", "Sales"]
  
  # return values
  return df
  # ----------------------------------------------------------------------------------------------------------------------

def grouping_sales(columns, dataset):

  # process grouping
  df = dataset.groupby(columns)[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].aggregate("sum").reset_index()

  # sorting values
  df = df.sort_values(by=["Global_Sales"], ascending=False)

  # return values
  return df
  # ----------------------------------------------------------------------------------------------------------------------

def unpivot_sales(columns, dataset):

  # process unpivot
  df = pd.melt(
    frame=dataset, id_vars=[columns], var_name='Region', value_name='Sales',
    value_vars=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
  )
  
  # return values
  return df
  # ----------------------------------------------------------------------------------------------------------------------