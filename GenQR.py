import qrcode   


print("\n***** QR Generrator *****\n")
data = input("Enter Message or URL:")
imgName = input("Enter Image Name To Save:")
qrimg = qrcode.make(data)
qrimg.save(imgName+".png")
print("\nQR Code Generrated")