import dataiku
from dataiku.customrecipe import *
input_A_names = get_input_names_for_role('input_A_role')
input_A_datasets = dataiku.Dataset(input_A_names[0]) 

# For outputs, the process is the same:
output_A_names = get_output_names_for_role('main_output')
output_A_datasets = dataiku.Dataset(output_A_names[0])
my_variable = get_recipe_config().get('parameter1')

# Read recipe inputs
input_df = input_A_datasets.get_dataframe()
output_df = input_df

# Write recipe outputs
output_A_datasets.write_with_schema(output_df)
