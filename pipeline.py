class Pipeline:

    def __init__(self, branches, pipeline, template):
        self.branches = branches
        self.pipeline = pipeline["pipeline_specs"]
        self.template = template

    ## group url, branch and repo name together
    def name(self, repo_name, repo_branch, url, only_branch=None):
        pair = []
        for i in repo_branch:
            pair.append([url, repo_name, i])
        return pair

    def branch_check(self):
        good_list = []
        for items in self.branches:
            for item in self.pipeline:
                if item["repo"] == items["url"] and item.get("only_for_branches") == None:
                    good_list += self.name(item["name"], items["branches"], item["repo"])
        return good_list

    def only_branch(self):
        good_list = []
        ## check if the pipeline spec has the key only_for_branches
        for items in self.branches:
            for item in self.pipeline:
                if item["repo"] == items["url"]:
                    for key, values in item.items():
                        if key == "only_for_branches":
                            good_list += self.name(item["name"], values, item["repo"])

        return good_list

    def create_pipeline(self):
        final_list = []
        for items in self.branch_check():
            steps = [{"checkout": items[0], "branch": items[2]}, {"run": "make test"}]
            final_list.append({
                'pipeline': f"{items[1]}/{items[2]}",
                'steps': steps
            })
        for items in self.only_branch():
            steps = [{"checkout": items[0], "branch": items[2]}, {"run": "make test"}, {"run": "deploy"}]
            final_list.append({
                'pipeline': f"{items[1]}/{items[2]}",
                'steps': steps
            })
        return final_list
