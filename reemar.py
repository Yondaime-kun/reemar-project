#!/usr/bin/python
# Author ? gada bosque
# Cuma percobaan wkwk nanti di banyakin dah biar agak kerenan dikit awokawok
# yang terpenting adalah:
#     ___  ____  _____ _   _ ____   ___  _   _ ____   ____ _____
#    / _ \|  _ \| ____| \ | / ___| / _ \| | | |  _ \ / ___| ____|
#   | | | | |_) |  _| |  \| \___ \| | | | | | | |_) | |   |  _|
#   | |_| |  __/| |___| |\  |___) | |_| | |_| |  _ <| |___| |___
#    \___/|_|   |_____|_| \_|____/ \___/ \___/|_| \_\\____|_____|



# Apa yang baru:
#   1. Perubahan Algoritma Pencocokan Data
#   2. Penambahan "github Searcher"
#   3. Penambahan Bot Chat Dari Simi
#


import os
try:
    import time
    import random
    import re
    import json
    import requests

except ImportError:
    os.system("pip install requests")

# -----[ Color ]-----
m = '\x1b[1;31m'
p = '\x1b[1;37m'
# -------------------

# ----------[ Banner ]----------
banner = f'''
{m}╦═╗{p}┌─┐┌─┐┌┬┐┌─┐┬─┐
{m}╠╦╝{p}├┤ ├┤ │││├─┤├┬┘
{m}╩╚═{p}└─┘└─┘┴ ┴┴ ┴┴└─
  {m}╔═╗{p}┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐
  {m}╠═╝{p}├┬┘│ │ │├┤ │   │
  {m}╩  {p}┴└─└─┘└┘└─┘└─┘ ┴ '''

###-------------------------[ Array Data ]-------------------------###
bantuan = ['reemar -help', '-help', 'help', 'bantuan']
kumpulan_perintah = ['saya butuh hiburan',
                     'cuaca jakarta',
                     'siapa yang menciptakanmu reemar',
                     'install bahan'
                     ]
pribadi_reemar = ["nama", "kamu", "anda", "namamu", ""]
tanya_siapa = ["siapa", "kamu", "anda", "reemar", "ini"]
perintah_reemar = ["siapa", "yang", "menciptakanmu", "reemar", "menciptakan", "membuatmu"]
perintah_cuaca = ["info", "cuaca", "hari", "ini", "di", "saat"]
bukan_perintah_cuaca = ["ya", "cerahya", "cerah", "hujan", "mendung", "apa", "hari", "ini"]

perintah_github = ["cari", "carikan", "script", "github", "repo", "bernama", "di"]
perintah_hiburan = ["hibur", "saya", "butuh" ,"hiburan", "gabut"]
perintah_gombal = ["gombalin", "gombalin saya",
                   "gombalin dong", "gombalin saya reemar"]
perintah_musik = ["putar", "putarkan", "saya", "play"
                  "musik"]
perintah_install = ["install", "bahan", "tools", "keperluan"]

ya = ["ya", "yes", "y", "ok"]
tidak = ["tidak", "no", "enggak", "n", "t"]

class Front_End():
    def __init__(self):
        os.system('clear')
        print(banner)
        self.Start_Chat()

    def Start_Chat(self):
        while True:
            chat_input = str(input(f'{m}[{p}?{m}]{p} Reemar _{m}>{p} '))
            input_split = chat_input.split(" ")

            in_a = 0
            in_b = 0
            in_c = 0
            in_d = 0
            in_e = 0
            in_f = 0
            in_g = 0
            in_h = 0

            in_not_f = 0
            in_wrong = 0

            if chat_input.lower() in bantuan:
                Help()
            elif chat_input.lower() in ['', ' ']:
                print(f'{m}type : {p}-help {m}for show all command')
            else:
                if len(input_split) > 1:
                    for x in range(len(input_split)):
                        if input_split[x] in perintah_hiburan:
                            in_a += 1
                        if input_split[x] in perintah_install:
                            in_b += 1
                        if input_split[x] in perintah_musik:
                            in_c += 1
                        if input_split[x] in perintah_gombal:
                            in_d += 1
                        if input_split[x] in perintah_github:
                            in_e += 1
                        if input_split[x] in perintah_cuaca:
                            if input_split[x] not in bukan_perintah_cuaca:
                                in_f += 1
                            if input_split[x] in bukan_perintah_cuaca:
                                in_not_f += 1
                        if input_split[x] in perintah_reemar:
                            in_g += 1
                        if input_split[x] in tanya_siapa:
                            in_h += 1

                    if in_not_f > in_f:
                        in_f = 0
                    if in_g == 1:
                        in_g = 0
                        
                    if in_a == 1:
                        in_a = 0

                    if in_h == 1:
                        in_h = 0

                    kw_list = [in_wrong, in_a, in_b, in_c, in_d, in_e, in_f, in_g, in_h]
                    maks = max(kw_list)
                    data_ans = 0

                    for x in range(len(kw_list)):
                        if maks != 0 and kw_list[x] == maks:
                            data_ans = x

                    #print (kw_list, max(kw_list), data_ans) #========

                    if data_ans == 0:
                        Back_end.Simi_chat(chat_input)
                    elif data_ans == 1:
                        Chat_Respod.Hibur("Hibur")
                    elif data_ans == 2:
                        Chat_Respod.Install_bahan("bahan")
                    elif data_ans == 3:
                        Back_end.Hibur.musik("musik")
                    elif data_ans == 4:
                        Back_end.Hibur(hibur="gombal")
                    elif data_ans == 5:
                        Back_end.Script_searcher(input_split)
                    elif data_ans == 6:
                        Back_end.Cuaca(chat_input)
                    elif data_ans == 7:
                        Chat_Respod.Pencipta_reemar("pencipta")
                    elif data_ans == 8:
                        Chat_Respod.tanya_pribadi("tanya")
                else:
                    Back_end.Simi_chat(chat_input)

