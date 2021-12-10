.section .data
string: .fill 20,1,42
d: .long 0
.section .text
.global main
main:
movl $3, %eax
movl $0, %ebx
movl $string, %ecx
movl $20, %edx
int $0x80
decl %eax
movl %eax, d

movl $string, %eax
movl d, %edx

krug:
cmpb $0, %edx
je kraj
cmpb $1, %edx
je kraj
movb (%eax), %ebx
movb 1(%eax), %ecx
movb %ebx, 1(%eax)
movb %ecx, (%eax)
addl $2, %eax
subl $2, %edx
jmp krug

kraj:
movl $4, %eax
movl $1, %ebx
movl $string, %ecx
movl d, %edx
int $0x80

movl $1, %eax
movl $0, %ebx
int $0x80
