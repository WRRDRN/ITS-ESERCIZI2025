def make_car(manufacturer, model, blue, **kwargs):
    car_info:dict = {'manufacturer': manufacturer, 'model': model, 'color':blue}
    
    for key, value in kwargs.items():
        car_info[key] = value
    return car_info

car = make_car ('subaru', 'outback', 'blue', tow_package=True)

print(car)