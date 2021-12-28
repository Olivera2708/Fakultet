.section .data
prompt1: .ascii "Unseite logicki izraz: \0"
d1= . - prompt1
prompt2: .ascii "Rezultat: \0"
d2= . - prompt2
err1: .ascii "Greska kod operanda.\n\0"
d3= . - err1
err2: .ascii "Greska kod operacije.\n\0"
d4= . - err2
unos: .fill 101,1,42
duzina: .long 0
broj1: .long 0
broj2: .long 0
brojac: .long 0
opera: .long 0
kraj: .long 0
rez: .fill 4,1,42
duz: .long 0
newline: .ascii "\n\0"
nl= . - newline
.section .text
.global main
main:

movl $4, %eax
movl $1, %ebx
movl $prompt1, %ecx
movl $d1, %edx
int $0x80

movl $3, %eax
movl $0, %ebx
movl $unos, %ecx
movl $101, %edx
int $0x80
decl %eax
movl %eax, duzina

movl $unos, %edi

broj:
movl $0, %eax
cmpb $'x', 1(%edi)
je heksadecimalni1
cmpb $'X', 1(%edi)
je heksadecimalni1
jmp decimalni

decimalni:
movl $0, %ecx
movb (%edi), %ecx
cmpb $32, %ecx
je got_br
cmpb $10, %ecx
je gotovo1
subb $'0', %ecx
js g_operanda
cmpl $10, %ecx
jae g_operanda
movl $10, %ebx
mulb %ebx
jc g_operanda
addb %ecx, %eax
jc g_operanda
incl %edi
jmp decimalni

heksadecimalni1:
addl $2, %edi
heksadecimalni:
movl $0, %ecx
movb (%edi), %ecx
cmpb $32, %ecx
je got_br
cmpb $10, %ecx
je gotovo1
subb $'0', %ecx
js g_operanda
cmpl $10, %ecx #broj 0-9
jb dalje
subb $7, %ecx
cmpl $10, %ecx
jb g_operanda
cmpl $17, %ecx #broj 10-16
jb dalje
subb $32, %ecx
cmpl $10, %ecx
jb g_operanda
cmpl $17, %ecx
jb dalje
jmp g_operanda

dalje:
movl $16, %ebx
mulb %ebx
jc g_operanda
addb %ecx, %eax
jc g_operanda
incl %edi
jmp heksadecimalni

got_br:
incl %edi
incl brojac
movl %eax, broj1
cmpl $3, brojac
je uradi
jmp operacija

operacija:
movl %eax, broj1
incl brojac
cmpb $'^', (%edi)
je ili
cmpb $'<', (%edi)
je levo
cmpb $'>', (%edi)
je desno
jmp g_operacija

ili:
movl $1, opera
movl broj1, %ebx
movl %ebx, broj2
addl $2, %edi
jmp broj

levo:
movl $2, opera
movl broj1, %ebx
movl %ebx, broj2
addl $2, %edi
jmp broj

desno:
movl $3, opera
movl broj1, %ebx
movl %ebx, broj2
addl $2, %edi
jmp broj

uradi:
movl $1, brojac
cmpl $1, opera
je radi_ili
cmpl $2, opera
je radi_levo
cmpl $3, opera
je radi_desno

radi_ili:
movl broj1, %eax
movl broj2, %ebx
xorb %ebx, %eax
movl %eax, broj1
cmpl $1, kraj
je gotovo
jmp operacija

radi_levo:
movl broj1, %ebx
movl broj2, %eax
levlje:
cmpl $0, %ebx
je nas2
rolb %eax
decl %ebx
jmp levlje
nas2:
movl %eax, broj1
cmpl $1, kraj
je gotovo
jmp operacija

radi_desno:
movl broj1, %ebx
movl broj2, %eax
desnje:
cmpl $0, %ebx
je nas1
rorb %eax
decl %ebx
jmp desnje
nas1:
movl %eax, broj1
cmpl $1, kraj
je gotovo
jmp operacija

gotovo1:
movl %eax, broj1
incl kraj
jmp uradi

gotovo:
movl $rez, %edi #string za upis
movl broj1, %eax #broj koji prebacujem
movl $8, %ecx #baza
pretvori:
movl $0, %edx
divl %ecx
addb $'0', %edx
movb %edx, (%edi)
incl duz
cmpl $0, %eax
je okreni
incl %edi
jmp pretvori

okreni:
movl $rez, %esi
okreci:
cmpl %edi, %esi
jae ispis
movb (%edi), %eax
movb (%esi), %ebx
movb %eax, (%esi)
movb %ebx, (%edi)
incl %esi
decl %edi
jmp okreci

ispis:
movl $4, %eax
movl $1, %ebx
movl $prompt2, %ecx
movl $d2, %edx
int $0x80

movl $4, %eax
movl $1, %ebx
movl $rez, %ecx
movl duz, %edx
int $0x80

movl $4, %eax
movl $1, %ebx
movl $newline, %ecx
movl $nl, %edx
int $0x80

movl $0, %ebx
jmp end

g_operacija:
movl $4, %eax
movl $1, %ebx
movl $err2, %ecx
movl $d4, %edx
int $0x80
movl $1, %ebx
jmp end

g_operanda:
movl $4, %eax
movl $1, %ebx
movl $err1, %ecx
movl $d3, %edx
int $0x80
movl $1, %ebx
jmp end

end:
movl $1, %eax
int $0x80
