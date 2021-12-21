.section .text
.global inter_to_oct_str
inter_to_oct_str:
pushl %ebp
movl %esp, %ebp
pushl %edi
pushl %esi

movl 8(%ebp), %eax #broj
movl 12(%ebp), %edi #adresa ciljana
movl 16(%ebp), %ecx #duzina
movl $8, %esi

pretvaraj:
decl %ecx
cmpl $1, %ecx
jb greska
movl $0, %edx
divl %esi
addb $'0', %edx
movb %edx, (%edi)
incl %edi
cmpl $0, %eax
jne pretvaraj
movl $0, (%edi)
decl %edi
movl 12(%ebp), %esi
obrni:
cmpl %edi, %esi
jae sve_ok
movb (%edi), %eax
movb (%esi), %ebx
movb %eax, (%esi)
movb %ebx, (%edi)
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
