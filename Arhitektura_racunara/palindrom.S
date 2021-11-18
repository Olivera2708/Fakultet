.section .data
poruka: .ascii "Unesite string:\0"
d1 = . - poruka
nijep:  .ascii "String nije palindrom.\n\0"
n1 = . - nijep
jestep: .ascii "String je palindrom.\n\0"
j1 = . - jestep
unos:   .fill 50,1,42
dp: .long 0
.section .text
.global main
main:

movl $4, %eax
movl $1, %ebx
movl $poruka, %ecx
movl $d1, %edx
int $0x80

movl $3, %eax
movl $0, %ebx
movl $unos, %ecx
movl $50, %edx
int $0x80
decl %eax
movl %eax, dp

#unet palindrom u unos
#duzina palinroma u dp

movl $unos, %ecx #od napred
movl $unos, %ebx #od nazad
addl dp, %ebx
decl %ebx
movl dp, %eax

poredi:
cmpl $0, %eax
je jeste
cmpl $1, %eax
je jeste
movb (%ecx), %edx
cmpb (%ebx), %edx
jne nije
incb %ecx
decb %ebx
subl $2, %eax
jmp poredi

nije:
movl $4, %eax
movl $1, %ebx
movl $nijep, %ecx
movl $n1, %edx
int $0x80

movl $1, %eax
movl $1, %ebx
int $0x80

jeste:
movl $4, %eax
movl $1, %ebx
movl $jestep, %ecx
movl $j1, %edx
int $0x80

movl $1, %eax
movl $0, %ebx
int $0x80

