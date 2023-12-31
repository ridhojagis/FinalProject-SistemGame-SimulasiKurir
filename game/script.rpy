﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aku")
define pa = Character("Pak Andi")
define bi = Character("Bu Ika")
define sep = Character("Septian")
define ant = Character("Anita")
define br = Character("Bu Rini")

screen sc_navigasi:
    add "thunderbolt" xanchor 0.0 yanchor 0.0 xpos 0.01 ypos 0.01
    add "rupiah" xanchor 0.0 yanchor 0.0 xpos 0.11 ypos 0.01
    add "gas" xanchor 0.0 yanchor 0.0 xpos 0.26 ypos 0.01

    # Text jumlah energi, uang, dan bensin
    text "{}%".format(jmlh_energi) xanchor 0.0 yanchor 0.0 xpos 0.05 ypos 0.02
    text "Rp.{}".format(jmlh_uang) xanchor 0.0 yanchor 0.0 xpos 0.15 ypos 0.02
    text "{}%".format(jmlh_bensin) xanchor 0.0 yanchor 0.0 xpos 0.3 ypos 0.02

    vbox:
        xalign 0.98
        yalign 0.02
        imagebutton:
            idle "btn_map.png"
            hover "btn_map_hover.png"
            action ui.callsinnewcontext("lokasitempat")

screen sc_perumdos:   
    vbox:
        xalign 0.88
        yalign 0.028
        imagebutton:
            idle "btn_door.png"
            hover "btn_door_hover.png"
            if (fsm_lokasitempat==8):
                action ui.callsinnewcontext("lokasiperumdost")
            elif (fsm_lokasitempat==9):
                action ui.callsinnewcontext("lokasiperumdosu")

screen map_perumdosu:
    imagemap:
        ground "perumdosu_ground.jpg"
        hover "perumdosu_hover.jpg"

        if (fsm_perumdosu==0):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.385 ypos 0.515
            hotspot(885, 570, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 1), Return("go_u1")]
        elif (fsm_perumdosu==1):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.445 ypos 0.515
            hotspot(589, 570, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 1), Return("go_ugerbang")]
            hotspot(885, 348, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 1), Return("go_u2")]
        elif (fsm_perumdosu==2):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.445 ypos 0.3
            hotspot(885, 570, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 1), Return("go_u1")]
            hotspot(840, 85, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 3), Return("go_u3")]
        elif (fsm_perumdosu==3):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.415 ypos 0.085
            hotspot(885, 348, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 3), Return("go_u2")]

screen map_perumdost:
    imagemap:
        ground "perumdost_ground.jpg"
        hover "perumdost_hover.jpg"

        if (fsm_perumdost==0):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.362 ypos 0.118
            hotspot(595, 289, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 1), Return("go_t1")]
        elif (fsm_perumdost==1):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.4 ypos 0.245
            hotspot(510, 125, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 1), Return("go_tgerbang")]
            hotspot(915, 735, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 3), Return("go_t2")]
        elif (fsm_perumdost==2):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.565 ypos 0.668
            hotspot(595, 289, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 3), Return("go_t1")]
            hotspot(1425, 670, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 3), Return("go_t3")]
        elif (fsm_perumdost==3):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.83 ypos 0.612
            hotspot(595, 289, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 3), Return("go_t1")]
            hotspot(915, 735, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 3), Return("go_t2")]
            hotspot(1745, 565, 190, 180) action [SetVariable("jmlh_bensin", jmlh_bensin - 1), Return("go_t4")]
        elif (fsm_perumdost==4):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.912 ypos 0.58
            hotspot(1425, 670, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 1), Return("go_t3")]

