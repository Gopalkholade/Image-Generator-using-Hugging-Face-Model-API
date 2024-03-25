import requests
from PIL import Image
from io import BytesIO

def generator(prompt=None, save_path="./", authorization_token=None ):
    if authorization_token !=None and len(prompt)>=5:
        API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
        b = requests.post(API_URL,
                        headers = {"Authorization": f"Bearer {authorization_token}"},
                        json={"inputs":str(prompt)})

        i = Image.open(BytesIO(b.content))
        i.save(f"{save_path}"+"image.png")

if __name__=="__main__":
    generator(prompt="Sheep with violin",authorization_token="<Your_token>")