# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aku")

screen map_lokasitempat:
    imagemap:
        ground "lokasi_ground.jpg"
        hover "lokasi_hover.jpg"

        hotspot(270, 365, 190, 180) action Return("go_kantor")
        hotspot(490, 215, 190, 180) action Return("go_spbu")
        hotspot(530, 35, 300, 120) action Return("go_graha")
        hotspot(900, 35, 300, 100) action Return("go_pens")
        hotspot(1090, 130, 300, 100) action Return("go_ppns")
        hotspot(1200, 285, 300, 100) action Return("go_ppns")
        hotspot(981, 385, 190, 180) action Return("go_perpus")
        hotspot(845, 565, 190, 180) action Return("go_kantin")
        hotspot(625, 465, 300, 100) action Return("go_masjid")
        hotspot(710, 815, 300, 100) action Return("go_k1mart")
        hotspot(560, 985, 300, 100) action Return("go_asrama")
        hotspot(1110, 980, 420, 100) action Return("go_wxnp")
        hotspot(1005, 885, 380, 100) action Return("go_aj")
        hotspot(1285, 760, 380, 100) action Return("go_t")
        hotspot(1380, 565, 380, 100) action Return("go_u")

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
        def __init__(self, nama, bbm_cost, energi_cost, reward):
            self.nama_paket= nama
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

        def add_paket(self, item):
            self.item_paket.append(item)

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
            
        def antarPaket(self, paket):
            self.bensin -= paket.bbm_cost
            self.energi -= paket.energi_cost
            self.uang += paket.reward
            self.item_paket.remove(paket)

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
        bensin = BBM("Bensin", 20000, 80)
        paket = Paket("Paket 1", 15, 10, 20000)
        

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Selamat datang di permainan Simulasi Kurir."
    "Disini kamu akan berperan sebagai Kurir Paket yang harus mengantarkan semua paket ke setiap customer dalam waktu yang telah ditentukan."
    "Kamu harus mengambil paket yang ada di kantor terlebih dahulu sebelum mengantarnya ke customer."
    "Selama menjadi kurir, kamu harus memperhatikan beberapa kondisi seperti energi, bensin, dan keuangan."
    "Bensin kamu akan terus berkurang setiap berpindah lokasi."
    "Energi kamu juga akan terus berkurang selama beraktivitas sebagai kurir. Dan kamu akan merasa lemas jika energimu tidak terpenuhi."
    "Kamu dapat menggunakan uang yang kamu punya untuk membeli bensin di SPBU."
    "Dan juga kamu dapat membeli berbagai makanan yanga ada di k1mart dengan uang tersebut."

    a "Hari ini ada 5 paket di Kantor"
    a "Aku harus mengantarkan semua paket itu sebelum jam 5 sore"
    a "Saat ini aku belum membawa paket apapun, aku harus mengambilnya terlebih dahulu di Gudang"

    menu:
        "Pergi ke SPBU":
            jump SPBU
        "Pergi ambil paket di Kantor":
            jump Kantor

    return

label lokasitempat:
    call screen map_lokasitempat

    if _return == "go_kantor":
        $ renpy.jump_out_of_context("")

label SPBU:

    return

label Kantor:
    "Kamu sedang berada di kantor"
    return

