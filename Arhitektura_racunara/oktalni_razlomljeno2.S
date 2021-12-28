.section .text
.global oct_str_float_to_inter
oct_str_float_to_inter:
pushl %ebp
movl %esp, %ebp
pushl %edi
pushl %esi

movl 8(%ebp), %edi #adresa stringa
#u 12(%ebp) je adresa greske
movl $8, %esi #baza
movl $0, %ecx
movl $0, %eax

na_kraj:
cmpb $0, 1(%edi)
je dalje
incl %edi
jmp na_kraj

dalje:
movl %eax, %ecx
movl $0, %eax
cmpb $'.', (%edi)
je sve_ok
movb (%edi), %eax
subb $'0', %eax
js greska
cmpl %esi, %eax
jae greska
movl $100000000, %edx
mull %edx
addl %ecx, %eax
divl %esi
decl %edi
jmp dalje

greska:
movl 12(%ebp), %ecx
movl $1, (%ecx)
jmp kraj

sve_ok:
movl %ecx, %eax
movl 12(%ebp), %ecx
movl $0, (%ecx)

kraj:
movl %ebp, %esp
popl %ebp
ret
