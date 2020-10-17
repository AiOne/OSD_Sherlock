# import qrcode
# from colorama import Style, Fore, init


# class QR_Converter():
#     def __init__(self, file_path, username, websiteInfo, **kwargs):
#         self.file_path = file_path
#         self.username   = username
#         # self.link = link
#         self.websiteInfo = websiteInfo

#         init(autoreset=True)

    

#     def convert_qr(self):
#         for info in self.websiteInfo: 
#             # print(info[0]['site_name'])
#             qr_img = qrcode.make(info[0]['url'])
         
#             print((
#             Style.BRIGHT + Fore.YELLOW + "<[" + 
#             Fore.GREEN + "saving QR code for" + Fore.BLUE+ " (" +self.username + ") " 
#             + Fore.GREEN + "in " + Fore.CYAN + info[0]['site_name'] + Fore.YELLOW + " ]>"))
#             qr_img.save(self.username + "/" +str(self.username+"_"+info[0]['site_name']+".png"))




