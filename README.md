## Simple JSON parser

### pre-req 
```pip3 install -r requirements.txt```

### usage

```
chmod +x test.py
./test.py
./test.py -s <int> -d <int>   
```

./test.py = Without any commandline argument default arguments are session_id = 107 and device_id =3. 
./test.py -s 60 -d 4 = This will print first 4 tasks same as asked while for 5th task it will use command line argument. 
