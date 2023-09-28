from flask import Flask, render_template
import aiohttp

app = Flask(__name__)
ENDPOINT = "https://api.breakingbadquotes.xyz/v1/quotes"

@app.route('/')
async def index():
    async with aiohttp.ClientSession() as session:
        req = await session.get(ENDPOINT)
        data = await req.json()

    quote = data[0]["quote"]
    author = data[0]["author"]
    return render_template("/template.html", quote=quote, author=author)


app.run(host='0.0.0.0', port=81)
