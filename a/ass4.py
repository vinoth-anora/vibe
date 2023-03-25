car_makes = ['Honda', 'Toyota', 'Ford', 'Nissan', 'Hyundai']
car_models = ['Honda Civic', 'Honda Accord', 'Toyota Corolla', 'Toyota Camry', 'Ford Fusion', 'Ford Escape',
                  'Nissan Sentra', 'Hyundai Elantra']


def dictionary():
    global car_makes
    global car_models

    print("makes :\n", car_makes)
    print("Models :\n", car_models)
    list1 = []
    for i in car_makes:
        a = []
        for j in range(len(car_models)):
            if i in car_models[j].split():
                a.append(car_models[j])
        list1.append(a)
    dic = {}
    [dic.update({car_makes[i]:list1[i]})for i in range(len(list1))]
    return dic


print("Makes as keys and Models as values in dictionary :\n", dictionary(1))
