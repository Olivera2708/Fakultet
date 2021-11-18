.section .data
niz: .long 2,6,9,3,2
NELEM = 5
suma: .long 0
.section .text
.global main

main:
movl $0, %eax
saberi:
addl niz(,%eax,4), %ebx
addl $1, %eax
cmpl $NELEM, %eax
jb saberi
movl %ebx, suma

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
