.section .data
str_unos:   .ascii "Unesite string:\0"
s1 = . - str_unos
str_ispis:  .ascii "\nObrnuti redosled:\n\0"
s2= . - str_ispis
str_len = 21
str_num = 10
string: .fill str_len*str_num, 1, 42
str_lens: .long 0
.section .text
.global main
main:
movl $str_num, %esi
movl $0, %edi
movl $string, %esp

unesi:
cmpl $0, %esi
je ispis
decl %esi
movl $4, %eax
movl $1, %ebx
movl $str_unos, %ecx
movl $s1, %edx
int $0x80

movl $3, %eax
movl $0, %ebx
movl %esp, %ecx #upis stringa u niz
movl $str_len, %edx
int $0x80
decl %eax
movl %eax, str_lens(,%edi,4) #upis duzine stringa u niz
incl %edi
addl $str_len, %esp
jmp unesi

ispis:
movl $4, %eax
movl $1, %ebx
movl $str_ispis, %ecx
movl $s2, %edx
int $0x80

naopako:
movl %esp, %esi
subl $21, %esi
movl $0, %esp

krug:
cmpl $str_num, %esp
je kraj
incl %esp
movl $4, %eax
movl $1, %ebx
movl %esi, %ecx
movl $4, %edx #ovde bi trebalo da se cita iz niza str_lens
int $0x80
subl $21, %esi
subl $4, %edi
jmp krug

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80

