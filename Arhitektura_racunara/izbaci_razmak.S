.section .data
s: .ascii "    nesto   \0"
razmak: .byte 0
.section .text
.global main
main:
movl $s, %eax

dodji_do_kraja:
cmpb $0, (%eax)
je razmaci
incl %eax
jmp dodji_do_kraja

razmaci:
cmpb $' ', -1(%eax)
jne izbaci
decl %eax
jmp razmaci

izbaci:
movb $0, (%eax)

movl $s, %eax

broj:
cmpb $' ', (%eax)
jne dalje
incb razmak
incl %eax
jmp broj

dalje:
movl %eax, %ebx
subl razmak, %ebx
prvirazmak:
cmpl $1, razmak
je kraj
movl (%eax), %esi
movl %esi, (%ebx)
incl %ebx
incl %eax
decb razmak
jmp prvirazmak

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
