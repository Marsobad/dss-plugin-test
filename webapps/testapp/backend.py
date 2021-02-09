from dataiku.customwebapp import *

# Access the parameters that end-users filled in using webapp config
# For example, for a parameter called "input_dataset"
# input_dataset = get_webapp_config()["input_dataset"]

import dataiku
from flask import request
from dataikuapi.dss.recipe import DSSRecipeCreator
from test.custom_recipe_creator import CustomRecipeCreator

project_key = dataiku.default_project_key()
client = dataiku.api_client()
project = client.get_project(project_key)

@app.route('/post_parameter',methods=['POST'])
def create_recipe():
    data = request.form
    new_parameter = data.get("parameter")

    new_input = get_webapp_config()["input_dataset"]
    new_output = get_webapp_config()["output_dataset"]
    new_recipe_name = "compute_{}".format(new_output)

    builder = CustomRecipeCreator('CustomCode_plugin', new_recipe_name, project)
    builder = builder.with_input(new_input, role="input_A_role")
    builder = builder.with_output(new_output, role="main_output")

    recipe_status = builder.get_recipe_status()
    if recipe_status == "NEW":
        builder.create()
        builder.set_parameter(new_parameter, "parameter1")
        status = "created"
    elif recipe_status == "ALREADY_EXISTS":
        status = "updated"
        builder.set_parameter(new_parameter, "parameter1")
    elif recipe_status == "WRONG_OUTPUT":
        error = "The dataset {output} is already the output of the recipe {recipe_name}".format(output=new_output,
                                                                                                recipe_name=new_recipe_name)
        return json.dumps({"status": "error", "data": new_recipe_name, "error": error})

    return json.dumps({"status": status, "data": new_recipe_name})


