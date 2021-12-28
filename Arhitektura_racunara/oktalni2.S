.section .text
.global oct_str_to_inter
oct_str_to_inter:
pushl %ebp
movl %esp, %ebp
pushl %edi
pushl %esi

movl 8(%ebp), %edi #string
movl $8, %esi
movl $0, %eax #krajnji broj
movl $0, %edx

cifra:
movb (%edi), %ecx
andl %ecx, %ecx
jz dalje
subb $'0', %ecx
js greska
cmpl %esi, %ecx
jae greska
mull %esi
jc greska2
addl %ecx, %eax
incl %edi
jmp cifra
dalje:
cmpl %edi, 8(%ebp)
jne sve_ok
jmp greska
greska2:
movl 12(%ebp), %ecx
movl $2, (%ecx)
jmp kraj
greska:
movl 12(%ebp), %ecx
movl $1, (%ecx)
jmp kraj
sve_ok:
movl 12(%ebp), %ecx
movl $0, (%ecx)
kraj:
popl %esi
popl %edi
movl %ebp, %esp
popl %ebp
ret 
