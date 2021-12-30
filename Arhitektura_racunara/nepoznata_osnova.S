#int str_to_inter(char* str, unsigned int* greska, unsigned int baza)
.section .text
.global str_to_inter
str_to_inter:
pushl %ebp
movl %esp, %ebp
subl $4, %esp
pushl %esi
pushl %edi
pushl %ebx

movl 16(%ebp), %esi
cmpl $2, 16(%ebp)
jb greska3
movl 12(%ebp), %edi
movl $0, (%edi)
cmpl $36, 16(%ebp)
ja greska3
movl $0, %eax
movl $0, %ecx
movl 8(%ebp), %ebx #string
cmpb $0, (%ebx) #prazan
je greska2
cifra:
movb (%ebx), %ecx
cmpb $10, %ecx
je znak2
subb $'0', %ecx
js greska2
cmpl $10, %ecx
jae next
cmpb 16(%ebp), %ecx
jb cifra2
jae greska2
next:
cmpb $17, %ecx #sa A 65-48
jb greska2
subb $7, %ecx
cmpb $36, %ecx #ovde su velika slova u formatu od 11 do 36
jb cifra2
cmpb $42, %ecx #manje od 97
jb greska2
subb $32, %ecx
cmpb $36, %ecx #mala u formatu od 11 do 36
jb cifra2
jmp greska2

cifra2:
cmpl %esi, %ecx
jae greska2
mull %esi
jc greska1
addl %ecx, %eax
jc greska1
incl %ebx
jmp cifra

znak2:
jmp kraj

greska3:
incl (%edi)

greska2:
incl (%edi)

greska1:
incl (%edi)

kraj:
popl %ebx
popl %edi
popl %esi
movl %ebp, %esp
popl %ebp
ret
