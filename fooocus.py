import numpy as np
import os
import requests
import json
import base64
import time
from PIL import Image as im

def host_url(pod_id):
    return f"https://{pod_id}-8888.proxy.runpod.net"

def focus_endpoint(image_url,mask_url,pod_id):

    params={
            "prompt": "perfect teeth, shiny teeth,veneer teeth, super white teeth, perfect shape of teeth",
            "negative_prompt" : "imperfect teeth",
            "style_selections":["Fooocus V2,Fooocus Enhance,Fooocus Sharp, Fooocus Negative"],
            "require_base64":True,
            "async_process": False,
            "input_image" : image_url,
            "input_mask" : mask_url,
            "image_prompts" : [],
            }
    response = requests.post(url=f"{host_url(pod_id)}/v2/generation/image-prompt",
                        data=json.dumps(params),
                        # files=filesjson,
                        )
    result = response.json()
    base = result[0]['base64']
    return base
    # image_data = base64.b64decode(base)
    # filename = secure_filename(file.filename)
    # file_extension = "png"
    # unique_filename = f"result-{int(time.time())}.{file_extension}"
    # temp_path = os.path.join("processed_image", unique_filename)
    # with open(unique_filename,"wb") as f:
    #     f.write(image_data)
    # # image2 = im.open(unique_filename)
    # return unique_filename

# print(focus_endpoint("https://teethe.s3.ap-south-1.amazonaws.com/image_1708207213_9AHcEBev.png","https://teethe.s3.ap-south-1.amazonaws.com/image_1708207222_Nam4eFsu.png","a3juid7agss9ns"))

   