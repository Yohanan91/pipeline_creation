import yaml
import yamlloader
import pipeline


with open("branches.yml") as file:
    branch_list = yaml.load(file, Loader=yaml.FullLoader)
with open("pipeline_specs.yml") as file:
    pipeline_specs = yaml.load(file, Loader=yaml.FullLoader)
with open("pipeline_template.yml") as file:
    pipeline_template = yaml.load(file, Loader=yaml.FullLoader)

pim = pipeline.Pipeline(branch_list, pipeline_specs, pipeline_template)

output_file = pim.template_list()

with open("output.yaml", "w") as file:
    documents = yaml.dump(output_file, file, sort_keys=False, default_flow_style=False)




