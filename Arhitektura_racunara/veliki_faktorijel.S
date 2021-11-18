.section .data
a: .quad 0xf
rezultat: .quad 0
greska: .byte 0
.section .text
.global main
main:
movl a, %eax
movl a+4, %ebx
movl a, %ecx
movl a+4, %edx
subl $1, %eax
subb $0, %ebx
subl $2, a
subb $0, a+4

faktorijel:
cmp $1, %ecx
je kraj
cmp $1, %edx
je kraj

ponovo:
subl $1, %eax
jnc saberi
sbbl $0, %ebx
jc gr

saberi:
addl %ecx, rezultat
adcl %edx, rezultat+4
jc gr

cmp $0, %eax
jnz ponovo
cmp $0, %ebx
jnz ponovo

movl rezultat, %ecx
movl rezultat+4, %edx
subl $1, a
sbbl $0, a+4
movl a, %eax
movl a+4, %ebx
jmp faktorijel

gr:
movb $1, greska

kraj:
movl $0, %eax
movl $1, %ebx
int $0x80
