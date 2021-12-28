.section .text
.global inter_to_oct_str
inter_to_oct_str:
pushl %ebp
movl %esp, %ebp
pushl %edi
pushl %esi

movl 8(%ebp), %eax #broj
movl 12(%ebp), %edi #adresa stringa
movl $8, %ecx

andl %eax, %eax
jns cifra
movb $'-', (%edi)
decl 16(%ebp)
incl %edi
incl 12(%ebp)
negl %eax

cifra:
decl 16(%ebp)
cmpl $1, 16(%ebp)
jb greska
movl $0, %edx
divl %ecx
addl $'0', %edx
movb %edx, (%edi)
incl %edi
cmpl $0, %eax
jne cifra
movl $0, (%edi)
decl %edi
movl 12(%ebp), %esi
obrni:
cmpl %edi, %esi
jae sve_ok
movb (%edi), %eax
movb (%esi), %ecx
movb %eax, (%esi)
movb %ecx, (%edi)
incl %esi
decl %edi
jmp obrni
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
