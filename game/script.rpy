# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aku")

screen sc_navigasi:
    add "thunderbolt" xanchor 0.0 yanchor 0.0 xpos 0.01 ypos 0.01
    add "rupiah" xanchor 0.0 yanchor 0.0 xpos 0.11 ypos 0.01
    add "gas" xanchor 0.0 yanchor 0.0 xpos 0.26 ypos 0.01

    vbox:
        xalign 0.98
        yalign 0.02
        imagebutton:
            idle "btn_map.png"
            hover "btn_map_hover.png"
            action ui.callsinnewcontext("lokasitempat")

screen map_lokasitempat:
    imagemap:
        ground "lokasi_ground.jpg"
        hover "lokasi_hover.jpg"

        hotspot(270, 365, 190, 180) action Return("go_kantor")
        hotspot(490, 215, 190, 180) action Return("go_spbu")
        hotspot(530, 35, 300, 120) action Return("go_graha")
        hotspot(900, 35, 300, 100) action Return("go_pens")
        hotspot(1090, 130, 300, 100) action Return("go_ppns")
        hotspot(1200, 285, 300, 100) action Return("go_tc")
        hotspot(981, 385, 190, 180) action Return("go_perpus")
        hotspot(845, 565, 190, 180) action Return("go_kantin")
        hotspot(625, 465, 300, 100) action Return("go_masjid")
        hotspot(710, 815, 300, 100) action Return("go_k1mart")
        hotspot(560, 985, 300, 100) action Return("go_asrama")
        hotspot(1110, 980, 420, 100) action Return("go_wxnp")
        hotspot(1005, 885, 380, 100) action Return("go_aj")
        hotspot(1285, 760, 380, 100) action Return("go_t")
        hotspot(1380, 565, 380, 100) action Return("go_u")

        if (fsm_lokasitempat==0):
            hotspot(490, 215, 190, 180) action Return("go_spbu")
            hotspot(530, 35, 300, 120) action Return("go_graha")
            hotspot(625, 465, 300, 100) action Return("go_masjid")
            
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.16 ypos 0.328
        elif (fsm_lokasitempat==1):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.38 ypos 0.038
        elif (fsm_lokasitempat==2):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.435 ypos 0.358
        elif (fsm_lokasitempat==3):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.455 ypos 0.482
        elif (fsm_lokasitempat==4):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.395 ypos 0.765
        elif (fsm_lokasitempat==5):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.475 ypos 0.63
        elif (fsm_lokasitempat==6):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.475 ypos 0.635
        elif (fsm_lokasitempat==7):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.51 ypos 0.69
        elif (fsm_lokasitempat==8):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.565 ypos 0.75
        elif (fsm_lokasitempat==9):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.655 ypos 0.588
        elif (fsm_lokasitempat==10):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.715 ypos 0.438
        elif (fsm_lokasitempat==11):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.525 ypos 0.345
        elif (fsm_lokasitempat==12):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.61 ypos 0.215
        elif (fsm_lokasitempat==13):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.55 ypos 0.112
        elif (fsm_lokasitempat==14):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.4585 ypos 0.032
        elif (fsm_lokasitempat==15):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.275 ypos 0.215

init python:
    class Makanan:
        def __init__(self, nama, cost, jumlah_energi):
            self.nama_makan = nama
            self.cost = cost
            self.jumlah_energi = jumlah_energi

    class BBM:
        def __init__(self, nama, cost, jumlah_bensin):
            self.bensin = nama
            self.cost = cost
            self.jumlah_bensin = jumlah_bensin
    
    class Paket:
        def __init__(self, nama, lokasi_antar, bbm_cost, energi_cost, reward):
            self.nama = nama
            self.lokasi_antar = lokasi_antar
            self.bbm_cost = bbm_cost
            self.energi_cost = energi_cost
            self.reward = reward

    class Inventory:
        def __init__(self, uang=0, energi=100, bensin=100):
            self.uang = uang
            self.energi = energi
            self.bensin = bensin
            self.item_makanan = []
            self.item_paket = []
            self.paket_kantor = []

        def addPaket(self, item):
            self.paket_kantor.append(item)

        def removePaket(self, item):
            self.paket_kantor.remove(item)

        def ambilPaket(self, item):
            self.item_paket.append(item)
            
        def antarPaket(self, item):
            self.bensin -= item.bbm_cost
            self.energi -= item.energi_cost
            self.uang += item.reward
            self.item_paket.remove(item)

        def beliMakan(self, item, jumlah_energi):
            if self.uang >= item.cost:
                self.uang -= item.cost
                self.energi += jumlah_energi
                self.item_makanan.append(item)
                return True
            else:
                "Uang kamu tidak cukup"
                return False
            
        def beliBBM(self, item, jumlah_bensin):
            if self.uang >= item.cost:
                self.uang -= item.cost
                self.bensin += jumlah_bensin
                return True
            else:
                "Uang kamu tidak cukup"
                return False

        def earn(self, nominal):
            self.uang += nominal

        def has_paket(self, item):
                if item in self.item_paket:
                    return True
                else:
                    return False
        
        def has_makanan(self, item):
                if item in self.item_makanan:
                    return True
                else:
                    return False
                
