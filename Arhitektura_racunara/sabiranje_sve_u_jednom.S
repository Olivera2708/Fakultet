.section .data
ulaz1:      .ascii "Unesite bazu broja:\0"
u1= . - ulaz1
ulaz2:      .ascii "Unesite broj:\0"
u2= . - ulaz2
ulaz3:      .ascii "Unesite bazu rezultata:\0"
u3= . - ulaz3
izlaz1:     .ascii "Rezultat:\0"
i1= . - izlaz1
greska1:    .ascii "Greska: pogresan znak!\0"
d1= . - greska1
greska2:    .ascii "Greska: prekoracenje!\0"
d2= . - greska2
baza1: .fill 3,1,42
baza2: .fill 3,1,42
baza3: .fill 3,1,42 
broj1: .fill 33,1,42
broj2: .fill 33,1,42
b1: .long 0
b2: .long 0
b3: .long 0
br1: .long 0
br2: .long 0
baza1b: .long 0
baza2b: .long 0
baza3b: .long 0
broj1b: .long 0
broj2b: .long 0
greska: .long 0
zbir_dec: .long 0
rezultat: .fill 32,1,42
duz_r: .long 0
.section .text
.global main
main:

#unos prve baze
movl $4, %eax
movl $1, %ebx
movl $ulaz1, %ecx
movl $u1, %edx
int $0x80

movl $3, %eax
movl $0, %ebx
movl $baza1, %ecx
movl $3, %edx
int $0x80
decl %eax
movl %eax, b1 #duzina baze

#####pretvori u broj#####
movl $0, %eax
movl $baza1, %ecx
pre1:
cmpl $0, b1
je got1
decl b1
movb (%ecx), %ebx
subb $'0', %ebx
js pogresan_znak
cmpl $10, %ebx
jae pogresan_znak
movl $10, %edi
mull %edi
addl %ebx, %eax
incl %ecx
jmp pre1

got1:
movl %eax, baza1b
cmpl $2, %eax
jb prekoracenje
cmpl $16, %eax ##36
ja prekoracenje

#unos broja
movl $4, %eax
movl $1, %ebx
movl $ulaz2, %ecx
movl $u2, %edx
int $0x80

movl $3, %eax
movl $0, %ebx
movl $broj1, %ecx
movl $32, %edx #ovo moras razmilsiti koliko je ogranicenje -> 64/baza
int $0x80

pushl baza1b
pushl $greska
pushl $broj1
call str_to_inter
addl $12, %esp

cmpl $1, greska
je prekoracenje
cmpl $2, greska
je pogresan_znak

#nakon ovoga resenje u %eax
movl %eax, broj1b


got2:

#unos druge baze
movl $4, %eax
movl $1, %ebx
movl $ulaz1, %ecx
movl $u1, %edx
int $0x80

movl $3, %eax
movl $0, %ebx
movl $baza2, %ecx
movl $3, %edx
int $0x80
decl %eax
movl %eax, b2 #duzina baze

#####pretvori u broj#####
movl $0, %eax
movl $baza2, %ecx
pre3:
cmpl $0, b2
je got3
decl b2
movb (%ecx), %ebx
subb $'0', %ebx
js pogresan_znak
cmpl $10, %ebx
jae pogresan_znak
movl $10, %edi
mull %edi
addl %ebx, %eax
incl %ecx
jmp pre3

got3:
movl %eax, baza2b
cmpl $2, %eax
jb prekoracenje
cmpl $16, %eax ##36
ja prekoracenje
#unos drugog broja

#unos broja
movl $4, %eax
movl $1, %ebx
movl $ulaz2, %ecx
movl $u2, %edx
int $0x80

movl $3, %eax
movl $0, %ebx
movl $broj2, %ecx
movl $32, %edx
int $0x80

pushl baza2b
pushl $greska
pushl $broj2
call str_to_inter
addl $12, %esp

cmpl $1, greska
je prekoracenje
cmpl $2, greska
je pogresan_znak

