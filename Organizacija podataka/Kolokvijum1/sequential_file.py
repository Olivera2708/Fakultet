import os
from binary_file import BinaryFile

class SequentialFile(BinaryFile):
    def __init__(self, filename, record, blocking_factor, empty_key=-1):
        BinaryFile.__init__(self, filename, record, blocking_factor, empty_key)

    def getFileName(self):
        return self.filename

    def init_file(self): #inicijalizacija praznog fajla
        with open(self.filename, "wb") as f:
            block = self.blocking_factor*[self.get_empty_rec()]
            self.write_block(f, block)

    def __find_in_block(self, block, rec):
        for j in range(self.blocking_factor):
            if block[j].get("evidencioni broj") == self.empty_key or block[j].get("evidencioni broj") > rec.get("evidencioni broj"):
                return (True, j)
        return (False, None)

    def insert_record(self, rec):
        #provera da li vec postoji sa tim id
        if (self.filename != "promena_sek.bin"):
            if self.find_by_id(rec.get("evidencioni broj")):
                print("Vec postoji slog sa zadatim evidencionim brojem")
                return True, "Vec postoji evidencioni broj u datoteci"

        with open(self.filename, "rb+") as f:
            while True:
                block = self.read_block(f)
                if not block: #kraj fajla
                    break

                last = self.__is_last(block)
                here, j = self.__find_in_block(block, rec)

                if not here: #ovde se ne nalazi mesto za upis
                    continue
            
                tmp_rec = block[self.blocking_factor - 1] #poslednja rec
                for k in range(self.blocking_factor-1, j, -1):
                    block[k] = block[k-1] #pomeranje, pravimo mesta
                block[j] = rec #dodamo rec
                rec = tmp_rec #sada moramo i ovu sledecu da premestimo

                f.seek(-self.block_size, 1)
                self.write_block(f, block) #sada upisemo blok

                if last and block[self.blocking_factor-1].get("evidencioni broj") != self.empty_key: #moramo da proverimo da li imamo na kraju prazan slog
                    block = self.blocking_factor*[self.get_empty_rec()]
                    self.write_block(f, block)

        return False, ""

    def __is_last(self, block):
        for i in range(self.blocking_factor):
            if block[i].get("evidencioni broj") == self.empty_key:
                return True
        return False

    def print_file(self):
        i = 0
        with open(self.filename, "rb") as f:
            while True:
                block = self.read_block(f)

                if not block:
                    return None

                i += 1
                print("Blok adrese {}".format(hex(id(i))))
                self.print_block(block)

    def find_by_id(self, id):
        i = 0
        with open(self.filename, "rb") as f:
            while True:
                block = self.read_block(f)

                if not block:
                    return None

                for j in range(self.blocking_factor):
                    if (block[j].get("evidencioni broj") == id):
                        return (i, j) #blok, slog
                    if (block[j].get("evidencioni broj") > id):
                        return None
                    
                i += 1
    
    def delete_by_id(self, id):
        found = self.find_by_id(id)

        if not found:
            print("Nije moguce obrisati slog, jer evidencioni broj ne postoji")
            return True, "Nema evidencionog broja u datoteci"

        block_ind = found[0] #indeks bloka
        rec_ind = found[1] #indeks sloga u bloku
        next_block = None

        with open(self.filename, "rb+") as f:
            while True:
                f.seek(block_ind*self.block_size) #pozicioniramo se kod bloka koji sadzi dati id
                block = self.read_block(f) 

                for i in range(rec_ind, self.blocking_factor-1):
                    block[i] = block[i+1] #pomeramo sve

                if self.__is_last(block): #ako poslednji blok pun
                    f.seek(-self.block_size, 1)
                    self.write_block(f, block)
                    break

                next_block = self.read_block(f)
                block[self.blocking_factor-1] = next_block[0]
                f.seek(-2*self.block_size, 1)
                self.write_block(f, block)

                block_ind += 1
                rec_ind = 0
        
        if next_block and next_block[0].get("evidencioni broj") == self.empty_key:
            os.ftruncate(os.open(self.filename, os.O_RDWR), block_ind*self.block_size) 

        return False, ""

    
    def update_file(self, novi):
        found = self.find_by_id(novi["evidencioni broj"])

        if not found:
            print("Nije mmoguce obrisati slog, jer evidencioni broj ne postoji")
            return True, "Nema evidencionog broja u datoteci"

        block_ind = found[0] #indeks bloka
        rec_ind = found[1] #indeks sloga u bloku

        with open(self.filename, "rb+") as f:
            f.seek(block_ind*self.block_size) #pozicioniramo se kod bloka koji sadzi dati id
            block = self.read_block(f)
            block[rec_ind] = novi

            f.seek(-self.block_size, 1)
            self.write_block(f, block) #sada upisemo blok

        return False, ""
        

    
    def read_blocks(self):
        blocks = []
        with open(self.filename, "rb") as f:
            while True:
                block = self.read_block(f)

                if not block:
                    break
                blocks.append(block)

        return blocks
