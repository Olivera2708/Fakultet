.section .text
.global maska
maska:
pushl %ebp
movl %esp, %ebp
pushl %ebx

movl 8(%ebp), %eax #n
movl 12(%ebp), %ecx #v
movl $0, %ebx

cmpl $1, %ecx
jbe preskoci

movl $0x00000000, %edx
jmp kraj

preskoci:
cmpl $32, %eax
jb nastavi
cmpl $0, %ecx
je sve_jedan

sve_nula:
movl $0x00000000, %edx
jmp kraj

sve_jedan:
movl $0xffffffff, %edx 
jmp kraj

nastavi:
cmpl $0, %ecx
je nula
jmp jedinica

nula:
movl $0xfffffffe, %edx #maska za push
jmp dalje

jedinica:
movl $0b00000001, %edx

dalje:
cmpl %ebx, %eax
je kraj
roll %edx
incl %ebx
jmp dalje

kraj:
movl %edx, %eax
popl %ebx
movl %ebp, %esp
popl %ebp
ret