#nakon ovoga resenje u %eax
movl %eax, broj2b

#unos rez baze
movl $4, %eax
movl $1, %ebx
movl $ulaz3, %ecx
movl $u3, %edx
int $0x80

#unos prve baze
movl $3, %eax
movl $0, %ebx
movl $baza3, %ecx
movl $32, %edx
int $0x80
decl %eax
movl %eax, b3 #duzina baze

#####pretvori u broj#####
movl $0, %eax
movl $baza3, %ecx
pre4:
cmpl $0, b3
je got4
decl b3
movb (%ecx), %ebx
subb $'0', %ebx
js pogresan_znak
cmpl $10, %ebx
jae pogresan_znak
movl $10, %edi
mull %edi
addl %ebx, %eax
incl %ecx
jmp pre4

got4:
movl %eax, baza3b
cmpl $2, %eax
jb prekoracenje
cmpl $16, %eax
ja prekoracenje

#saberi broj1b i broj2b
movl broj1b, %eax
addl broj2b, %eax
jc prekoracenje
movl %eax, zbir_dec
#u eax je rezultat

#zbir je u zbir_dec, baza je u baza3b
movl zbir_dec, %eax
movl $rezultat, %edi
movl $rezultat, %esi
movl baza3b, %ecx

andl %eax, %eax
jns preb
movb $'-', (%edi)
incl %eax
incl %esi

preb:
incl duz_r
movl $0, %edx
divl %ecx
addb $'0', %edx
movb %edx, (%edi)
cmpl $0, %eax
je okreni
incl %edi
jmp preb

okreni:
cmpl %edi, %esi
jae ispis_rezultata
movb (%edi), %eax
movb (%esi), %ebx
movb %eax, (%esi)
movb %ebx, (%edi)
incl %esi
decl %edi
jmp okreni

ispis_rezultata:
movl $4, %eax
movl $1, %ebx
movl $izlaz1, %ecx
movl $i1, %edx
int $0x80

movl $4, %eax
movl $1, %ebx
movl $rezultat, %ecx
movl duz_r, %edx
int $0x80
jmp kraj

pogresan_znak:
movl $4, %eax
movl $1, %ebx
movl $greska1, %ecx
movl $d1, %edx
int $0x80
jmp kraj

prekoracenje:
movl $4, %eax
movl $1, %ebx
movl $greska2, %ecx
movl $d2, %edx
int $0x80

kraj:
movl $1, %eax
movl $0, %ebx
int $0x80


str_to_inter:
pushl %ebp
movl %esp, %ebp
subl $4, %esp
pushl %esi
pushl %edi
pushl %ebx

movl 16(%ebp), %esi
cmpl $2, 16(%ebp)
jb greska31
movl 12(%ebp), %edi
movl $0, (%edi)
cmpl $36, 16(%ebp)
ja greska31
movl $0, %eax
movl $0, %ecx
movl 8(%ebp), %ebx #string
cmpb $0, (%ebx) #prazan
je greska21
cifra:
movb (%ebx), %ecx
cmpb $10, %ecx
je znak2
subb $'0', %ecx
js greska21
cmpl $10, %ecx
jae next
cmpb 16(%ebp), %ecx
jb cifra2
jae greska21
next:
cmpb $17, %ecx #sa A 65-48
jb greska21
subb $7, %ecx
cmpb $36, %ecx #ovde su velika slova u formatu od 11 do 36
jb cifra2
cmpb $42, %ecx #manje od 97
jb greska21
subb $32, %ecx
cmpb $36, %ecx #mala u formatu od 11 do 36
jb cifra2
jmp greska21

cifra2:
cmpl %esi, %ecx
jae greska21
mull %esi
jc greska11
addl %ecx, %eax
jc greska11
incl %ebx
jmp cifra

znak2:
jmp kraj1

greska31:
incl (%edi)

greska21:
incl (%edi)

greska11:
incl (%edi)

kraj1:
popl %ebx
popl %edi
popl %esi
movl %ebp, %esp
popl %ebp
ret
