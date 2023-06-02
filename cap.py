from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 300, height = 100)
captcha_text = input("Please enter text: ")
data = image.generate(captcha_text)
image.write(captcha_text, (captcha_text) + ".png")

