.section .text
.global inter_to_oct_str_float
inter_to_oct_str_float:
pushl %ebp
movl %esp, %ebp
pushl %edi

movl 8(%ebp), %eax #broj
movl 12(%ebp), %edi #adresa
movl %eax, %edx

cmpl $3, 16(%ebp)
jbe greska

movl $'0', (%edi)
incl %edi
movl $'.', (%edi)
incl %edi

addl $2, 12(%ebp)

konvertovanje:
movl %edx, %eax
movl $8, %ecx #baza
movl $0, %edx
decl 16(%ebp)
cmpl $2, 16(%ebp)
jbe dalje
mull %ecx
movl $100000000, %ecx
divl %ecx
addb $'0', %eax
movb %eax, (%edi)
incl %edi
cmpl $0, %edx
jne konvertovanje
dalje:
movb $0, (%edi)
decl %edi
jmp dobro

greska:
movl $1, %eax
jmp kraj

dobro:
movl $0, %eax

kraj:
popl %edi
movl %ebp, %esp
popl %ebp
ret
