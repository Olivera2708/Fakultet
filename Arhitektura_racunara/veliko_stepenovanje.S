.section .data
b: .quad 0x19
n: .long 0x8
a: .quad 0
greska: .byte 0
.section .text
.global main
main:
movl b, %eax
movl b+4, %ebx
movl b, %ecx
movl b+4, %edx
movl n, %esi

ponovo:
subl $1, %eax
jnc saberi
sbbl $0, %ebx
jc gr

saberi:
addl %ecx, a
adcl %edx, a+4
jc gr

cmp $0, %eax
jnz ponovo
cmp $0, %ebx
jnz ponovo

movl b, %eax
movl b+4, %ebx
movl a, %ecx
movl a+4, %edx
movl $0, a
movl $0, a+4

decl %esi
cmp $1, %esi
jnz ponovo

gr:
movb $1, greska

kraj:
movl %ecx, a
movl %edx, a+4

movl $0, %eax
movl $1, %ebx
int $0x80
