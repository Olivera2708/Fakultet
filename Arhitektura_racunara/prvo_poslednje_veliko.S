.section .data
text: .ascii "ovo je neki tekst\0"
.section .text
.global main
main:
movl $text, %eax
#prvo veliko
movb (%eax), %ebx
subb $32, %ebx
movb %ebx, (%eax)

krug:
cmpb $0, 1(%eax)
je uradi
incl %eax
jmp krug

uradi:
movb (%eax), %ebx
subb $32, %ebx
movb %ebx, (%eax)

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
