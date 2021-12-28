.section .text
.global oct_str_to_inter
oct_str_to_inter:
pushl %ebp
movl %esp, %ebp
subl $4, %esp
pushl %edi
pushl %esi
pushl %ebx
################################jedan test ne prolazi######################
movl $0, %eax #konacan broj
movl $8, -4(%ebp) #baza
movl $1, %esi #negacija
movl 8(%ebp), %edi #adresa stringa
cmpb $0, (%edi) #prazan string
je greska1
cmpb $'+', (%edi)
je redovno1
cmpb $'-', (%edi)
jne redovno
negl %esi #ako je negativan broj
redovno1:
incl %edi #naredni el stringa
redovno:
movl $0, %ecx
movb (%edi), %ecx
andb %ecx, %ecx
jz kraj
subb $'0', %ecx
js greska1
cmpl -4(%ebp), %ecx
jae greska1
imull -4(%ebp)
jo greska2
movl %eax, %ebx
movl %ecx, %eax
imull %esi
movl %eax, %ecx
movl %ebx, %eax
addl %ecx, %eax
jo greska2
incl %edi #sledeci el stringa
jmp redovno
greska1:
movl 12(%ebp), %esi
movl $1, (%esi)
jmp kraj1
greska2:
movl 12(%ebp), %esi
movl $2, (%esi)
jmp kraj1
kraj:
movl 12(%ebp), %esi
movl $0, (%esi)
kraj1:
popl %ebx
popl %esi
popl %edi
movl %ebp, %esp
popl %ebp
ret
