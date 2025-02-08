from openai import OpenAI

client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")

response = client.audio.speech.create(
    model="ds-tts-1", #model="deepseek-chat",
    voice="victoria",
    input="Hello world! This is a streaming test."
)
response.stream_to_file("output.mp3")
