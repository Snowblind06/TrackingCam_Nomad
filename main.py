from __future__ import division
from getch import getche, getch
import time
import RPi.GPIO as GPIO
import Adafruit_PCA9685
from getch import getche, getch

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

PWM_init = 300  # angle about 90°
PWM_Min = 100  # angle about 0°
PWM_Max = 500  # angle about 180°

global actual_value_x
actual_value_x = PWM_init
global actual_value_y
actual_value_y = PWM_init


# Channel = 0   # PWM port number.


# Set the value of PWM to control rotation.
def servo_value(Channel, value):  # The value range is between 100-500.
    pwm.set_pwm(Channel, 0, value)


# Set the angle of pwm to control the rotation.
def servo_angle(Channel, angle):  # The angle range is between 0-180 .
    value = int(4096 * ((angle * 11) + 500) / 2000 + 0.5)  # Conversion angle value.
    pwm.set_pwm(Channel, 0, value)


def init_servo():

    global actual_value_x
    actual_value_x = PWM_init
    global actual_value_y

    actual_value_y = PWM_init
    servo_value(0, PWM_init)
    servo_value(1, PWM_init)

    print("servo initialisation successful")


def move_axis(axis, target_value, step):
    global actual_value_x
    global actual_value_y

    if axis == 0:
        while 110 <= actual_value_x <= 480:
            print("move_axis_x: actual_value_x before move is:")
            print(actual_value_x)

            while actual_value_x != target_value:
                actual_value_x = actual_value_x + step
                servo_value(axis, actual_value_x)
                time.sleep(0.05)
                print("move_axis_x: actual_value_x is now:")
                print(actual_value_x)

                if actual_value_x < 120:
                    init_servo()
                    time.sleep(0.05)
                    print("move_axis_x: 100 limit reached!")
                    main()

                elif actual_value_x > 480:
                    init_servo()
                    time.sleep(0.05)
                    print("move_axis_x: 500 limit reached! Go back")
                    main()

            break

    if axis == 1:
        while 140 <= actual_value_y <= 490:
            print("move_axis_x: actual_value_y before move is:")
            print(actual_value_y)

            while actual_value_y != target_value:
                actual_value_y = actual_value_y + step
                servo_value(axis, actual_value_y)
                time.sleep(0.05)
                print("move_axis_y: actual_value_y is now:")
                print(actual_value_y)

                if actual_value_y < 160:
                    init_servo()
                    time.sleep(0.05)
                    print("move_axis_y: 100 limit reached!")
                    main()

                elif actual_value_y > 490:
                    init_servo()
                    time.sleep(0.05)
                    print("move_axis_y: 500 limit reached! Go back")
                    main()

            break


def move_left():
    global actual_value_x
    target_value_x_plus = actual_value_x + 20
    move_axis(0, target_value_x_plus, 5)
    print(actual_value_x)
    print("moved LEFT")


def move_right():
    global actual_value_x
    target_value_x_moin = actual_value_x - 20
    move_axis(0, target_value_x_moin, -5)
    print(actual_value_x)
    print("moved RIGHT")


def move_up():
    global actual_value_y
    target_value_y_plus = actual_value_y + 20
    move_axis(1, target_value_y_plus, +5)
    print(actual_value_y)
    print("moved UP")


def move_down():
    global actual_value_y
    target_value_y_moin = actual_value_y - 20
    move_axis(1, target_value_y_moin, -5)
    print(actual_value_y)
    print("moved DOWN")


def main():
    print("Ready for manual control? Use Z or S to go Up or Down, and Q or D to go Left or Right")

    init_servo()

    while True:
        key = getche()

        if key == "d":
            move_left()
            continue

        elif key == "q":
            move_right()
            continue

        elif key == "z":
            move_up()
            continue

        elif key == "s":
            move_down()
            continue

        elif key == "m":
            init_servo()

        continue


if __name__ == '__main__':
    main()
