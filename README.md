# captcha-bypass
A tool that automates work using known captcha bypass methods.

## INSTALL

1. git clone
2. pip3 install -r requirements.txt

## Descriptions of Bypass Methods

1. Captcha param None method is success: It can be bypassed by completely deleting the parameter containing the Captcha Token.
2. Captcha param Null method is success: It can be bypassed by leaving the value of the parameter containing the Captcha Token blank.
3. Add Header method is success: bypass by adding X-Forwarded-Host, X-Forwarded-For, X-Originating-IP, X-Remote-IP, X-Remote-Addr, can be done.
4. POST->GET method is potentially success: It can be bypassed by turning the POST method into a GET method. **Manual control may be required!**
5. POST->PUT method is potentially success: It can be bypassed by converting the POST method to the PUT method. **Manual control may be required!**

## Usage

```bash
python3 main.py -u https://target.com/login -r request.txt
```

### Arguments

| Argument        | Description                        | Required |
| --------------- | ---------------------------------- | -------- |
| `-u, --url`     | Target URL                         | Yes      |
| `-r, --request` | Raw HTTP request file (txt format) | Yes      |
| `-t, --token`   | Captcha token parameter name       | No       |
| `-e, --error`   | Captcha error string to check      | No       |

### Example request.txt

The request file should be in raw HTTP format. You can capture this from Burp Suite or browser developer tools.

```http
POST /login HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0
Content-Type: application/x-www-form-urlencoded
Accept: */*

username=admin&password=test&captcha=TOKEN
```

> **Note:** The tool automatically detects the captcha parameter from common names like `captcha`, `g-recaptcha-response`, `verification_code`, etc. Use `-t` flag only if your captcha parameter has a custom name.


