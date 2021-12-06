.section .text
.global maska64
maska64:
pushl %ebp
movl %esp, %ebp
pushl %esi
pushl %ebx

movl 8(%ebp), %esi #n
movl 12(%ebp), %ecx #v
movl $0, %ebx

cmpl $1, %ecx
jbe preskoci

movl $0x00000000, %edx
movl $0x00000000, %eax
jmp kraj

preskoci:
cmpl $64, %eax
jb nastavi
cmpl $0, %ecx
je sve_jedan

sve_nula:
movl $0x00000000, %edx
movl $0x00000000, %eax
jmp kraj

sve_jedan:
movl $0xffffffff, %edx 
movl $0xffffffff, %eax
jmp kraj

nastavi:
cmpl $0, %ecx
je nula
jmp jedinica

nula:
movl $0xfffffffe, %eax #maska za push
movl $0xffffffff, %edx
jmp dalje

jedinica:
movl $0x00000001, %eax
movl $0x00000000, %edx

dalje:
cmpl %ebx, %esi
je kraj
incl %ebx
roll %eax
cmpl $32, %ebx
jae drugi_deo
jmp dalje

drugi_deo:
cmpl $0, %ecx
je nula_d
jmp jedinica_d

nula_d:
movl $0xfffffffe, %edx #maska za push
movl $0xffffffff, %eax
jmp dalje1

jedinica_d:
movl $0b00000001, %edx
movl $0x00000000, %eax

dalje1:
cmpl %ebx, %esi
je kraj
incl %ebx
roll %edx
jmp dalje1

kraj:
popl %esi
popl %ebx
movl %ebp, %esp
popl %ebp
ret

