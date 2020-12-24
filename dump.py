###--- CODE-SNIPPET BUILDER ---###

name = input("*** Enter a name for your code-snippet: ")
prefix = input("\n\n*** Enter a prefix for your code-snippet: ")

body = list()
with open('template.txt') as doc:
    for line in doc:
        body.append(line)

code_snippet = dict()

code_snippet[name] = {
    "prefix": name,
    "body": prefix,
}

print(code_snippet)
