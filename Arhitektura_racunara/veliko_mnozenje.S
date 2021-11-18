.section .data
a: .quad 0x75D86B4
b: .quad 0x644E
rezultat: .quad 0
greska: .byte 0
.section .text
.global main
main:
movb $0, greska
movl $0, rezultat
movl a, %eax
movl a+4, %ebx
movl b, %ecx
movl b+4, %edx

ponovo:
subl $1, %ecx
jnc saberi
sbbl $0, %edx
jc gr

saberi:
addl %eax, rezultat
adcl %ebx, rezultat+4
jc gr

cmp $0, %ecx
jnz ponovo
cmp $0, %edx
jnz ponovo
jz kraj

gr:
movb $1, greska

kraj:
movl $0, %eax
movl $1, %ebx
int $0x80
