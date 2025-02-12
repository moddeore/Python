link = input("Enter the link of content you have to made a QR code : ")
import qrcode as qr
img = qr.make(link)
img.save("QR_code")
img.show()