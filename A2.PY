class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

BMW=vehicle("BMW",250,22)
print("Model Name:",BMW.name)
print("Model MAX Speed",BMW.max_speed)
print("Model Mileage:",BMW.mileage)
Audi=vehicle("Audi",240,18)
print("Model Name:",Audi.name)
print("Model Max speed:",Audi.max_speed)
print("Model Mileage:",Audi.mileage)