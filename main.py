# Created By Vxi#0208
# FYI May Show Error "Import "qrcode" could not be resolved" Just Leave It! It Will Work
# pip install qrcode

import qrcode # To Create QR Code!
import os # To Clear Console!

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def main():
    url = input("Please Type The URL You Want To Turn Into A QR Code: ")
    img = qrcode.make(url)
    img.show()
    print("Complete!")
    clear()
    main()
clear()
main()