#kontrol FSM utk transisi kondisional
label fsm_updates:

    return

# The game starts here.

label start:

    scene bg room

    $ fsm_paket_1 = 0
    $ fsm_paket_2 = 0
    $ fsm_paket_3 = 0
    $ fsm_paket_4 = 0
    $ fsm_paket_5 = 0
    $ fsm_paket_kantor = 0
    $ fsm_makan = 0
    $ fsm_spbu = 0
    $ fsm_energi = 0
    $ fsm_bbm = 0
    $ fsm_uang = 0
    $ fsm_lokasitempat = 0

    python:
        inventory = Inventory()
        migoreng = Makanan("Mi Goreng", 4500, 50)
        nasigoreng = Makanan("Nasi Goreng", 4500, 50)
        bensin_80 = BBM("Bensin", 20000, 80)
        bensin_60 = BBM("Bensin", 15000, 60)
        bensin_40 = BBM("Bensin", 10000, 40)
        bensin_20 = BBM("Bensin", 5000, 20)
        paket1 = Paket("Paket Pak Andi", "Perumdos U, Kos U3", 0, 5, 20000)
        paket2 = Paket("Paket Bu Ika", "Perumdos U, Kos U2", 0, 5, 25000)
        paket3 = Paket("Paket Anita", "Perumdos T, Kos T2", 0, 5, 30000)
        paket4 = Paket("Paket Septian", "Asrama", 0, 5, 15000)
        paket5 = Paket("Paket Bu Rini", "Perumdos T, Kos T4", 0, 5, 10000)
        inventory.addPaket(paket1)
        inventory.addPaket(paket2)
        inventory.addPaket(paket3)
        inventory.addPaket(paket4)
        inventory.addPaket(paket5)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Selamat datang di permainan Simulasi Kurir."
    "Disini kamu akan berperan sebagai Kurir Paket yang harus mengantarkan semua paket ke setiap customer."
    "Kamu harus mengambil paket yang ada di kantor terlebih dahulu sebelum mengantarnya ke customer."
    "Selama menjadi kurir, kamu harus memperhatikan beberapa indikator seperti energi, bensin, dan keuangan."
    "Bensin kamu akan terus berkurang setiap berpindah lokasi."
    "Energi kamu juga akan terus berkurang selama beraktivitas sebagai kurir. Dan kamu akan merasa lemas jika energimu tidak terpenuhi."
    "Kamu dapat menggunakan uang yang kamu punya untuk membeli bensin di SPBU."
    "Dan juga kamu dapat membeli berbagai makanan yang ada di K1 Mart atau Kantin dengan uang tersebut."

    $ jmlh_uang = inventory.uang
    $ jmlh_bensin = inventory.bensin
    $ jmlh_paket = len(inventory.paket_kantor)
    $ paket_dibawa = len(inventory.item_paket)

    $ fsm_makan = 1
    $ fsm_energi = 1
    $ fsm_bbm = 1
    $ fsm_uang = jmlh_uang

    show screen sc_navigasi
    "Gunakan Map yang ada di pojok kanan atas untuk berpindah lokasi."
    "Saat ini kamu memiliki uang sebanyak Rp. %(jmlh_uang)d dan bensin sebanyak %(jmlh_bensin)d."

    scene bg_jalan
    with fade
    a "Hari ini masih ada %(jmlh_paket)d paket di Kantor"
    a "Aku harus mengantarkan semua paket itu sebelum jam 5 sore"
    a "Saat ini aku belum membawa paket apapun, aku harus mengambilnya terlebih dahulu di Kantor"

    menu:
        "Pergi ke SPBU":
            $ jmlh_bensin -= 10
            jump SPBU
        "Pergi ambil paket di Kantor":
            $ jmlh_bensin -= 10
            jump Kantor

    return

