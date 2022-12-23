# Kita Belajar Casting
# merubah dari suatu tipe ke tipe lain
# tipe data = int,float,str,bool

##INTEGER
print("=====INTEGER=====")
data_int = 9
print("data=",data_int, ",type=",type(data_int))

data_float=float(data_int)
data_str=str(data_int)
data_bool=bool(data_int) #AKAN FALSE JIKA NILAI INT = 0

print("data=",data_float, ",type=",type(data_float))
print("data=",data_str, ",type=",type(data_str))
print("data=",data_bool, ",type=",type(data_bool))


##FLOAT
print("=====FLOAT=====")
data_float=0
print("data=",data_float, ",type=",type(data_float))

data_int = int(data_float) #akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #AKAN FALSE JIKA NILAI INT = 0

print("data=",data_int, ",type=",type(data_int))
print("data=",data_str, ",type=",type(data_str))
print("data=",data_bool, ",type=",type(data_bool))


##BOOLEAN
print("=====BOOLEAN=====")
data_bool=False
print("data=",data_bool, ",type=",type(data_bool))

data_int = int(data_bool) #akan dibulatkan ke bawah
data_str = str(data_bool)
data_float = float(data_bool) #AKAN FALSE JIKA NILAI INT = 0

print("data=",data_int, ",type=",type(data_int))
print("data=",data_str, ",type=",type(data_str))
print("data=",data_float, ",type=",type(data_float))


##STRING
print("=====STRING=====")
data_str="10"
print("data=",data_str, ",type=",type(data_str))

data_int = int(data_str) #STRING HARUS ANGKA
data_str = float(data_str) #STRING HARUS ANGKA
data_bool = bool(data_str) #FALSE JIKA STRING KOSONG

print("data=",data_int, ",type=",type(data_int))
print("data=",data_float, ",type=",type(data_float))
print("data=",data_bool, ",type=",type(data_bool))