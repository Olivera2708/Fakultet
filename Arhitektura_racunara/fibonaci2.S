.section .text
.global fibonaci

fibonaci:
pushl %ebp
movl %esp, %ebp

movl $0, %eax
movl $1, %ecx
movl $1, %edx

krug:
cmpl 8(%ebp), %edx #poredimo sa n
je kraj
addl %ecx, %eax
jc prekoracenje
xchgl %ecx, %eax

incl %edx
jmp krug

prekoracenje:
movl 12(%ebp), %eax
movl $1, (%eax)
movl %ebp, %esp
popl %ebp
ret

kraj:
movl %ecx, %eax
movl 12(%ebp), %eax
movl $0, (%eax)

movl %ecx, %eax
movl %ebp, %esp
popl %ebp
ret
