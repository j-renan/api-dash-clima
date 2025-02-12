from visual_crossing.usecase.get_clima_by_city_usecase import GetClimaByCityUseCase


class VisualCrossingController:
    def __init__(self):
        self.get_clima_usecase = GetClimaByCityUseCase()

    def get_clima_by_city(self, city: str):
        return self.get_clima_usecase.execute(city)


