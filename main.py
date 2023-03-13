import secrets
import uuid
import logging
import string
import io

from flask import Flask, jsonify, send_file, Response
from flask_cors import CORS
from captcha.image import ImageCaptcha
from markdown import markdown
from deta import Deta

def random_text(length: int = 4) -> str:
	alphabets = string.ascii_letters + string.digits
	text = "".join(secrets.choice(alphabets) for i in range(int(length)))
	return text

def response(content: str) -> Response:
	resp = content if isinstance(content, Response) else Response(content)
	resp.headers.add("Access-Control-Allow-Origin", "*")
	resp.headers.add("Referrer-Policy", "no-referrer")
	return resp

image_captcha = ImageCaptcha(400, 150, font_sizes=(105, 125, 140))

deta = Deta("c0JDpq54AxNw_GYLzK9oVP7Mh5ZSNoXzMzdsmUsuLHDp1")
data = deta.Base("data")
drive = deta.Drive("CAPTCHA")

def emergency_call():
	drive.delete_many(drive.list()["names"])

logging.getLogger("werkzeug").setLevel(logging.ERROR)

app = Flask("HDBVM")
CORS(app)

@app.route("/")
def home():
	with open("index.md", "r") as readme_file:
		css = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css"
		js = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"
		head = f"""
			<head>
				<link rel="icon" href="/icon">
				<!--link rel="stylesheet" href="{css}"-->
				<!--script src="{js}"></script-->
			</head>
		"""

		return response(head + markdown(
			readme_file.read(), extensions=["fenced_code"]
		))

@app.route("/api")
def api():
	with open("index.html", "r") as home_file:
		return response(home_file.read())

@app.route("/api/js")
def api_js():
	with open("hdbvm.js", "r") as js_file:
		return response(js_file.read())

@app.route("/api/new")
@app.route("/api/new/length/<length>")
@app.route("/api/new/value/<captcha_value>")
def api_new(length: int = 4, captcha_value: str = None):
	key = uuid.uuid4().hex
	value = captcha_value or random_text(length if int(length) > 0 else 4)
	image_data = image_captcha.generate(value)

	data.put({"value": value}, key, expire_in=900)
	drive.put(f"{key}.png", image_data)

	return response(jsonify({
		"id": key
	}))

@app.route("/api/img")
@app.route("/api/img/id/<captcha_id>")
@app.route("/api/img/length/<length>")
@app.route("/api/img/value/<captcha_value>")
def api_img(captcha_id: str = None, length: int = 4, captcha_value: str = None):
	key = captcha_id or uuid.uuid4().hex
	value = captcha_value or random_text(length if int(length) > 0 else 4)
	image_data = None

	if captcha_id:
		captcha_file = drive.get(f"{captcha_id}.png")
		if captcha_file:
			image_data = io.BytesIO(captcha_file.read())
		else:
			image_data = image_captcha.generate(value)
	else:
		image_data = image_captcha.generate(value)

	return send_file(
		image_data,
		mimetype="image/png",
		as_attachment=False,
		download_name=f"{key}.png"
	)

@app.route("/api/check/<captcha_id>/<input_data>")
def api_check(captcha_id: str = None, input_data: str = None):
	captcha_data = data.get(captcha_id if captcha_id else "invalid data")
	if not captcha_data:
		return jsonify({
			"id": captcha_id,
			"exists": False,
			"result": False
		})
	
	if captcha_data["value"] == input_data:
		drive.delete(f"{captcha_id}.png")
		data.delete(captcha_id)
	
	return response(jsonify({
		"id": captcha_id,
		"exists": True,
		"result": captcha_data["value"] == input_data
	}))

@app.route("/api/renew/img/<captcha_id>")
def api_renew_img(captcha_id: str = None):
	captcha_data = data.get(captcha_id if captcha_id else "invalid data")
	if not captcha_data:
		return jsonify({
			"id": captcha_id,
			"result": False
		})
	
	image_data = image_captcha.generate(captcha_data["value"])
	drive.put(f"{captcha_id}.png", image_data)

	return response(jsonify({
		"id": captcha_id,
		"result": True
	}))

@app.route("/api/renew/<captcha_id>")
def api_renew(captcha_id: str = None):
	captcha_data = data.get(captcha_id if captcha_id else "invalid data")
	if not captcha_data:
		return jsonify({
			"id": captcha_id,
			"result": False
		})
	
	value = random_text(len(captcha_data["value"]))
	data.put({"value": value}, captcha_id, expire_in=900)
	image_data = image_captcha.generate(value)
	drive.put(f"{captcha_id}.png", image_data)

	return response(jsonify({
		"id": captcha_id,
		"result": True
	}))

@app.route("/icon")
def icon():
	return response(send_file(
		"icon.png",
		mimetype="image/png",
		as_attachment=False,
		download_name="icon.png"
	))

@app.errorhandler(404)
@app.errorhandler(403)
@app.errorhandler(500)
def error(*_, **__):
	return ":/\nYou messed up\nSee <a href='/'>docs</a>."

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)

