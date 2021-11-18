.section .data
.section .text
.global main
main:
movl $10, %ecx #n-ti
movl $0, %eax
movl $1, %ebx

petlja:
decl %ecx
addl %ebx, %eax
movl %eax, %edx
movl %ebx, %eax
movl %edx, %ebx
cmpl $1, %ecx
ja petlja

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80