###-------------------------[ Algoritma Lama ]-------------------------###
"""
    def Start_Chat(self):
        while True:
            chat_input = str(input(f'{m}[{p}?{m}]{p}Reemar _{m}>{p} '))
            if chat_input.lower() in kumpulan_perintah:
                Chat_Respod(chat_input)
            elif chat_input.lower() in perintah_hiburan:
                Chat_Respod.Hibur("Hibur")
            elif chat_input.lower() in perintah_musik:
                Back_end(hibur="musik")
            elif chat_input.lower() in bantuan:
                Help()
            elif "cuaca" in chat_input.split() and len(chat_input.split()) > 1:
                return Back_end.Cuaca(chat_input)
            elif chat_input.split(" ") in perintah_github and len(chat_input.split(" ")) > 1:
                return 

            elif chat_input.lower() in ['', ' ']:
                print(f'{m}type : {p}-help {m}for show all command')
            else:
                print(f'{p}[{m}!{p}] Salah {m}!!')

"""


class Chat_Respod():
    def __init__(self, chat_input):
        for x in range(len(kumpulan_perintah)):
            if str(chat_input) == kumpulan_perintah[x]:
                array_exist = x

        if array_exist == 0:
            self.Hibur()
        elif array_exist == 1:
            self.Pencipta_reemar()
        elif array_exist == 2:
            self.Install_bahan()

    def Hibur(self):
        print(f'\n\t{m}-------------------------{p}')
        print('\t - putarkan saya musik')
        print('\t - gombalin saya reemar')
        print(f'\t{m}-------------------------{p}')
        while True:
            chat_input = str(input(f'{m}[{p}?{m}]{p}Reemar _{m}>{p} '))
            if chat_input in perintah_musik:
                # os.system('termux-tts-speak -r 1.2 Baiklah')
                return Back_end.Hibur(hibur="musik")
                break
            elif chat_input in perintah_gombal:
                return Back_end.Hibur(hibur="gombal")
                break
            else:
                print("Perintah Tidak tersedia")

    def Pencipta_reemar(self):
        print(f"{m}[{p}!{m}]{p} Saya diciptakan oleh Orang yang bernama Muhamad Royyani. Dia Hanyalah Seorang anak, yang masih berumur 16 tahun")

    def Install_bahan(self):
        os.system("pkg install termux-api")
    def tanya_pribadi(self):
        print(f"{m}[{p}!{m}]{p} Saya adalah Reemar yang berkolaborasi dengan simi, saya adalah bot chat, sementara ini saya hanya bisa beberapa saja. untuk bantuan ketik \"help\"")

