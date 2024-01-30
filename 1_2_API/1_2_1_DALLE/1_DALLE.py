from openai import OpenAI
client = OpenAI()

prompt = input("Prompt: ")

response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  size="1024x1024",
  quality="hd",
  n=1,
  style="natural"
)

image_url = response.data[0].url
print(image_url)