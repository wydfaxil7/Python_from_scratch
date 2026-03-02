class Phone:
    def __init__(self, brand, model, **kwargs):
        super().__init__(**kwargs)
        self.brand = brand
        self.model = model

class Camera:
    def __init__(self, resolution, **kwargs):
        super().__init__(**kwargs)
        self.resolution = resolution

class Smartphone(Phone, Camera):
    def __init__(self, brand, model, resolution):
        super().__init__(brand=brand, model=model, resolution=resolution)

    def browse_internet(self):
        print("Browsing the internet")

s = Smartphone("Apple", "iPhone 13", "12MP")
print(s.brand)
print(s.model)  
s.browse_internet()
