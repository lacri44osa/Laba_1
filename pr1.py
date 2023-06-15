class Komp:
    def __init__(self, processor, ram, video_card, storage):
        self._processor = processor
        self._ram = ram
        self._video_card = video_card
        self._storage = storage

    @property
    def processor(self):
        return self._processor

    @processor.setter
    def processor(self, processor):
        self._processor = processor

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, ram):
        self._ram = ram

    @property
    def video_card(self):
        return self._video_card

    @video_card.setter
    def video_card(self, video_card):
        self._video_card = video_card

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, storage):
        self._storage = storage

komp = Komp("Intel Core i7", "16 GB", "NVIDIA GeForce RTX 3070", "512 GB SSD")
print(komp.processor)
print(komp.ram) 
print(komp.video_card) 
print(komp.storage) 

komp.processor = "AMD Ryzen 9"
komp.ram = "32 GB"
komp.video_card = "AMD Radeon RX 6700 XT"
komp.storage = "1 TB NVMe SSD"
print(komp.processor) 
print(komp.ram)
print(komp.video_card) 
print(komp.storage)
