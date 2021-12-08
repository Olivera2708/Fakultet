.section .data
vise_ima_slova: .ascii "Vise ima slova\0"
d1 = . - vise_ima_slova
vise_ima_bez_slova: .ascii "Vise ima znakova\0"
d2 = . - vise_ima_bez_slova
string: .fill 50,1,42
d: .long 0
slova: .long 0
nisu_slova: .long 0
.section .text
.global main
main:

unos:
movl $3, %eax
movl $0, %ebx
movl $string, %ecx
movl $50, %edx
int $0x80
decl %eax
movl %eax, d

movl $0, %ebx
movl $string, %eax
provera:
incl %ebx
cmpb d, %ebx
je kraj
cmpb $65, (%eax)
jb nije_slovo
cmpb $122, (%eax)
ja nije_slovo
cmpb $90, (%eax)
jbe jeste_slovo
cmpb $97, (%eax)
jae jeste_slovo
jmp provera

nije_slovo:
addl $1, nisu_slova
jmp provera

jeste_slovo:
addl $1, slova
jmp provera

kraj:
movl slova, %eax
cmpl nisu_slova, %eax
ja vise_slova

movl $4, %eax
movl $1, %ebx
movl $vise_ima_bez_slova, %ecx
movl $d2, %edx
int $0x80
jmp end

vise_slova:
movl $4, %eax
movl $1, %ebx
movl $vise_ima_slova, %ecx
movl $d1, %edx
int $0x80


end:
movl $1, %eax
movl $0, %ebx
int $0x80
