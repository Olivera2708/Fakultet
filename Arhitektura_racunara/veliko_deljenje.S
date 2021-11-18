.section .data
a: .quad 0x75D86B4
b: .quad 0x644E
rezultat: .quad 0
ostatak: .quad 0
.section .text
.global main
main:
movl $0, rezultat
movl $0, ostatak
movl a, %eax
movl a+4, %ebx
movl b, %ecx
movl b+4, %edx

ponovo:
addl $1, rezultat
subl %ecx, %eax
sbbl %edx, %ebx

cmp %ecx, %eax
jae ponovo
cmp $0, %edx
je kraj
cmp %edx, %ebx
jae ponovo

kraj:
movl %eax, ostatak
movl %ebx, ostatak+4

movl $0, %eax
movl $1, %ebx
int $0x80
