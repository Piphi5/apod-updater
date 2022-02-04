import jinja2
import json
import sys
import requests

key = sys.argv[1]
response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key}")

desired_cols = ["copyright", "url"]

if response:
  raw_data = json.loads(response.text)
  data = {k: v for k, v in raw_data.items() if k in desired_cols}
  subs = jinja2.Environment( 
              loader=jinja2.FileSystemLoader('./')      
              ).get_template('template.jinja').render(**data)
  # lets write the substitution to a file
  with open("apod-displayer/index.html",'w') as f:
    f.write(subs)
  
