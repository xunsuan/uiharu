import os

OUT = 'build/'

print("\nstep1~>\033[32mset 32bit environment virable\033[0m\n")
print("\033[34m==>\033[0m CFLAGS=-m32")
os.popen("export CFLAGS='-m32'")
print("\033[34m==>\033[0m CXXFLAGS=-m32")
os.popen("export CXXFLAGS='-m32'")
print("\033[34m==>\033[0m LDFLAGS=-m32")
os.popen("export LDFLAGS='-m32'")
print("\n")
if os.path.isdir('./{OUT}'.format(OUT=OUT)):
    print("step2~>\033[32mclean build env\033[0m\n")
    os.system("make clean")
print("step2~>\033[32mmake kernel\033[0m\n")
os.system("make build")
os.system("make")
print("\n")
print("step3~>\033[32mwrite kernel 2 disk\033[0m\n")
os.popen("sh ./tools/write_kernel_2_disk.sh {OUT}kernel.bin".format(OUT=OUT))
print("\n\033[31mdone!\033[0m\n")
