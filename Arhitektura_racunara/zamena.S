.section .data
recenica: .fill 40,1,42
d: .long 0
menjati: .fill 3,1,42
.section .text
.global main
main:

#unos prvog stringa
movl $3, %eax
movl $0, %ebx
movl $recenica, %ecx
movl $40, %edx
int $0x80
decl %eax
movl %eax, d

#unos drugog stringa 
movl $3, %eax
movl $0, %ebx
movl $menjati, %ecx
movl $3, %edx
int $0x80

movl $menjati, %eax
movl (%eax), %ebx #ono sto treba zameniti
addl $2, %eax 
movl (%eax), %ecx #ono sa cim se menja
movl $recenica, %eax
movl $0, %edx

proveri:
cmpl d, %edx
je gotovo
incl %edx
cmpb (%eax), %ebx
je menjaj
dalje:
incl %eax
jmp proveri

menjaj:
movb %ecx, (%eax)
jmp dalje 

gotovo:
movl $4, %eax
movl $1, %ebx
movl $recenica, %ecx
movl d, %edx
int $0x80

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
