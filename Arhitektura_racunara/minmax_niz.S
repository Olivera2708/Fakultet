.section .data
niz: .long 2,7,9,3,5,7
NELEM = 6
min: .long 0
max: .long 0
.section .text
.global main
main:
movl $0, %eax
movl niz(,%eax,4), %ebx
movl %ebx, min
movl %ebx, max

provera:
addl $1, %eax
cmpl $NELEM, %eax
jae kraj
movl niz(,%eax,4), %ebx
cmpl min, %ebx
jb novimin
cmpl max, %ebx
ja novimax
jmp provera

novimin:
movl %ebx, min
jmp provera

novimax:
movl %ebx, max
jmp provera

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
