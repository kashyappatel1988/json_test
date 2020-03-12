## Simple JSON parser

### pre-req 
```pip3 install -r requirements.txt```

### usage

```
chmod +x test.py
./test.py
./test.py -s <int> -d <int>   
```

./test.py = Without any commandline argument default arguments are session_id = 107 and device_id =3. <br/>
./test.py -s 60 -d 4 = This will print first 4 tasks same as asked while for 5th task it will use command line arguments. <br/> 
./test.py -s 81 = In this case default device_id would be 3.<br/>
./test.py -d 4 = In this case default session_id would be 107.<br/>
