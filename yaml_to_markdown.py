#!/usr/bin/env python

import yaml

problems = {}
md_string = ""

with open('perl6_daily_programmer.yaml', 'r') as file:
    problems = yaml.safe_load(file)

#print(problems)
for problem_id, problem_data in problems.items():
    md_string += "\n\n#[" + problem_data['title'] + "](" + problem_data['url'] + ")"
    if problem_data['solutions']:
        for solution in problem_data['solutions']:
            md_string += "\n\n##" + solution['solution_url']
            md_string += "\n" + solution['solution_body']
    else:
        md_string += "\n\n##No Solutions in Perl6"

with open('perl6_daily_programmer.md', 'w') as file:
    file.write(md_string)