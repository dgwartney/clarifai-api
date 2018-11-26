#!/usr/bin/env python      
from clarifai.rest import ClarifaiApp
import os
import sys
import json

if len(sys.argv) != 2:
    print('usage: {0}'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)
else:
    url = sys.argv[1]

api_key = os.environ['CLARIFAI_API_KEY']
app = ClarifaiApp(api_key=api_key)
      
# get the general model
model = app.models.get("general-v1.3")
      
# predict with the model
# result = model.predict_by_url(url=url)
result = model.predict_by_url(url=url)
print(json.dumps(result))
