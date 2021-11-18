.section .data
.section .text
.global main
main:
movl $9, %eax
movl $7, %ebx
movl $0, %ecx #rezultat


mnozi:
decl %eax
addl %ebx, %ecx
cmpl $0, %eax
ja mnozi

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
