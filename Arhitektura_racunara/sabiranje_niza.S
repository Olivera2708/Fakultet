.section .data
a: .long 5,32,9,5,14,6,23,11
b: .long 3,25,7,28,4,6,19,13
c: .long 0
NELEM = 8
.section .text
.global main
main:
movl $0, %eax

saberi:
movl a(,%eax,4), %ebx
movl b(,%eax,4), %ecx
addl %ebx, %ecx
movl %ecx, c(,%eax,4)
addl $1, %eax
cmpl $NELEM, %eax
jbe saberi

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
