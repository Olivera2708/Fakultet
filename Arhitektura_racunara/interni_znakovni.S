.section .data
duzina = 10
znakovni: .fill duzina,1,0
.section .text
.global main
main:
movl $3750000, %eax #broj
movl $znakovni, %edi #adresa upisa
movl $10, %ebx #baza
cifra:
movl $0, %edx #ovde ce se nalaziti cifra
divl %ebx
addb $'0', %edx #dodam ascii
movb %edx, (%edi)
incl %edi
cmpl $0, %eax
jne cifra
movb $0, (%edi) #dodaj kraj stringa
decl %edi
movl $znakovni, %esi
obrni:
cmpl %edi, %esi
jae kraj
movb (%esi), %eax
movb (%edi), %ebx
movb %eax, (%edi)
movb %ebx, (%esi)
incl %esi
decl %edi
jmp obrni
kraj:
movl $1, %eax
movl $0, %ebx
int $0x80
