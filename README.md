# C for Python Test

Steps

1. (Windows) run `dev.bat` to start a Docker container (`gcc` image)
2. Under `src`, run `compile.sh` or this code from console:
   ``` shell
   gcc -fPIC -shared -o mylib.so demo.c
   ```
3. Run `python3 demo.py`
4. ???
5. Profit!
