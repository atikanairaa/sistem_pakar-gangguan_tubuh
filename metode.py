gejala_list = {
    "G01": "Nyeri punggung bagian bawah",
    "G02": "Kepala, leher, perut, dan bagian pinggul tampak lebih maju",
    "G03": "Kesulitan menempelkan area punggung pada tempat tidur atau lantai",
    "G04": "Postur tubuh membusung",
    "G05": "Kepala terlihat lebih condong ke depan dibandingkan dengan bagian tubuh lain",
    "G06": "Tubuh menjadi bungkuk",
    "G07": "Ada seperti punuk di bagian punggung atas",
    "G08": "Tulang punggung terasa kaku dan otot bagian belakang paha terasa kencang",
    "G09": "Perbedaan pada tinggi bahu kanan dan kiri",
    "G10": "Tubuh cenderung condong ke satu sisi",
    "G11": "Salah satu kaki lebih panjang saat berdiri tegak",
    "G12": "Tinggi pinggang tidak rata",
    "G13": "Kepala tidak sejajar dengan bahu",
    "G14": "Nyeri leher dan bahu",
    "G15": "Leher terasa kaku dan tegang",
    "G16": "Kesulitan dalam berdiri tegak",
    "G17": "Masalah dengan keseimbangan saat berdiri atau duduk",
    "G18": "Postur tubuh condong ke depan",
}

penyakit = {
    "P01": "Lordosis",
    "P02": "Kifosis",
    "P03": "Skoliosis",
    "P04": "Forward Head Posture (FHP)",
    "P05": "Flat Back Syndrome (FBS)"
}

aturan = [
    (["G01", "G02", "G03", "G04"], "P01"),
    (["G05", "G06", "G07", "G08", "G09"], "P02"),
    (["G05", "G06", "G08", "G09"], "P02"),
    (["G05", "G06", "G07", "G08"], "P02"),
    (["G09", "G10", "G11", "G12"], "P03"),
    (["G05", "G13", "G14", "G15"], "P04"),
    (["G01", "G16", "G17", "G18"], "P05"),
    (["G01", "G16", "G17"], "P05")
]

def inferensi(gejala_terpilih):
    hasil = []
    for syarat, kode_penyakit in aturan:
        if all(g in gejala_terpilih for g in syarat):
            if penyakit[kode_penyakit] not in hasil:
                hasil.append(penyakit[kode_penyakit])
    return hasil