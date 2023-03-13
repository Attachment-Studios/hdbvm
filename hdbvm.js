class Captcha {
	root = "https://hdbvm.attachment-studios.tk/api";
	element = null;
	id = null;
	value = false;

	constructor() {
		this.construct();
	}

	construct() {
		this.load_element();
		this.load().then(() => {this.build()});
	}

	load_element() {
		let captcha_el = null;
		if (document.getElementsByTagName("captcha").length) {
			captcha_el = document.getElementsByTagName("captcha")[0];
		}
		this.element = captcha_el;
		this.value = false;
	}
	
	async load() {
		await fetch(`${this.root}/new`).then(req => req.json()).then(data => {
			this.id = data["id"];
		}).catch(err => {
			console.log("Captcha Load Unsuccessful.");
			console.log(err);
		});
	}

	build() {
		this.build_template_1();
	}

	build_template_1() {
		let content = `
			<style>
				.captcha-image {
					aspect-ratio: 16/6;
				}

				.captcha-content {
					width: 100%;
					height: 80%;
					padding: 0.25rem;
					margin: 0;
				}

				.captcha-message {
					font-size: 14px;
				}

				.captcha-input {
					display: flex;
					justify-content: space-between;
				}

				.captcha-input input {
					width: 100%;
					margin: 0.25rem;
				}

				.captcha-buttons {
					display: flex;
					justify-content: space-between;
				}

				.captcha-buttons button {
					width: 100%;
					margin: 0.25rem;
				}

				@media (max-width: 479px) {
					captcha {
						width: 100%;
					}
				}
			</style>
			<div id="captcha-image" class="captcha-image">
				<img id="captcha-img" src="${this.root}/img/id/${this.id}" />
			</div>
			<div id="captcha-content" class="captcha-content">
				<div id="captcha-input-box" class="captcha-input">
					<input id="captcha-input" placeholder="captcha by hdbvm" required />
				</div>
				<div id="captcha-buttons" class="captcha-buttons">
					<button type="button" onclick="captcha.submit();">Submit</button>
					<button type="button" onclick="captcha.reload();">Reload</button>
				</div>
				<div id="captcha-message" class="captcha-message"></div>
			</div>
		`;
		this.element.style = `
			display: flex;
			background: white;
			aspect-ratio: 32/7;
			width: 50%;
			border-radius: 0.25rem;
			margin: 0.25rem;
			padding: 0;
			overflow: hidden;
			min-width: 21.5095rem;
		`;
		this.element.innerHTML = content;
	}

	async submit() {
		document.getElementById("captcha-message").innerHTML = "checking...";
		let captcha_value = document.getElementById("captcha-input").value;
		if (captcha_value == "") {
			this.value = false;
			document.getElementById("captcha-input").focus();
			document.getElementById("captcha-message").innerHTML = "Captcha Required!";
			return;
		}
		await fetch(`${this.root}/check/${this.id}/${captcha_value}`).then(req => req.json()).then(data => {
			if (data["exists"] == true) {
				if (data["result"] == true) {
					this.value = true;
					document.getElementById("captcha-content").innerHTML = "Captcha Correct!";
				} else {
					this.value = false;
					document.getElementById("captcha-input").focus();
					document.getElementById("captcha-message").innerHTML = "Captcha Incorrect!";
				}
			} else {
				document.getElementById("captcha-img").src = document.getElementById("captcha-img").src + "?" + new Date().getTime();
				document.getElementById("captcha-message").innerHTML = "Captcha Expired!";
			}
		}).catch(err => {
			console.log("Captcha Load Unsuccessful.");
			console.log(err);
		});
	}

	async reload() {
		document.getElementById("captcha-message").innerHTML = "reloading...";
		await fetch(`${this.root}/renew/${this.id}`).then(req => req.json()).then(data => {
			if (data["exists"] == false) {
				this.construct();
			} else {
				document.getElementById("captcha-img").src = document.getElementById("captcha-img").src + "?" + new Date().getTime();
			}
		}).catch(err => {
			console.log("Captcha Load Unsuccessful.");
			console.log(err);
		});
	}
}

captcha = new Captcha();

