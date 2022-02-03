from flask import Flask, send_file
from os import listdir as l

app = Flask(__name__)

l = [g for g in l() if g.endswith(".pdf")]

@app.route('/')
def page():
    content = ""
    for pdf in l:
        content += f'<a href="{pdf}"><h3>{pdf[:-4]}</h3></a>\n'
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	{content}
</body>
</html>'''
    return html

@app.route(f"/<file>")
def comic(file):
	return send_file(file)

app.run(host='10.1.52.10', port=5000, debug=True)