label lokasitempat:
    hide screen sc_navigasi
    call screen map_lokasitempat

    if _return == "go_kantor":
        $ renpy.jump_out_of_context("Kantor")


label SPBU:
    $ fsm_lokasitempat==15
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_spbu
    "Kamu sedang berada di SPBU"
    "Saat ini kamu memiliki uang sebanyak Rp. %(jmlh_uang)d dan bensin sebanyak %(jmlh_bensin)d."

    jump SPBU

label Kantor:
    $ jmlh_paket = len(inventory.paket_kantor)
    $ paket_dibawa = len(inventory.item_paket)
    $ fsm_lokasitempat = 0

    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver

    scene bg_kantor

    if (jmlh_paket > 0):
        $ fsm_paket_kantor = 0
        "Kamu sedang berada di kantor, ada %(jmlh_paket)d paket yang belum diantar"
    else:
        $ fsm_paket_kantor = 1
        "Kamu sedang berada di kantor, Sudah tidak ada paket yang tersisa di Kantor."

    if (paket_dibawa > 0):
        "Kamu sedang membawa beberapa paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "%(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "%(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"

    "Saat ini kamu memiliki uang sebanyak Rp. %(jmlh_uang)d dan bensin sebanyak %(jmlh_bensin)d."

    if (fsm_paket_kantor == 0):
        menu:
            "Ambil Paket 1" if (fsm_paket_kantor == 0 and fsm_paket_1 == 0):
                $ fsm_paket_1 = 1
                $ inventory.ambilPaket(paket1)
                $ inventory.removePaket(paket1)
                "Kamu mengambil Paket 1"
                call fsm_updates
            "Ambil Paket 2" if (fsm_paket_kantor == 0 and fsm_paket_2 == 0):
                $ fsm_paket_2 = 1
                $ inventory.ambilPaket(paket2)
                $ inventory.removePaket(paket2)
                "Kamu mengambil Paket 2"
                call fsm_updates

    jump Kantor

label Graha:
    $ fsm_lokasitempat==1
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_graha
    "Kamu sedang berada di Graha"

    jump Graha

label Masjid:
    $ fsm_lokasitempat==2
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_masjid
    "Kamu sedang berada di Masjid"

    jump Masjid

label Kantin:
    $ fsm_lokasitempat==3
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_kantin
    "Kamu sedang berada di Kantin"

    jump Kantin

label K1Mart:
    $ fsm_lokasitempat==5
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_k1mart
    "Kamu sedang berada di K1 Mart"

    jump K1Mart

label Asrama:
    $ fsm_lokasitempat==4
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_asrama
    "Kamu sedang berada di Asrama"

    jump Asrama     

label PENS:
    $ fsm_lokasitempat==14
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_kantin
    "Kamu sedang berada di PENS"

    jump PENS      

label PPNS:
    $ fsm_lokasitempat==13
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_kantin
    "Kamu sedang berada di PPNS"

    jump PPNS     

label Dept_TC:
    $ fsm_lokasitempat==11
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_kantin
    "Kamu sedang berada di Departemen Teknik Informatika"

    jump Dept_TC     

label Perpus:
    $ fsm_lokasitempat==10
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_kantin
    "Kamu sedang berada di Perpus"

    jump Perpus    

label Perumdos_U:
    $ fsm_lokasitempat==9
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_kantin
    "Kamu sedang berada di Perumdos U"

    jump Perumdos_U

label Perumdos_T:
    $ fsm_lokasitempat==8
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_kantin
    "Kamu sedang berada di Perumdos T"

    jump Perumdos_T  

label Perumdos_AJ:
    $ fsm_lokasitempat==6
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_kantin
    "Kamu sedang berada di Perumdos AJ"

    jump Perumdos_AJ  

label Perumdos_WXNP:
    $ fsm_lokasitempat==7
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0):
        jump GameOver
    scene bg_kantin
    "Kamu sedang berada di Perumdos WXNP"

    jump Perumdos_WXNP  

label GameOver:
    if (fsm_bbm == 0):
        "Bensin kamu habis. Kamu tidak bisa melanjutkan pengantaran paket karena motormu mogok."
    return
