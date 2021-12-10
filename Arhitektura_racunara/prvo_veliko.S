.section .data
text: .ascii "ovo je neki tekst\0"
.section .text
.global main
main:

movl $text, %eax
movb (%eax), %ebx
subb $32, %ebx
movb %ebx, (%eax)

krug:
cmpb $0, (%eax)
je kraj
cmpb $' ', -1(%eax)
je povecaj
incl %eax
jmp krug

povecaj:
movb (%eax), %ebx
subb $32, %ebx
movb %ebx, (%eax)
incl %eax
jmp krug

kraj:
movl $0, %eax
movl $1, %ebx
int $0x80
