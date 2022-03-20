# Singkatan
Merupakan library python untuk mengubah singkatan menjadi kata asli dalam bahasa Indonesia. 

## How to use it
Cara untuk menggunakannya sangat mudah. Berikut contohnya
```python
from Singkatan.SingkatanConverter import SingkatanConverter

# Inisialisasi terlebih dahulu
test = SingkatanConverter()

# Silahkan masukan kata ke dalam method convert.
# Jika ada di dalam dataset, akan return kata aslinya. 
# Jika tidak ada akan return kata itu sendiri
test.convert('djln')      # di jalan
test.convert('ats')       # ats (karena ats belum terdefine di dataset)
```
## Kamu bisa menambahkan dataset sendiri
Yup, kamu bisa menambahkan dataset sendiri. Caranya juga cukup mudah. Berikut contohnya
```python
from Singkatan.SingkatanConverter import SingkatanConverter

# Inisialiasi seperti biasa
test = SingkatanConverter()
test.importDictionary('./path/to/dictionary.csv')

test.convert('ats')     # atas (jika terdapat data di dalam dictionarynya)
```

## Format dictionary atau dataset
Untuk formatnya dalam csv dan berikut strukturnya
```csv
singkatan;kata asli
singkatan;kata asli
```
Kamu bisa melihat detailnya di repository ini [Meisa Putri 21 - Indonesian Twitter Emotion Dataset](https://github.com/meisaputri21/Indonesian-Twitter-Emotion-Dataset)

## Update
Kedepannya akan diupdate jika ada perubahan, termasuk formatting dataset supaya lebih mudah digunakan