###--- IMPORTS ---###
import json
import settings
import os


###--- GLOBAL VARIABLES ---###
path_to_vsc_codesnippets = settings.CODE_SNIPPET_PATH


###--- CODE-SNIPPET BUILDER ---###

def create_codesnippet():
    # [!] optional: accetps input
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

    # print(type(code_snippet))  # dict
    # print(code_snippet)

    snippet_as_json = json.dumps(code_snippet, indent=4)
    # print(type(snippet_as_json))  # str

    with open(os.path.join(path_to_vsc_codesnippets, f"{name}.code-snippets"), "w") as final_snippet:
        final_snippet.write(snippet_as_json)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    create_codesnippet()
