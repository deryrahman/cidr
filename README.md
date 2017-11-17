# Tugas Kecil Jaringan Komputer
Dery Rahman A / 13515097

### Petunjuk penggunaan program

1. Buka terminal, jalankan make run
    ```sh
    $ make run
    ```
2. Karena saya menggunakan python, maka tidak perlu dicompile

### Penjelasan singkat

**Phase 1**
    Network IPv4 berbentuk quad-dotted dengan masing-masing merepresentasikan 8-bit (1-byte). Pada dasarnya sebuah network IPv4 dapat mempunyai beberapa host dengan melakukan masking. Misalnya untuk network dengan address 53.71.139.80 dan netmask /25, dapat mempunyai sebanyak 254 host.
    Netmask yang digunakan adalah /25 = 11111111.11111111.11111111.1|0000000. Address yang digunakan 53.71.139.80 = 00110101.01000111.10001011.0|1010000. Address setelah dilakukan masking dengan netmask akan menghasilkan host gateway / address subnet. Host gateway dari hasil masking tersebut adalah 53.71.139.0 = 00110101.01000111.10001011.0|**0000000**. Dan memiliki host boardcast 53.71.139.127 = 00110101.01000111.10001011.0|**1111111**. Boardcast diambil dari host yang mempunyai semua nilai bit 1, sedangkan gateway semua nilai bit 0. Antara address 53.71.139.0 hingga 53.71.139.127 merupakan address host yang valid untuk network 53.71.139.80 dengan netmask /25. Dalam contoh ini, subnetnya adalah 53.71.139.0/25
    Karena pada soal tidak diberikan netmask, maka untuk semua host dari network xxx.xxx.xxx.xxx dengan netmask /32 adalah merupakan host yang valid. (hanya mempunyai 1 host, yaitu xxx.xxx.xxx.xxx itu sendiri). Dalam kata lain, salah satu subnetnya yang valid adalah xxx.xxx.xxx.xxx/32

**Phase 2**
    Untuk setiap subnet, jumlah host yang dapat dibentuk adalah 2^(32-netmask). Misal untuk subnet 53.71.139.0/25, host yang dapat dibentuk antara rentang 53.71.139.0 = 00110101.01000111.10001011.0|**0000000** hingga 53.71.139.127 = 00110101.01000111.10001011.0|**1111111**
    
**Phase 3**
    Untuk mengecek apakah suatu host berada pada subnet yang diberikan, format address host dan subnet dijadikan representasi bit. Kemudian bandingkan n bit depan antara host dan subnet tadi, n adalah netmask. Jika sama, maka host tersebut berada dalam subnet yang sama. Misal untuk subnet 53.71.139.0/25, akan mempunyai representasi bit **00110101.01000111.10001011.0**|0000000 dan netmask 25, maka host akan valid jika mempunyai representasi bit antara **00110101.01000111.10001011.0**|0000000 hingga **00110101.01000111.10001011.0**|1111111