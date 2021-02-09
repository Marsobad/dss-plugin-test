from dataikuapi.dss.recipe import SingleOutputRecipeCreator


class CustomRecipeCreator(SingleOutputRecipeCreator):
    def ___init__(self,type, name, project, plugin_id):
        SingleOutputRecipeCreator.__init__(self, type, name, project)
        self.new_input = None
        self.new_output = None
        self.input_role = None
        self.output_role = None

    def with_input(self, dataset_name, project_key=None, role="main"):
        self.new_input = dataset_name
        self.input_role = role
        return self._with_input(dataset_name, project_key, role)

    def with_output(self, dataset_name, append=False, role="main"):
        self.new_output = dataset_name
        self.output_role = role
        return self._with_output(dataset_name, append, role)

    def get_recipe_status(self):
        for recipe_ref in self.project.list_recipes():
            recipe_name = recipe_ref.get("name")
            recipe = self.project.get_recipe(recipe_name)
            settings = recipe.get_settings()
            if recipe.get_settings().type == self.recipe_proto["type"]:
                # get recipe role (role) from custom recipe settings --> new object custom recipe
                custom_recipe_input = settings.get_recipe_inputs().get(self.input_role).get("items")[0].get("ref")
                custom_recipe_output = settings.get_recipe_outputs().get(self.output_role).get("items")[0].get("ref")

                if custom_recipe_input and custom_recipe_output:
                    if custom_recipe_output == self.new_output and custom_recipe_input == self.new_input:
                        return "ALREADY_EXISTS"
                    elif custom_recipe_output == self.new_output:
                        return "WRONG_OUTPUT"
        return "NEW"

    def set_parameter(self,new_parameter, parameter_name):
        recipe = self.project.get_recipe(self.recipe_proto["name"])
        recipe_settings = recipe.get_settings()
        recipe_settings.data['recipe']['params']['customConfig'][parameter_name] = new_parameter
        recipe_settings.save()