screen map_lokasitempat:
    imagemap:
        ground "lokasi_ground.jpg"
        hover "lokasi_hover.jpg"

        if (fsm_lokasitempat==0):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.16 ypos 0.328

            hotspot(490, 215, 190, 180) action [SetVariable("jmlh_bensin", jmlh_bensin - 3), Return("go_spbu")]
            hotspot(530, 35, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_graha")]
            hotspot(625, 465, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_masjid")]
            
        elif (fsm_lokasitempat==1):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.38 ypos 0.038

            hotspot(490, 215, 190, 180) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_spbu")]
            hotspot(270, 365, 190, 180) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_kantor")]
            hotspot(625, 465, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_masjid")]
            hotspot(900, 35, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_pens")]

        elif (fsm_lokasitempat==2):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.435 ypos 0.358

            hotspot(270, 365, 190, 180) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_kantor")]
            hotspot(530, 35, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_graha")]
            hotspot(845, 565, 190, 180) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_kantin")]
            
        elif (fsm_lokasitempat==3):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.455 ypos 0.482

            hotspot(625, 465, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_masjid")]
            hotspot(710, 815, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_k1mart")]
            
        elif (fsm_lokasitempat==4):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.395 ypos 0.765

            hotspot(710, 815, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_k1mart")]

        elif (fsm_lokasitempat==5):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.475 ypos 0.635

            hotspot(845, 565, 190, 180) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_kantin")]
            hotspot(560, 985, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_asrama")]
            hotspot(1005, 885, 380, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 3), Return("go_aj")]
            hotspot(1285, 760, 380, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_t")]

        elif (fsm_lokasitempat==6):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.51 ypos 0.69

            hotspot(1285, 760, 380, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_t")]
            hotspot(710, 815, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 3), Return("go_k1mart")]
            hotspot(1110, 980, 420, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_wxnp")]
            
        elif (fsm_lokasitempat==7):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.565 ypos 0.75

            hotspot(1005, 885, 380, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_aj")]
            
        elif (fsm_lokasitempat==8):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.655 ypos 0.588

            hotspot(1005, 885, 380, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_aj")]
            hotspot(710, 815, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_k1mart")]
            hotspot(1380, 565, 380, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_u")]
            
        elif (fsm_lokasitempat==9):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.715 ypos 0.438

            hotspot(1285, 760, 380, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_t")]
            hotspot(1200, 285, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_tc")]
            hotspot(981, 385, 190, 180) action [SetVariable("jmlh_bensin", jmlh_bensin - 105), Return("go_perpus")]
            
        elif (fsm_lokasitempat==10):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.525 ypos 0.345

            hotspot(1200, 285, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_tc")]
            hotspot(1380, 565, 380, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_u")]
            
        elif (fsm_lokasitempat==11):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.61 ypos 0.215

            hotspot(981, 385, 190, 180) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_perpus")]
            hotspot(1380, 565, 380, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_u")]
            hotspot(1090, 130, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_ppns")]

        elif (fsm_lokasitempat==12):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.55 ypos 0.112

            hotspot(1200, 285, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_tc")]
            hotspot(900, 35, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_pens")]

        elif (fsm_lokasitempat==13):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.4585 ypos 0.032

            hotspot(1090, 130, 300, 100) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_ppns")]
            hotspot(530, 35, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 5), Return("go_graha")]

        elif (fsm_lokasitempat==14):
            add "marker disini" xanchor 0.0 yanchor 0.0 xpos 0.275 ypos 0.215

            hotspot(530, 35, 300, 120) action [SetVariable("jmlh_bensin", jmlh_bensin - 10), Return("go_graha")]
            hotspot(270, 365, 190, 180) action [SetVariable("jmlh_bensin", jmlh_bensin - 3), Return("go_kantor")]
            
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
        def __init__(self, uang=10000, energi=100, bensin=100):
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
            self.energi -= item.energi_cost
            self.uang += item.reward
            self.item_paket.remove(item)

        def beliMakan(self, item):
            if self.uang >= item.cost:
                self.uang -= item.cost
                self.energi += item.jumlah_energi
                self.item_makanan.append(item)
                return True
            else:
                "Uang kamu tidak cukup"
                return False
            
        def beliBBM(self, item):
            if self.uang >= item.cost:
                self.uang -= item.cost
                self.bensin += item.jumlah_bensin
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

    $ fsm_paket = 0
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
    $ fsm_perumdosu = 0
    $ fsm_perumdost = 0

    python:
        inventory = Inventory()
        migoreng = Makanan("Mi Goreng", 4500, 25)
        nasigoreng = Makanan("Nasi Goreng", 4500, 30)
        bensin_80 = BBM("Bensin", 20000, 80)
        bensin_60 = BBM("Bensin", 15000, 60)
        bensin_40 = BBM("Bensin", 10000, 40)
        bensin_20 = BBM("Bensin", 5000, 20)
        paket1 = Paket("Pak Andi", "Perumdos U, Kos U3", 0, 5, 20000)
        paket2 = Paket("Bu Ika", "Perumdos U, Kos U2", 0, 5, 25000)
        paket3 = Paket("Anita", "Perumdos T, Kos T2", 0, 5, 30000)
        paket4 = Paket("Septian", "Asrama", 0, 5, 15000)
        paket5 = Paket("Bu Rini", "Perumdos T, Kos T4", 0, 5, 10000)
        inventory.addPaket(paket1)
        inventory.addPaket(paket2)
        inventory.addPaket(paket3)
        inventory.addPaket(paket4)
        inventory.addPaket(paket5)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show admin

    # These display lines of dialogue.

    "Selamat datang di permainan Simulasi Kurir."
    "Disini kamu akan berperan sebagai Kurir Paket yang harus mengantarkan semua paket ke setiap customer."
    "Kamu harus mengambil paket yang ada di kantor terlebih dahulu sebelum mengantarnya ke customer."
    "Selama menjadi kurir, kamu harus memperhatikan beberapa indikator seperti energi, bensin, dan keuangan."
    "Bensin kamu akan terus berkurang setiap berpindah lokasi."
    "Energi kamu juga akan terus berkurang selama beraktivitas sebagai kurir. Dan kamu akan merasa lemas jika energimu tidak terpenuhi."
    "Kamu dapat menggunakan uang yang kamu punya untuk membeli bensin di SPBU."
    "Dan juga kamu dapat membeli berbagai makanan yang ada di K1 Mart atau Kantin dengan uang tersebut."

    $ jmlh_energi = inventory.energi
    $ jmlh_uang = inventory.uang
    $ jmlh_bensin = inventory.bensin
    $ jmlh_paket = len(inventory.paket_kantor)
    $ paket_dibawa = len(inventory.item_paket)

    $ fsm_makan = 1
    $ fsm_energi = 1
    $ fsm_bbm = 2
    $ fsm_uang = jmlh_uang

    show screen sc_navigasi
    "Gunakan Map yang ada di pojok kanan atas untuk berpindah lokasi."
    "Saat ini kamu memiliki uang sebanyak Rp. %(jmlh_uang)d dan bensin sebanyak %(jmlh_bensin)d\%."

    scene bg_jalan
    with fade

    a "Hari ini masih ada %(jmlh_paket)s paket di Kantor"
    a "Aku harus mengantarkan semua paket itu hari ini"
    if (paket_dibawa <= 0):
        a "Saat ini aku belum membawa paket apapun, aku harus mengambilnya terlebih dahulu di Kantor"

    jump Kantor

label lokasitempat:
    hide screen sc_navigasi
    call screen map_lokasitempat
    $ paket_dibawa = len(inventory.item_paket)

    if _return == "go_kantor":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Kantor")
    if _return == "go_spbu":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("SPBU")
    if _return == "go_graha":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Graha")
    if _return == "go_pens":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("PENS")
    if _return == "go_ppns":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("PPNS")
    if _return == "go_tc":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Dept_TC")
    if _return == "go_perpus":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Perpus")
    if _return == "go_kantin":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Kantin")
    if _return == "go_k1mart":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("K1Mart")
    if _return == "go_masjid":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Masjid")
    if _return == "go_asrama":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Asrama")
    if _return == "go_wxnp":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Perumdos_WXNP")
    if _return == "go_aj":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Perumdos_AJ")
    if _return == "go_t":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Perumdos_T")
    if _return == "go_u":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Perumdos_U")

label lokasiperumdosu:
    hide sc_perumdos
    call screen map_perumdosu
    $ paket_dibawa = len(inventory.item_paket)

    if _return == "go_ugerbang":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Perumdos_U")
    if _return == "go_u1":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("U_Kos1")
    if _return == "go_u2":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("U_Kos2")
    if _return == "go_u3":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("U_Kos3")

label lokasiperumdost:
    hide sc_perumdos
    call screen map_perumdost
    $ paket_dibawa = len(inventory.item_paket)

    if _return == "go_tgerbang":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("Perumdos_T")
    if _return == "go_t1":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("T_Kos1")
    if _return == "go_t2":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("T_Kos2")
    if _return == "go_t3":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("T_Kos3")
    if _return == "go_t4":
        play sound "/audio/driveby.mp3"
        $ renpy.movie_cutscene("courier.webm")
        $ renpy.jump_out_of_context("T_Kos4")

label SPBU:
    $ fsm_lokasitempat=14
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)
    show screen sc_navigasi
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    elif (jmlh_bensin > 0 and jmlh_bensin <= 80):
        $ fsm_bbm = 1
    elif (jmlh_bensin > 80):
        $ fsm_bbm = 2

    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
        
    scene bg spbu
    "Kamu sedang berada di SPBU"
    if (fsm_bbm == 2):
        "Bensin kamu masih banyak!. Manfaatkan waktumu untuk mengantar paket."
        "Saat ini kamu memiliki uang sebanyak Rp. %(jmlh_uang)d dan bensin sebanyak %(jmlh_bensin)d\%."
    elif (fsm_bbm == 1):
        "Saat ini kamu memiliki uang sebanyak Rp. %(jmlh_uang)d dan bensin sebanyak %(jmlh_bensin)d\%."
        menu:
            "Pilih jumlah bensin"
            "Isi 20" if (jmlh_uang >= bensin_20.cost):
                if(jmlh_bensin + bensin_20.jumlah_bensin > 100):
                    "Tidak bisa diisi, tangki terlalu penuh!"
                    jump SPBU
                $ jmlh_bensin += 20
                $ jmlh_uang -= bensin_20.cost
                if (jmlh_bensin > 0 and jmlh_bensin <= 80):
                    $ fsm_bbm = 1
                elif (jmlh_bensin > 80):
                    $ fsm_bbm = 2
            "Isi 40" if (jmlh_uang >= bensin_40.cost):
                if(jmlh_bensin + bensin_40.jumlah_bensin > 100):
                    "Tidak bisa diisi, tangki terlalu penuh!"
                    jump SPBU
                $ jmlh_bensin += 40
                $ jmlh_uang -= bensin_20.cost
                if (jmlh_bensin > 0 and jmlh_bensin <= 80):
                    $ fsm_bbm = 1
                elif (jmlh_bensin > 80):
                    $ fsm_bbm = 2
            "Isi 60" if (jmlh_uang >= bensin_60.cost):
                if(jmlh_bensin + bensin_60.jumlah_bensin > 100):
                    "Tidak bisa diisi, tangki terlalu penuh!"
                    jump SPBU
                $ jmlh_bensin += 60
                $ jmlh_uang -= bensin_20.cost
                if (jmlh_bensin > 0 and jmlh_bensin <= 80):
                    $ fsm_bbm = 1
                elif (jmlh_bensin > 80):
                    $ fsm_bbm = 2
                $ inventory.beliBBM(bensin_60)
            "Isi 80" if (jmlh_uang >= bensin_80.cost):
                if(jmlh_bensin + bensin_80.jumlah_bensin > 100):
                    "Tidak bisa diisi, tangki terlalu penuh!"
                    jump SPBU
                $ jmlh_bensin += 80
                $ jmlh_uang -= bensin_20.cost
                if (jmlh_bensin > 0 and jmlh_bensin <= 80):
                    $ fsm_bbm = 1
                elif (jmlh_bensin > 80):
                    $ fsm_bbm = 2
                $ inventory.beliBBM(bensin_80)
    jump SPBU

label Kantor:
    $ jmlh_paket = len(inventory.paket_kantor)
    $ paket_dibawa = len(inventory.item_paket)
    $ fsm_lokasitempat=0
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)

    show screen sc_navigasi

    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver

    scene bg kantor
    with fade
    show aku

    if (jmlh_paket > 0):
        $ fsm_paket_kantor = 0
        "Kamu sedang berada di kantor, ada %(jmlh_paket)d paket yang belum diantar"
    else:
        $ fsm_paket_kantor = 1
        "Kamu sedang berada di kantor, Sudah tidak ada paket yang tersisa di Kantor."

    "Saat ini kamu memiliki uang sebanyak Rp. %(jmlh_uang)d dan bensin sebanyak %(jmlh_bensin)d\%."

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"

    if (fsm_paket_kantor == 0):
        menu:
            "Ambil Paket 1" if (fsm_paket_kantor == 0 and fsm_paket_1 == 0):
                $ fsm_paket_1 = 1
                $ inventory.ambilPaket(paket1)
                $ inventory.removePaket(paket1)
                $ jmlh_energi -= paket1.energi_cost
                "Kamu mengambil Paket 1"
                call fsm_updates from _call_fsm_updates
            "Ambil Paket 2" if (fsm_paket_kantor == 0 and fsm_paket_2 == 0):
                $ fsm_paket_2 = 1
                $ inventory.ambilPaket(paket2)
                $ inventory.removePaket(paket2)
                $ jmlh_energi -= paket2.energi_cost
                "Kamu mengambil Paket 2"
                call fsm_updates from _call_fsm_updates_1
            "Ambil Paket 3" if (fsm_paket_kantor == 0 and fsm_paket_3 == 0):
                $ fsm_paket_3 = 1
                $ inventory.ambilPaket(paket3)
                $ inventory.removePaket(paket3)
                $ jmlh_energi -= paket3.energi_cost
                "Kamu mengambil Paket 3"
                call fsm_updates from _call_fsm_updates_2
            "Ambil Paket 4" if (fsm_paket_kantor == 0 and fsm_paket_4 == 0):
                $ fsm_paket_4 = 1
                $ inventory.ambilPaket(paket4)
                $ inventory.removePaket(paket4)
                $ jmlh_energi -= paket4.energi_cost
                "Kamu mengambil Paket 4"
                call fsm_updates from _call_fsm_updates_3
            "Ambil Paket 5" if (fsm_paket_kantor == 0 and fsm_paket_5 == 0):
                $ fsm_paket_5 = 1
                $ inventory.ambilPaket(paket5)
                $ inventory.removePaket(paket5)
                $ jmlh_energi -= paket5.energi_cost
                "Kamu mengambil Paket 5"
                call fsm_updates from _call_fsm_updates_4
            "Ambil semua Paket" if (fsm_paket_kantor == 0):
                $ fsm_paket = 1
                if (fsm_paket_1 == 0):
                    $ fsm_paket_1 = 1
                    $ inventory.ambilPaket(paket1)
                    $ inventory.removePaket(paket1)
                    $ jmlh_energi -= paket1.energi_cost
                if (fsm_paket_2 == 0):
                    $ fsm_paket_2 = 1
                    $ inventory.ambilPaket(paket2)
                    $ inventory.removePaket(paket2)
                    $ jmlh_energi -= paket2.energi_cost
                if (fsm_paket_3 == 0):
                    $ fsm_paket_3 = 1
                    $ inventory.ambilPaket(paket3)
                    $ inventory.removePaket(paket3)
                    $ jmlh_energi -= paket3.energi_cost
                if (fsm_paket_4 == 0):
                    $ fsm_paket_4 = 1
                    $ inventory.ambilPaket(paket4)
                    $ inventory.removePaket(paket4)
                    $ jmlh_energi -= paket4.energi_cost
                if (fsm_paket_5 == 0):
                    $ fsm_paket_5 = 1
                    $ inventory.ambilPaket(paket5)
                    $ inventory.removePaket(paket5)
                    $ jmlh_energi -= paket5.energi_cost
                "Kamu mengambil semua Paket yang ada di kantor"
                call fsm_updates from _call_fsm_updates_5

    jump Kantor

label Graha:
    $ fsm_lokasitempat=1
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)
    show screen sc_navigasi
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg graha
    "Kamu sedang berada di Graha"

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"

    jump Graha

label Masjid:
    $ jmlh_energi -= 5
    $ fsm_lokasitempat=2
    $ paket_dibawa = len(inventory.item_paket)
    show screen sc_navigasi
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg masjid
    "Kamu sedang berada di Masjid"

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"

    menu:
        "pergi ke kantin" if (fsm_lokasitempat==2):
            jump Kantin

    jump Masjid

label Kantin:
    $ fsm_lokasitempat=3
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)
    show screen sc_navigasi
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    elif (jmlh_energi < 50):
        $ fsm_makan = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg kantin
    "Kamu sedang berada di Kantin"

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
    if (fsm_makan == 0):
        a "Wahh laparnya.."

    menu:
        "Makan Mi Goreng" if (fsm_makan == 0):
            if (jmlh_uang >= migoreng.cost):
                $ jmlh_uang -= migoreng.cost
                $ jmlh_energi += migoreng.jumlah_energi
                if (jmlh_energi > 50):
                    $ fsm_makan = 1
        "Makan Nasi Goreng" if (fsm_makan == 0):
            if (jmlh_uang >= nasigoreng.cost):
                $ jmlh_uang -= nasigoreng.cost
                $ jmlh_energi += nasigoreng.jumlah_energi
                if (jmlh_energi > 50):
                    $ fsm_makan = 1
        "pergi ke K1 Mart" if (fsm_lokasitempat==3):
            jump K1Mart
        "pergi ke Masjid" if (fsm_lokasitempat==3):
            jump Masjid

    jump Kantin

label K1Mart:
    $ fsm_lokasitempat=5
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)
    show screen sc_navigasi
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    elif (jmlh_energi < 50):
        $ fsm_makan = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg k1mart
    "Kamu sedang berada di K1 Mart"

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
    if (fsm_makan == 0):
        a "Wahh laparnya.."

    menu:
        "Makan Mi Goreng" if (fsm_makan == 0):
            if (jmlh_uang >= migoreng.cost):
                $ jmlh_uang -= migoreng.cost
                $ jmlh_energi += migoreng.jumlah_energi
                if (jmlh_energi > 50):
                    $ fsm_makan = 1
        "Makan Nasi Goreng" if (fsm_makan == 0):
            if (jmlh_uang >= nasigoreng.cost):
                $ jmlh_uang -= nasigoreng.cost
                $ jmlh_energi += nasigoreng.jumlah_energi
                if (jmlh_energi > 50):
                    $ fsm_makan = 1
        "pergi ke Perum T" if (fsm_lokasitempat==5):
            jump Perumdos_T
        "pergi ke Kantin" if (fsm_lokasitempat==5):
            jump Kantin
        "pergi ke Asrama" if (fsm_lokasitempat==5):
            jump Asrama
        "pergi ke Perumdos A-J" if (fsm_lokasitempat==5):
            jump Perumdos_AJ

    jump K1Mart

label Asrama:
    $ fsm_lokasitempat=4
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)

    if (fsm_paket_kantor == 1 and paket_dibawa == 0):
        "Selamat!! kamu sudah mengantarkan semua pesanan ke customer."
        "Good Ending."
        jump GoodEnding
    
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg asrama
    "Kamu sedang berada di Asrama"

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        
        if(inventory.has_paket(paket4) and fsm_paket_4== 1):
            $ reward = paket4.reward
            show aku at center
            show aku at left
            a "Permisi.."
            show septian at right
            with dissolve
            sep "Iya? paket ya?"
            a "Iya Mas, apa benar atas nama Mas Septian?"
            sep "Iya benar mas"
            a "Baik silahkan Mas.. harga ongkirnya Rp.%(reward)d"
            sep "Oke ini mas"
            $ inventory.antarPaket(paket4)
            $ fsm_paket_4 = 2
            $ jmlh_uang += reward
        elif(fsm_paket_4 == 2):
            "Kamu sudah mengantar paket milik Septian."
        else:
            "Kamu tidak membawa paket milik Septian."
    jump Asrama     

label PENS:
    $ fsm_lokasitempat=13
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)
    show screen sc_navigasi
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg pens
    "Kamu sedang berada di PENS"

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"

    jump PENS      

label PPNS:
    $ fsm_lokasitempat=12
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)
    show screen sc_navigasi
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg ppns
    "Kamu sedang berada di PPNS"

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"

    jump PPNS     

label Dept_TC:
    $ fsm_lokasitempat=11
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)
    show screen sc_navigasi
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg tc
    "Kamu sedang berada di Departemen Teknik Informatika"

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"

    jump Dept_TC     

label Perpus:
    $ fsm_lokasitempat=10
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)
    show screen sc_navigasi
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg perpus
    "Kamu sedang berada di Perpus"

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"

    jump Perpus    

label Perumdos_U:
    $ fsm_lokasitempat=9
    $ fsm_perumdosu = 0
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)

    show screen sc_navigasi
    show screen sc_perumdos
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene ugerbang
    "Kamu sedang berada di Perumdos U"

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"

    jump Perumdos_U

label U_Kos1:
    $ fsm_perumdosu = 1
    $ jmlh_energi -= 3
    $ paket_dibawa = len(inventory.item_paket)
    
    show screen sc_perumdos
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene u1
    "Kamu sedang berada di Perumdos U Kos-Kosan 1"

    jump U_Kos1

label U_Kos2:
    $ fsm_perumdosu = 2
    $ jmlh_energi -= 3
    $ paket_dibawa = len(inventory.item_paket)
    if (fsm_paket_kantor == 1 and paket_dibawa == 0):
        "Selamat!! kamu sudah mengantarkan semua pesanan ke customer."
        "Good Ending."
        return
    
    show screen sc_perumdos
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg u2
    "Kamu sedang berada di Perumdos U Kos-Kosan 2"
    if(paket_dibawa > 0):
        if(inventory.has_paket(paket2) and fsm_paket_2== 1):
            $ reward = paket2.reward
            show aku at center
            show aku at left
            a "Permisi.."
            show ika at right
            with dissolve
            bi "Iya? paket ya?"
            a "Iya Bu, apa benar atas nama Bu Ika?"
            bi "Iya benar mas"
            a "Baik silahkan Bu.. harga ongkirnya Rp.%(reward)d"
            bi "Oke ini mas"
            $ inventory.antarPaket(paket2)
            $ fsm_paket_2 = 2
            $ jmlh_uang += reward
        elif(fsm_paket_2 == 2):
            "Kamu sudah mengantar paket milik Bu Ika."
        else:
            "Kamu tidak membawa paket milik Bu Ika."

    jump U_Kos2

label U_Kos3:
    $ fsm_perumdosu = 3
    $ jmlh_energi -= 3
    $ paket_dibawa = len(inventory.item_paket)
    if (fsm_paket_kantor == 1 and paket_dibawa == 0):
        "Selamat!! kamu sudah mengantarkan semua pesanan ke customer."
        "Good Ending."
        return
    
    show screen sc_perumdos
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg u3
    "Kamu sedang berada di Perumdos U Kos-Kosan 3"
    if(paket_dibawa > 0):
        if(inventory.has_paket(paket1) and fsm_paket_1== 1):
            $ reward = paket1.reward
            show aku at center
            show aku at left
            a "Permisi.."
            show andi at right
            with dissolve
            pa "Iya? paket ya?"
            a "Iya Pak, apa benar atas nama Pak Andi?"
            pa "Iya benar mas"
            a "Baik silahkan Pak.. harga ongkirnya Rp.%(reward)d"
            pa "Oke ini mas"
            $ inventory.antarPaket(paket1)
            $ fsm_paket_1 = 2
            $ jmlh_uang += reward
        elif(fsm_paket_1 == 2):
            "Kamu sudah mengantar paket milik Pak Andi."
        else:
            "Kamu tidak membawa paket milik Pak Andi."

    jump U_Kos3

label Perumdos_T:
    $ fsm_lokasitempat=8
    $ fsm_perumdost = 0
    $ jmlh_energi -= 5
    $ paket_dibawa = len(inventory.item_paket)
    
    show screen sc_navigasi
    show screen sc_perumdos
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg tgerbang
    "Kamu sedang berada di Perumdos T"

    if (paket_dibawa > 0):
        "Kamu sedang membawa %(paket_dibawa)d paket yaitu:"
        if (fsm_paket_1 == 1):
            $ nama_paket = paket1.nama
            $ alamat_tujuan = paket1.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_2 == 1):
            $ nama_paket = paket2.nama
            $ alamat_tujuan = paket2.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_3 == 1):
            $ nama_paket = paket3.nama
            $ alamat_tujuan = paket3.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_4 == 1):
            $ nama_paket = paket4.nama
            $ alamat_tujuan = paket4.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"
        if (fsm_paket_5 == 1):
            $ nama_paket = paket5.nama
            $ alamat_tujuan = paket5.lokasi_antar
            "Atas nama %(nama_paket)s, alamat tujuan di %(alamat_tujuan)s"

    jump Perumdos_T  

label T_Kos1:
    $ fsm_perumdost = 1
    $ jmlh_energi -= 3
    $ paket_dibawa = len(inventory.item_paket)
    
    show screen sc_perumdos
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg t1
    "Kamu sedang berada di Perumdos T Kos-Kosan 1"

    jump T_Kos1

label T_Kos2:
    $ fsm_perumdost = 2
    $ jmlh_energi -= 3
    $ paket_dibawa = len(inventory.item_paket)
    if (fsm_paket_kantor == 1 and paket_dibawa == 0):
        "Selamat!! kamu sudah mengantarkan semua pesanan ke customer."
        "Good Ending."
        return
    
    show screen sc_perumdos
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg t2
    "Kamu sedang berada di Perumdos T Kos-Kosan 2"
    if(paket_dibawa > 0):
        if(inventory.has_paket(paket3) and fsm_paket_3 == 1):
            $ reward = paket3.reward
            show aku at center
            show aku at left
            a "Permisi.."
            show anita at right
            with dissolve
            ant "Iya? paket ya?"
            a "Iya mbak, apa benar atas nama Anita?"
            ant "Iya benar mas"
            a "Baik silahkan mbak.. harga ongkirnya Rp.%(reward)d"
            ant "Oke ini mas"
            $ inventory.antarPaket(paket3)
            $ fsm_paket_3 = 2
            $ jmlh_uang += reward
        elif(fsm_paket_3 == 2):
            "Kamu sudah mengantar paket milik Anita."
        else:
            "Kamu tidak membawa paket milik Anita."

    jump T_Kos2

label T_Kos3:
    $ fsm_perumdost = 3
    $ jmlh_energi -= 3
    $ paket_dibawa = len(inventory.item_paket)
    
    show screen sc_perumdos
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg t3
    "Kamu sedang berada di Perumdos T Kos-Kosan 3"

    jump T_Kos3

label T_Kos4:
    $ fsm_perumdost = 4
    $ jmlh_energi -= 3
    $ paket_dibawa = len(inventory.item_paket)
    if (fsm_paket_kantor == 1 and paket_dibawa == 0):
        "Selamat!! kamu sudah mengantarkan semua pesanan ke customer."
        "Good Ending."
        return
    
    show screen sc_perumdos
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg t4
    "Kamu sedang berada di Perumdos T Kos-Kosan 4"
    if(paket_dibawa > 0):
        if(inventory.has_paket(paket5) and fsm_paket_5 == 1):
            $ reward = paket5.reward
            show aku at center
            show aku at left
            a "Permisi.."
            show rini at right
            with dissolve
            br "Iya? paket ya?"
            a "Iya Bu, apa benar atas nama Bu Rini?"
            br "Iya benar mas"
            a "Baik silahkan Bu.. harga ongkirnya Rp.%(reward)d"
            br "Oke ini mas"
            $ inventory.antarPaket(paket5)
            $ fsm_paket_5 = 2
            $ jmlh_uang += reward
        elif(fsm_paket_5 == 2):
            "Kamu sudah mengantar paket milik Bu Rini."
        else:
            "Kamu tidak membawa paket milik Bu Rini."

    jump T_Kos4 

label Perumdos_AJ:
    $ fsm_lokasitempat=6
    show screen sc_navigasi
    $ paket_dibawa = len(inventory.item_paket)
    
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg perumdosaj
    "Kamu sedang berada di Perumdos AJ"

    jump Perumdos_AJ  

label Perumdos_WXNP:
    $ fsm_lokasitempat=7
    $ paket_dibawa = len(inventory.item_paket)
    show screen sc_navigasi
    
    if (jmlh_energi <= 0):
        $ fsm_energi = 0
    if (jmlh_bensin <= 0):
        $ fsm_bbm = 0
    if (fsm_bbm == 0 or fsm_energi == 0):
        jump GameOver
    scene bg perumdoswxnp
    "Kamu sedang berada di Perumdos WXNP"

    jump Perumdos_WXNP  

label GameOver:
    if (fsm_bbm == 0):
        "Bensin kamu habis. Kamu tidak bisa melanjutkan pengantaran paket karena motormu mogok."
    if (fsm_energi == 0):
        "Energi kamu habis. Kamu tidak bisa melanjutkan pengantaran paket karena kecapekan"
    return

label GoodEnding:

    return
