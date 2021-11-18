.section .data
poruka1: .ascii "Unesite ime i prezime: \0"
d1= . - poruka1
poruka2: .ascii "Vi ste: \0"
d2= . - poruka2
imeprez: .fill 50,1,42
d3: .long 0
.section .text
.global main
main:

movl $4, %eax
movl $1, %ebx
movl $poruka1, %ecx
movl $d1, %edx
int $0x80

movl $3, %eax
movl $0, %ebx
movl $imeprez, %ecx
movl $d3, %edx
int $0x80
decl %eax
movl %eax, d3

movl $imeprez, %eax
subl $1, %eax
dalje:
addl $1, %eax
cmpb $0, (%eax)
je zavrseno
movl (%eax), %ebx
cmpb $90, %ebx
jbe dalje
subb $32, %ebx
movl %ebx, (%eax)
jmp dalje

zavrseno:
movl $4, %eax
movl $1, %ebx
movl $poruka2, %ecx
movl $d2, %edx
int $0x80

movl $4, %eax
movl $1, %ebx
movl $imeprez, %ecx
movl d3, %edx
int $0x80

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
