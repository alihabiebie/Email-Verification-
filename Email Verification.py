try:
    email = input("Masukkan Alamat Email Anda: ")
    user1 = email.split("@")
    user01 = user1[0]
    user = user01.replace("_", "").replace(".", "")
    hosting11 = user1[1]
    hosting1 = hosting11.split(".")
    hosting = hosting1[0]
    ekstensi = hosting1[1]
    def alamatEmail(email):
        if user.isalnum() != True: 
            return "Format Username Salah"
        elif hosting.isalnum() != True:
            return "Format Hosting Salah"
        elif ekstensi.isalpha() != True | len(ekstensi) > 5:
            return "Format Ekstensi Salah"
        else:
            return "Alamat Email yang anda masukkan Valid !"
    print(alamatEmail(email))
except:
    print("Format Email salah")