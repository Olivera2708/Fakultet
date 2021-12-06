.section .text
.global SetParity
SetParity:
pushl %ebp
movl %esp, %ebp

movl 8(%ebp), %eax
movl (%eax), %ecx
movl $0, %eax
movl $0, %edx

krug:
cmpl $15, %edx
je promeni
shrl %ecx
adcl $0, %eax
incl %edx
cmpl $2, %eax
je vrati
jmp krug

vrati:
movl $0, %eax
jmp krug

promeni:
movl 8(%ebp), %ecx
cmpl $1, %eax
je jedan
shll (%ecx)
shrl (%ecx)
jmp kraj

jedan:
movl $0b1000000000000000, %edx
orl %edx, (%ecx)

kraj:
movl %ebp, %esp
popl %ebp
ret
