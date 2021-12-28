.section .text
.global inter_to_oct_str_float
inter_to_oct_str_float:
pushl %ebp
movl %esp, %ebp
pushl %edi
pushl %esi

movl 8(%ebp), %eax #broj
movl 12(%ebp), %edi #adresa stringa
movl $1, %esi

cmpl $3, 16(%ebp)
jbe greska

movb $'0', (%edi)
incl %edi
incl %esi
movb $'.', (%edi)
incl %edi
incl %esi

radi:
movl $8, %ecx
cmpl %esi, 16(%ebp)
jbe dalje
mull %ecx
movl $0, %edx
movl $100000000, %ecx
divl %ecx
addb $'0', %eax
movb %eax, (%edi)
incl %edi
incl %esi
movl %edx, %eax
cmpl $0, %edx
je dalje
jmp radi

dalje:
movb $0, (%edi)
jmp sve_ok

greska:
movl $1, %eax
jmp kraj

sve_ok:
movl $0, %eax

kraj:
popl %esi
popl %edi
movl %ebp, %esp
popl %ebp
ret
