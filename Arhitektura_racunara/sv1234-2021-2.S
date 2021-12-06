#autor: Imenko Prezimić INDEX ra1234-2015
#int encode(char* izvorni, char* ciljni, char* enkodovati);
.section .text
.global encode
encode:
pushl %ebp
movl %esp, %ebp
pushl %ebx
movl $0, %ebx
pushl %esi
movl 16(%ebp), %esi #enkodovati
decl %esi

element:
incl %esi
cmpl $0, (%esi)
je kraj
movl 8(%ebp), %eax #izvorni
movl 12(%ebp), %ecx #ciljani

trazi:
cmpb $0, (%eax)
je element
movl (%eax), %edx
cmpb (%esi), %edx
je menjaj
incl %eax
incl %ecx
jmp trazi

menjaj:
movb (%ecx), %edx
movb %edx, (%esi)
incl %ebx
jmp element

kraj:
movl %ebx, %eax
popl %esi
popl %ebx
movl %ebp, %esp
popl %ebp
ret

