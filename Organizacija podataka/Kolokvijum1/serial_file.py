import os
from binary_file import BinaryFile

class SerialFile(BinaryFile):
    def __init__(self, filename, record, blocking_factor, empty_key=-1):
        BinaryFile.__init__(self, filename, record, blocking_factor, empty_key)

    def init_file(self): #inicijalizacija praznog fajla
        with open(self.filename, "wb") as f:
            block = self.blocking_factor*[self.get_empty_rec()]
            self.write_block(f, block)

    def insert_record(self, rec):
        # if self.find_by_id(rec.get("evidencioni broj")):
        #     print("Vec postoji u fajlu")
        #     return False
        
        with open(self.filename, "rb+") as f:
            f.seek(-self.block_size, 2) #citanje poslednjeg bloka
            block = self.read_block(f)

            for i in range(self.blocking_factor):
                if block[i].get("evidencioni broj") == self.empty_key: #trazimo prvi prazan
                    block[i] = rec
                    break
            
            i += 1

            if i == self.blocking_factor: #jel popunjen blok
                f.seek(-self.block_size, 1)
                self.write_block(f, block)
                block = self.blocking_factor*[self.get_empty_rec()]
                self.write_block(f, block)
            else:
                block[i] = self.get_empty_rec()
                f.seek(-self.block_size, 1)
                self.write_block(f, block)
            
        return True

    def __is_last(self, block):
        for i in range(self.blocking_factor):
            if block[i].get("evidencioni broj") == self.empty_key:
                return True
        return False

    def file_to_array(self):
        result = []

        with open(self.filename, "rb") as f:
            while True:
                block = self.read_block(f)

                if not block:
                    break

                for b in block:
                    if b["evidencioni broj"] == -1:
                        break
                    result.append({
                            "evidencioni broj" : int(b.get("evidencioni broj")),
                            "naziv projekcije" : b.get("naziv projekcije").replace("\x00", ""),
                            "datum" : b.get("datum"),
                            "vreme" : b.get("vreme"),
                            "oznaka sale" : b.get("oznaka sale"),
                            "trajanje projekcije" : int(b.get("trajanje projekcije")),
                            "status" : int(b.get("status"))
                        })

            return result

    def print_file(self):
        i = 0
        with open(self.filename, "rb") as f:
            while True:
                block = self.read_block(f)

                if not block: #dosli do kraja
                    break

                i += 1
                print("Blok adrese {}".format(hex(id(i))))
                self.print_block(block)

    def find_by_id(self, id):
        i = 0
        with open(self.filename, "rb") as f:
            while True:
                block = self.read_block(f)

                for j in range(self.blocking_factor):
                    if block[j].get("evidencioni broj") == id:
                        return (i, j)
                    elif block[j].get("evidencioni broj") == self.empty_key: #onda kraj
                        return None
                
                i += 1

    def delete_by_id(self, id):
        found = self.find_by_id(id)

        if not found:
            return

        block_idx = found[0]
        rec_idx = found[1]
        next_block = None

        with open(self.filename, "rb+") as f:
            while True:
                f.seek(block_idx*self.block_size)
                block = self.read_block(f)

                i = rec_idx
                while i < self.blocking_factor-1: #brisemo tako sto sve pomeramo
                    block[i] = block[i+1]
                    i += 1

                if self.__is_last(block): #upisemo i gotovo
                    f.seek(-self.block_size, 1)
                    self.write_block(f, block)
                    break

                next_block = self.read_block(f) #ako nije poslednji
                block[self.blocking_factor-1] = next_block[0]
                f.seek(-2*self.block_size, 1)
                self.write_block(f, block)

                block_idx += 1
                rec_idx = 0

        if next_block and next_block[0].get("evidencioni broj") == self.empty_key: #ako smo oslobodili skroz poslednji blok, oslobodimo
            os.ftruncate(os.open(self.filename, os.O_RDWR), block_idx*self.block_size)


