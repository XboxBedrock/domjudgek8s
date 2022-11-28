fields = [("replicas", "The amount of instances you want to run, perhaps one per 500mb of ram (int): "), 
          ("server", "The url of the instance, such as https://calicojudge.com/ (str): "), 
          ("username", "The username of the judgeinstance login (str): "), 
          ("password", "The password of the judgeinstance login (str): ")]

with open("templates/template.yml", "r") as template:
    total = ''.join(template.readlines())
    for k,v in fields:
        val = input(v)
        total = total.replace('{{'+k+'}}', val)
    with open("domjudge.yml", "w") as write_template:
        write_template.write(total)