class Back_end():
    class Hibur():
        def __init__(self, **data):
            if data["hibur"] == "musik":
                return Back_end.Hibur.musik("musik")
            elif data["hibur"] == "gombal":
                return Back_end.Hibur.gombal("gombal")

        def musik(self):
            lokasi_f = str(
                input(f'{m}[{p}?{m}]{p}Masukkan nama folder ex : /sdcard/Music/ _{m}>{p} '))
            os.system('mpv '+lokasi_f)

        def gombal(self):
            # didapat dari https://katasiana.com/kata-kata-gombal/
            ###==---------------------=[ Penggombalan ]=---------------------==###
            kalimat_gombal_awal = ["Kamulah bulan bagi matahariku...",
                                   "Tahu nggak kenapa menara pisa miring?",
                                   "Sejak mengenalmu bawaannya aku pengen belajar terus",
                                   "Bagaimana kalau kita berdua jadi komplotan perampok?",
                                   "Kamu tau gak? Kenapa kalau aku menghafal lihatnya ke atas?",
                                   "Orang kurus itu setia",
                                   "Maksud hati memeluk gunung",
                                   "Kamu tu kayak warteg",
                                   "Aku gak sedih kok kalo besok hari senin",
                                   ]
            kalimat_gombal_akhir = ["Cahaya kemilau dirimu menerangi malamku yang sunyi",
                                    "Soalnya ketarik sama senyuman kamu",
                                    "Belajar menjadi yang terbaik buat kamu.",
                                    "Aku merampok hatimu dan kamu merampas hatiku.",
                                    "soalnya kalau merem langsung kebanyang wajahmu.",
                                    "makan aja tidak pernah nambah apalagi pasangan.",
                                    "apalah daya aku lebih suka memeluk kamu.",
                                    "sederhana namun berkualitas.",
                                    "aku sedihnya kalau gak ketemu kamu",
                                    ]
            total_kalimat_gombal = (len(kalimat_gombal_awal))-1

            while True:
                random_kata = random.randint(0, total_kalimat_gombal)
                #os.system('termux-tts-speak -r 1.2 '+kalimat_gombal_awal[random_kata])
                print("     "+kalimat_gombal_awal[random_kata]+",")
                time.sleep(2)
                #os.system('termux-tts-speak -r 1.2 '+kalimat_gombal_akhir[random_kata])
                print("     "+kalimat_gombal_akhir[random_kata])

                tanya = str(
                    input(f'{m}[{p}?{m}]{p}Apakah anda ingin mendengarkan lagi? : '))
                if tanya.lower() in ya:
                    time.sleep(1)
                elif tanya.lower() in tidak:
                    print("Oke")
                    break
                else:
                    print("Pilihan tidak tersedia")
                    break

    class Cuaca():
        def __init__(self, chat_input):
            for x in range(len(chat_input.split())):
                if chat_input.split()[x] not in perintah_cuaca:
                    # Saya sengaja pakai curl, bisa diganti request tapi saya coba nggak ada warnanya(beda kode)
                    os.system("curl -s  http://wttr.in/" +
                              chat_input.split()[x]+" | sed -n \"1,7p\"")
                    break

    class Script_searcher():
        def __init__(self, chat_input):
            self.chat_input = chat_input
            for x in range(len(chat_input)):
                if chat_input[x] not in perintah_github:
                    json_data = json.loads(requests.get(
                        "https://api.github.com/search/repositories?q="+str(chat_input[x])+"&sort=stars&order=desc").text)
            self.git_url_clone = git_url_clone = []

            try:
                if len(json_data) > 0:
                    print (f'{m}[{p}!{m}]{p} Ini Adalah Beberapa Script yang Saya temukan :){p} ')
                    for total_data in range(len(json_data["items"])):
                        git_url_clone.append(
                            json_data["items"][total_data]["full_name"])
                        print(f"  {m}[{p}{total_data}{m}]{p}", git_url_clone[total_data])
                    clone = bool(self.git_url_clone)
                    
                    while True:
                        print (f'{m}[{p}!{m}]{p} Reemar  : Mau Di Clone?')
                        tanya = str(input(f'{m}[{p}?{m}]{p} Reemar _{m}>{p} '))
                        if tanya in ya:
                            print (f'{m}[{p}!{m}]{p} Reemar  : Nomor?')
                            tanya = str(input(f'{m}[{p}?{m}]{p} Reemar _{m}>{p} '))
                            self.cloning(tanya.split()[-1])
                            break
                        elif tanya in tidak:
                            print (f'{m}[{p}!{m}]{p} Reemar  : Oke, Baiklah')
                            break
                        else:
                            print(f'{p}[{m}!{p}] Salah {m}!!')
                else:
                    print (f'{m}[{p}!{m}]{p} Nope, Script tidak ditemukan :({p} ')
            except:
                print (f'{m}[{p}!{m}]{p} Nope, Script tidak ditemukan :({p} ')

        def cloning(self, chat_input):    
            num = chat_input.strip()
            try:
                os.system("cd ~;git clone https://github.com/"+self.git_url_clone[int(num)])
                print (f'{m}[{p}+{m}]{p} Reemar  :{p} Lokasi Download berada di direktori Home(~)')
            except:
                print(f'{m}type : {p}-help {m}for show all command')

    class Simi_chat():
        def __init__(self, chat_input):
            api = 'https://secureapp.simsimi.com/v1/simsimi/talkset?uid=287126054&av=6.8.9.4&lc=id&cc=&tz=Asia%2FJakarta&os=a&ak=pNfLbeQT%2B0cnFY8YHQb7CNHowpg%3D&message_sentence={}&normalProb=8&isFilter=1&talkCnt=2&talkCntTotal=2&reqFilter=1&session=XZzaduTVCSqa6vMtuyFhGv9eCXiyWwKJVETZjpQjc2oLPGBN2XtpzcKRFhLukHd6EAYVWMiSGuPzQV5Vwcdmwz14&triggerKeywords=%5B%5D'.format(chat_input)
            res = requests.get(api).text
            jes = json.loads(res)['simsimi_talk_set']
            jaw = random.choice(jes['answers'])
            jawab = jaw['sentence']
            print (f'{m}[{p}+{m}]{p} Reemar  :{p} ', jawab)

class Help():
    def __init__(self):
        print('\n\t[ List command ]')
        print(*kumpulan_perintah, sep="\n")


if __name__ == "__main__":
    try:
        clone = False
        requests.get("https://google.com")
        Front_End()
    except:
        print("\n")
        pass
