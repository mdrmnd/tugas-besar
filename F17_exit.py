from F16_save import save

def exit(nama):
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    pil_exit = input()
    if pil_exit == "Y" or pil_exit == "y" :
        save()
    elif pil_exit == "N" or pil_exit == "n":
        print(f"Data terbaru tidak tersimpan dalam file.\n\nSampai jumpa {nama}")
    else : #jika input != Y, y, n, atau N
        exit()
    return


