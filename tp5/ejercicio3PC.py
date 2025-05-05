class Subject:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def emit(self, id_emitido):
        print(f"\nID emitido: {id_emitido}")
        for sub in self.subscribers:
            sub.notify(id_emitido)


class Observer:
    def __init__(self, my_id):
        self.my_id = my_id

    def notify(self, id_emitido):
        if self.my_id == id_emitido:
            print(f"Observer {self.my_id}: ¡ID coincidente!")


# Crea el subject y los observers
subject = Subject()

obs1 = Observer("AB12")
obs2 = Observer("CD34")
obs3 = Observer("EF56")
obs4 = Observer("GH78")

subject.subscribe(obs1)
subject.subscribe(obs2)
subject.subscribe(obs3)
subject.subscribe(obs4)

# emitir IDs (al menos 4 que coincidan)
ids_a_emitir = ["AB12", "ZZ99", "CD34", "XXXX", "EF56", "GH78", "YU01", "WXYZ"]

for id_ in ids_a_emitir:
    subject.emit(id_)
