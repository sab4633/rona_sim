import Blob

class place:
    visitors = []
    quantity = 0;



    def visiting(self, aBlob):
        self.visitors.append(aBlob)
        self.quantity+=1

    def end_of_cycle(self):
        if(self.quantity>1):
            for i in self.visitors:
                for j in self.visitors:
                    if(i!=j):
                        i.infect(i,j)



    def end_of_day(self):
        self.visi



