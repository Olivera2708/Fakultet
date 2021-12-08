.section .data
BREL = 10
a: .long 6, 8, 4, 5, 7, 21, 3, 12, 58, 10
b: .long 11, 56, 3, 1, 7, 9, 78, 14, 54, 9
c: .long 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
nisu_pozitivni: .ascii "Nisu svi pozitivni\0"
d1 = . - nisu_pozitivni
jesu_pozitivni: .ascii "Jesu svi pozitivni\0"
d2 = . - jesu_pozitivni 
.section .text
.global main
main:
movl $0, %edi
movl $a, %ebx
movl $b, %ecx
movl $0, %edx

krug:
incl %edx
cmpl $BREL, %edi
je dalje
cmpl $3, %edx
je oduzmi
movl (%ebx), %esi
addl (%ecx), %esi
movl %esi, c(,%edi,4)
addl $4, %ebx
addl $4, %ecx
incl %edi
jmp krug

oduzmi:
movl (%ebx), %esi
subl (%ecx), %esi
movl %esi, c(,%edi,4)
movl $0, %edx
addl $4, %ebx
addl $4, %ecx
incl %edi
jmp krug

dalje:
movl $0, %edi
movl $c, %eax

izvrsi:
incl %edi
cmpl $BREL, %edi
je jesu
cmpl $0, (%eax)
jbe nisu
addl $4, %eax
jmp izvrsi

jesu:
movl $4, %eax
movl $1, %ebx
movl $jesu_pozitivni, %ecx
movl $d2, %edx
int $0x80
jmp kraj

nisu:
movl $4, %eax
movl $1, %ebx
movl $nisu_pozitivni, %ecx
movl $d1, %edx
int $0x80

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
