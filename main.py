def roma_to_int(roma):
    roma_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in roma:
        if char not in roma_dict:
            print("Hata: Geçersiz Roma rakamı")
            return None

        current_value = roma_dict[char]

        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value

        prev_value = current_value

    if total < 1 or total > 5000:
        print("Hata: Girdi aralık dışında (1 ile 5000 arasında olmalı)")
        return None

    return total

while True:
    roma_rakami = input("Lütfen bir Roma rakamı girin (örn: III), çıkmak için 'q' tuşuna basın: ")

    if roma_rakami.lower() == 'q':
        break

    sonuc = roma_to_int(roma_rakami)

    if sonuc is not None:
        print(f"Karşılık gelen ondalık sayı: {sonuc}")
