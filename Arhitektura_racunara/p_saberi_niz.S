.section .text
.global saberi_niz
saberi_niz:
pushl %ebp
movl %esp, %ebp
subl $4, %esp
pushl %ebx
pushl %esi
pushl %edi

movl 8(%ebp), %eax #niz a
movl 12(%ebp), %ebx #niz b
movl 16(%ebp), %ecx #niz c rezultat
movl $0, %edx #brojac

saberi:
movl 20(%ebp), %esi
cmpl %esi, %edx
je kraj
movl (%eax), %esi
movl 4(%eax), %edi
addl (%ebx), %esi
adcl 4(%ebx), %edi
jc greska
movl %esi, (%ecx)
movl %edi, 4(%ecx)
incl %edx
addl $8, %eax
addl $8, %ebx
addl $8, %ecx
jmp saberi

greska:
movl $1, %eax
popl %edi
popl %esi
popl %ebx
movl %ebp, %esp
popl %ebp
ret

kraj:
movl $0, %eax
popl %edi
popl %esi
popl %ebx
movl %ebp, %esp
popl %ebp
ret
