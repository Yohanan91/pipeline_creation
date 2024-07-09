class Pipeline:

    def __init__(self, branches, pipeline, template):
        self.branches = branches
        self.pipeline = pipeline["pipeline_specs"]
        self.template = template

    ## group url, branch and repo name together
    def name(self, repo_name, repo_branch, url):
        pair = []
        for item in repo_branch:
            if repo_name == "pipeline-2" and item == "main":
                pair.append([url, repo_name, item])
            elif repo_name == "pipeline-1":
                pair.append([url, repo_name, item])
            else:
                pass
        return pair

    def branch_check(self):
        good_list = []
        for items in self.branches:
            for item in self.pipeline:
                if item["repo"] == items["url"]:
                    good_list += self.name(item["name"], items["branches"], item["repo"])
        return good_list

    def template_list(self):
        final_list = []
        for items in self.branch_check():
            if items[2] == "main":
                final_list.append({"pipeline": items[1] + "/" + items[2], "steps": [{"checkout": items[0], "branch": items[2]}, {"run": "make test"}, {"run": "deploy"}]})
            else:
                final_list.append({"pipeline": items[1] + "/" + items[2], "steps": [{"checkout": items[0], "branch": items[2]}, {"run": "make test"}]})

        return final_list
