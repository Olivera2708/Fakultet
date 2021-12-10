.section .text
.global SaberiMnozi
SaberiMnozi:
pushl %ebp
movl %esp, %ebp
pushl $0
pushl %ebx
pushl %esi
pushl %edi

movl 8(%ebp), %edi #duzina_niza
movl 12(%ebp), %ebx #niz_a
movl 16(%ebp), %ecx #niz_b
movl 20(%ebp), %esi #niz_c

krug:
cmpl $0, %edi
je kraj
movw (%ebx), %eax
mulw (%ecx)
jc greska1
movw %eax, (%esi)
dalje1:
decl %edi
cmpl $0, %edi
je kraj
addl $2, %ebx
addl $2, %ecx
addl $2, %esi
movw (%ebx), %eax
addw (%ecx), %eax
jc greska2
movw %eax, (%esi)
dalje2:
decl %edi
addl $2, %ebx
addl $2, %ecx
addl $2, %esi
jmp krug

greska1:
movw $11111, (%esi)
incl -4(%ebp)
jmp dalje1

greska2:
movw $11111, (%esi)
incl -4(%ebp)
jmp dalje2

kraj:
movl -4(%ebp), %eax
popl %edi
popl %esi
popl %ebx
movl %ebp, %esp
popl %ebp
ret
