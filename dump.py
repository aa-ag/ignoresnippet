###--- IMPORTS ---###
import json

###--- CODE-SNIPPET BUILDER ---###

# [!] optiona: accetps input
# name = input("*** Enter a name for your code-snippet: ")
# prefix = input("\n*** Enter a prefix for your code-snippet: ")
name = "gitignore"
prefix = "ignore"
description = "A gitignore template for Python projects."

body = list()
with open('template.txt') as doc:
    for line in doc:
        body.append(line.replace('\n', ''))

code_snippet = dict()

code_snippet[name] = {
    "prefix": prefix,
    "body": body,
    "description": description,
}

print(type(code_snippet))  # dict
# print(code_snippet)

snippet_as_json = json.dumps(code_snippet, indent=4)
print(type(snippet_as_json))  # str
print(snippet_as_json)

# TO DO: set as .code-snippets on VSC
