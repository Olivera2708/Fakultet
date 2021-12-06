#autor: Imenko Prezimić INDEX ra1234-2018
.section .data
prompt_1: .ascii "Unesite string: \0"
d1 = . - prompt_1
prompt_2: .ascii "Enkodovan string: \0"
d2 = . - prompt_2
unos: .fill 50,1,42
d3: .long 0
.section .text
.global main
main:

movl $4, %eax
movl $1, %ebx
movl $prompt_1, %ecx
movl $d1, %edx
int $0x80

movl $3, %eax
movl $0, %ebx
movl $unos, %ecx
movl $50, %edx
int $0x80
decl %eax
movl %eax, d3

movl $unos, %eax
movl $0, %ebx
decl %eax
jmp prvi
krug:
incl %ebx
prvi:
incl %eax
cmpl d3, %ebx
je dalje
cmpb $122, (%eax)
ja krug
cmpb $96, (%eax)
ja mali
cmpb $65, (%eax)
jb krug
cmpb $91, (%eax)
jb veliki
jmp krug

mali:
subl $3, (%eax)
cmpb $97, (%eax)
jb dodaj26
jmp krug

dodaj26:
addl $26, (%eax)
jmp krug

veliki:
subl $3, (%eax)
cmpb $65, (%eax)
jb dodaj26
jmp krug

dalje:
movl $4, %eax
movl $1, %ebx
movl $prompt_2, %ecx
movl $d2, %edx
int $0x80

movl $4, %eax
movl $1, %ebx
movl $unos, %ecx
movl d3, %edx
int $0x80

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
