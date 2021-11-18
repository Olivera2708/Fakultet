.section .data
s: .ascii "debcaf\0"
.section .text
.global main
main:
movl $s, %eax
movl $0, %edx

br_el:
cmpb $0, (%eax)
je namesti
incl %edx
incl %eax
jmp br_el

namesti:
movl $s, %eax
ponovo:
movl $s, %eax
decl %edx
krug:
cmpl $1, %edx
je kraj
movl (%eax), %ebx
incl %eax
cmpb $0, (%eax)
je ponovo
cmpb (%eax), %ebx
jb krug
movb (%eax), %ecx
movb %ebx, (%eax)
movb %ecx, -1(%eax)
jmp krug


kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
