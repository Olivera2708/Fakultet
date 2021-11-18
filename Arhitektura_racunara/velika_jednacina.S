.section .data
b: .quad 0x644E
c: .quad 0x212D3
a: .quad 0
greska: .byte 0
.section .text
.global main
main:
movl $0, greska
movl b, %ebx
movl b+4, %ecx
movl c, %eax
movl c+4, %edx

mnozi2:
addl b, %ebx
adcl b+4, %ecx
jc gr
movl %ebx, b
movl %ecx, b+4

deli3:
subl $3, %eax
subb $0, %edx
addl  $1, a
adcl $0, a+4
cmp $3, %eax
jae deli3

movl a, %eax
movl a+4, %edx
addl b, %eax
adcl b+4, %edx

movl %eax, a
movl %edx, a+4
jmp kraj

gr:
movl $1, greska

kraj:
movl $0, %eax
movl $1, %ebx
int $0x80
