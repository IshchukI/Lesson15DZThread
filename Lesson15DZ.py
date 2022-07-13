import threading
import random
import time

car_speed = random.randint(30, 170)
train_speed = random.randint(70, 110)
s_car = 0
s_train = 0
s_cross_roads = train_speed*10/3.6


def car_movement():
    global s_car
    for i in range(0, 30):
        s_car += car_speed/3.6
        if i == 10:
            print(f">>>>>>>>>>from car thread<<distance to сrossroad is: intersection point = <{s_cross_roads}>, car movement = <{s_car}>, train movement = <{s_train}>, dif = {s_train - s_car}>")
            if (s_car - s_cross_roads) < 50:
                print(">>>>>>>>>>car thread waiting for the train to pass")
                time.sleep(5)
                print(">>>>>>>>>>train passed")
        time.sleep(0.3)
        print(f"Пройденный путь car:{round(s_car, 2)}")



def train_movement():
    global s_train
    for i in range(0, 30):
        s_train += train_speed/3.6
        time.sleep(0.3)
        print(f"---Пройденній путь train:{s_train}")


print(f"car speed: <{car_speed}>, train speed: <{train_speed}>")

th1 = threading.Thread(target=car_movement, name="car thread")
th2 = threading.Thread(target=train_movement, name="train thread")

th1.start()
th2.start()


