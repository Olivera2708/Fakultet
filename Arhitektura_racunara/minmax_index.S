.section .data
NELEM = 8
niz: .long 12,5,6,23,7,45,9,26
min: .long 0
max: .long 0
.section .text
.global main
main:
movl $0, %eax
movl niz(,%eax,4), %edi #cuvam min
movl niz(,%eax,4), %esi #cuvam max

poredi:
addl $1, %eax
cmpl $NELEM, %eax
jae kraj
movl niz(,%eax,4), %ebx
cmpl %ebx, %edi
jb dalje
movl %ebx, %edi
movl %eax, min
dalje:
cmpl %ebx, %esi
ja poredi
movl %ebx, %esi
movl %eax, max
jmp poredi

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
