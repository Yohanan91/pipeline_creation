# The problem
Imagine you were trying to automate the creation of CI/CD pipelines given some input configuration. The pipelines and all the configurations are yaml.

Your task is to write a script that takes the inputs and converts them into output yaml that contains fully hydrated pipeline configs.

## The inputs are:
_Inputs files are under the `inputs` directory_
1. `pipeline_specs.yml`: A yaml file containing specifications of the pipelines we would like to build. Each entry under the `pipeline_specs` key in this file is a pipeline spec with a pipeline name (`name`) and a repository url (`repo`). Each entry in this file can become one or more entries in the output yaml
2. `branches.yml`: A file containing a list of repositories, each with a list of branches for that repository and a git url for the repo.
3. `pipeline_template.yml`: A template that will be the basis for constructing each entry in the output yaml. Each entry in the output yaml should have the same structure as the template, with the variables replaced.

## Expected output
A file called `pipelines.yml` that contains fully hydrated pipeline configs based on the template and the other inputs described above.


# Rules
1. Each entry in the `pipeline_specs.yml` file under `pipeline_specs` can turn into one ore more entries in the final `pipelines.yml` file.
2. Without any branch filters on the pipeline spec, each (pipeline spec, branch)  combination from `pipeline_specs.yml` and `branches.yml` respectively should map to an entry in the output `pipelines.yml`
3. If there are any branch filters on a pipeline spec (that is if the spec has the `only_for_branches` option specified), only the branches specified in the filter that also exist in the branches file for that repo should have matching pipelines in `pipelines.yml`.
4. All pipeline objects in the output `pipelines.yml` share the same structure, described by `pipeline_template.yml`. The variables in that template (values between `((...))`) are to be replaced with actual values got from the other two input files before being added to the output `pipelines.yml` file.
5. Some steps in the pipeline template should only appear in the output file if the pipeline object branch matches the `only_for_branches` filter. See the  expected output for an example. 

# Ask before you start
If any of the instructions here is not clear, please ask your interviewer for clarification.
