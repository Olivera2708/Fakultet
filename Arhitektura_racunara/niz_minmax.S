.section .data
NELEM = 10
niz: .long 1,2,3,4,5,6,7,8,9,10
suma: .long 0
min: .long 0
max: .long 0
.section .text
.global main
main:
movl $0, %ebx
movl niz(,%ebx,4), %eax
movl %eax, min
movl %eax, max
incl %ebx

poredimin:
movl niz(,%ebx,4), %eax
cmpl min, %eax
jb zamenimin
poredimax:
cmpl max, %eax
ja zamenimax
provera:
cmpl $NELEM, %ebx
jl poredimin

zamenimin:
movl %eax, min
jmp poredimax

zamenimx:
movl %eax, max
jmp provera

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80