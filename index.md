<title>HDBVM</title>
<style>
	@media print{blockquote,img,pre,tr{page-break-inside:avoid}*,:after,:before{background:0 0!important;color:#fff!important;box-shadow:none!important;text-shadow:none!important}a,a:visited{text-decoration:underline}a[href]:after{content:" (" attr(href) ")"}abbr[title]:after{content:" (" attr(title) ")"}a[href^="#"]:after,a[href^="javascript:"]:after{content:""}blockquote,pre{border:1px solid #666}thead{display:table-header-group}img{max-width:100%!important}h2,h3,p{orphans:3;widows:3}h2,h3{page-break-after:avoid}}canvas,html,iframe,img,select,svg,textarea,video{max-width:100%}code,pre{font-family:Menlo,Monaco,"Courier New",monospace;background-color:#060606}pre{padding:.5rem;line-height:1.25;overflow-x:scroll}a,a:visited{color:#3498db}a:active,a:focus,a:hover{color:#2980b9}.modest-no-decoration,a{text-decoration:none}@media screen and (min-width:32rem) and (max-width:48rem){html{font-size:15px}}@media screen and (min-width:48rem){html{font-size:16px}}.modest-p,p{font-size:1rem;margin-bottom:1.3rem}.modest-h1,.modest-h2,.modest-h3,.modest-h4,h1,h2,h3,h4{margin:1.414rem 0 .5rem;font-weight:inherit;line-height:1.42}.modest-h1,h1{margin-top:0;font-size:3.998rem}.modest-h2,h2{font-size:2.827rem}.modest-h3,h3{font-size:1.999rem}.modest-h4,h4{font-size:1.414rem}.modest-h5,h5{font-size:1.121rem}.modest-h6,h6{font-size:.88rem}.modest-small,small{font-size:.707em}html{background:#1f1f1f;font-size:18px}body{color:#ccc;font-family:'Open Sans Condensed',sans-serif;font-weight:300;margin:0 auto;max-width:48rem;line-height:1.45;padding:.25rem}h1,h2,h3,h4,h5,h6{font-family:Arimo,Helvetica,sans-serif}h1,h2{border-bottom:0.5px solid #fafafa77;margin-bottom:1.15rem;padding-bottom:.5rem;text-align:center}blockquote{border-left:8px solid #060606;padding:1rem}:not(pre)>code{color:red}a:hover{text-decoration:underline}*{outline:none}
</style>

# <a id="top" href="#top">HDBVM</a>
<center><img src="/api/img/value/HDBVM" width="100%" height="auto" alt="HDBVM"></center><br>
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

## <a id="make-a-captcha" href="#make-captcha">Make a CAPTCHA</a>
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

## <a id="rener-captcha" href="#renew-captcha">Renew a CAPTCHA</a>
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
<center><img src="/icon" width="25%" height="auto" alt="HDBVM"></center>

