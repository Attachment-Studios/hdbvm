---
title: "HDBVM"
tagline: "Easy Human Distinction By Visual Method API, in short - CAPTCHA API"
theme_color: "#2980b9"
git: "https://github.com/Attachment-Studios/hdbvm"
homepage: "https://hdbvm.attachment-studios.tk"
---

# <a id="top" href="#top">HDBVM</a>
<center><img src="https://hdbvm.attachment-studios.tk/api/img/value/HDBVM" width="100%" height="auto" alt="HDBVM"></center><br>
It stands for `Human Distinction By Visual Medthod`, in other words, a `captcha` api.

# <a id="features" href="#features">What HDBVM can do?</a>
- Create captcha images.
	- Randomly generated
	- Randomly generated but given length
	- Given value
- Store captcha images temporarily(15 minutes).
- Verify generated captcha with given input.

# <a id="docs" href="#docs">API Docs</a>

## <a id="make-captcha-images" href="#make-captcha-images">Make a CAPTCHA image</a>
You can make a captcha image without making a completely functional captcha, just the image. To do so you have a few options.

### <a id="random-image" href="#random-image">Random Image</a>
Just use - `/api/img`. This gets a random captcha every time, 4 characters long.

### <a id="random-image-given-length" href="#random-image-given-length">Random Image from given length</a>
Just use - `/api/img/length/<length>`. This gets a random captcha every time, with given amount of characters.

### <a id="image-from-given-value" href="#image-from-given-value">Image from given value</a>
Just use - `/api/img/value/<value>`. This gets a captcha with given value. The image might be different each time however.

### <a id="image-from-existing-captcha" href="#image-from-existing-captcha">Image from existing captcha</a>
Just use - `/api/img/id/<id>`. This gets the exact same captcha unless captcha was renewed or captcha was succesfully passed. This just fetches one if it exists. To make one you need to create a captcha.

## <a id="make-a-captcha" href="#make-a-captcha">Make a CAPTCHA</a>
To make a captcha, call the url - `/api/new`. This will return you a `JSON` with content including ID of the captcha.
```json
{
	"id": <captcha id here>
}
```

### <a id="make-random" href="#make-random">Randomly Generated CAPTCHA</a>
To generate a random captcha, nothing extra is required in the url - `/api/new`. This returns a captcha with 4 characters.

### <a id="make-random-given-length" href="#make-random-given-length">Randomly Generated CAPTCHA given the length</a>
To generate a random captcha with given amount of characters, just add `length` property - `/api/new/length/<length>`.

### <a id="make-from-given-value" href="#make-from-given-value">CAPTCHA from given value</a>
To generate a captcha with given value, just add `value` property - `/api/new/value/<value>`.

## <a id="match-captcha" href="#match-captcha">Match CAPTCHA with value</a>
To match values you need to have id of a captcha and a value you want to check. Then use - `/api/check/<id>/<value>` to get a `JSON` with data. If id captcha is `expired/invalid`, result will always be false.
```json
{
	"id": <id>,
	"exists": <if the id is valid - true>,
	"result": <if the value is correct - true>
}
```

## <a id="renew-captcha" href="#renew-captcha">Renew a CAPTCHA</a>
A captcha can be renewed if it has not expired. However from this, image will always change. The value might be changed if wanted. The id for the captcha can be used for 15 minutes more. Both cases will return a similar `JSON`. Result will only bee true if captcha is valid and the process was successful.
```json
{
	"id": <captcha id here>,
	"result": <if captcha was renewed - true>
}
```

### <a id="renew-entire-captcha" href="#renew-entire-captcha">Renew the value and image</a>
To renew both captcha and image, use - `/api/renew/<id>`.

### <a id="renew-captcha-image" href="#renew-captcha-image">Renew the image only</a>
To renew the captcha image only, use - `/api/renew/img/<id>`.

# <a id="icon" href="#icon">Our icon</a>
To get our icon, if you wish so, use `/icon`.<br>
<center><img src="https://hdbvm.attachment-studios.tk/icon" width="25%" height="auto" alt="HDBVM"></center>

