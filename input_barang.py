listBrg = []

ulang = 'YA'
while ulang == 'YA' :
    print('Input Data Barang')
    kode = input('Kode Barang : ')
    namaBrg = input('Nama Barang : ')
    qty = int(input('Jumlah Barang : '))
    harga = int(input('Harga Barang : '))
    jumlah = int(qty * harga)
    total = jumlah
    dictBrg = {
        'kode' : kode,
        'namaBrg' : namaBrg,
        'qty' : qty,
        'harga' : harga,
        'total' : total
    }

    
    listBrg.append(dictBrg)
    print(" ")
    ulang = input('Isi data barang lagi? (YA/TIDAK) ')
    print("=======================================================================")

    print('{:^50}'.format("Data Barang"))
    print('{0:10} {1:20} {2:10} {3:10} {4:10}' . format('Kode','NamaBarang','Qty','Harga','Total'))
    
    for dictBrg in listBrg :
        print('{0:10} {1:20} {2:<10} {3:<10} {4:<10}'.format( dictBrg[
        'kode'], dictBrg['namaBrg'], dictBrg['qty'], dictBrg['harga'], dictBrg['total']))

        
   
   