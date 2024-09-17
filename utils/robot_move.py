import qumcum_ble as qumcum


# 立ち姿リセット
def robot_reset():
    qumcum.motor_angle_multi_time(0, 90, 90, 90, 90, 90, 180, 600)
    qumcum.motor_start(True)


# 万歳動作
def robot_cheers():
    qumcum.motor_angle_multi_time(180, 90, 90, 90, 90, 90, 0, 600)
    qumcum.motor_start(True)
    qumcum.wait(2)


# 拒否動作　首を振る
def robot_denial():
    for _ in range(4):
        qumcum.motor_angle_time(4, 45, 1)
        qumcum.motor_start()

        qumcum.motor_angle_time(4, 135, 1)
        qumcum.motor_start()

    qumcum.motor_angle_time(4, 90, 1)
    qumcum.motor_start()
    qumcum.wait(3)


# ロボットの歩行動作
def robot_walk():
    qumcum.motor_set_pos(5, 55)
    qumcum.motor_start(True)
    qumcum.wait(1)
    qumcum.motor_angle_time(3, 110, 750)
    qumcum.motor_start(True)
    qumcum.wait(1)
    qumcum.motor_set_pos(2, 65)
    qumcum.motor_start(True)
    qumcum.wait(1)

    qumcum.motor_angle_multi_time(0, 70, 90, 90, 90, 90, 180, 600)
    qumcum.motor_start(True)
    qumcum.wait(1)
    qumcum.motor_set_pos(2, 90)
    qumcum.motor_start(True)
    qumcum.wait(1)

    qumcum.motor_set_pos(3, 125)
    qumcum.motor_start(True)
    qumcum.wait(1)
    qumcum.motor_angle_time(5, 70, 750)
    qumcum.motor_start(True)
    qumcum.wait(1)
    qumcum.motor_set_pos(6, 115)
    qumcum.motor_start(True)
    qumcum.wait(1)

    qumcum.motor_angle_multi_time(0, 90, 90, 90, 90, 115, 180, 600)
    qumcum.motor_start(True)
    qumcum.wait(1)
    qumcum.motor_set_pos(6, 90)
    qumcum.motor_start(True)
    qumcum.wait(1)


def robot_pose_hans_up_left():
    qumcum.motor_set_pos(5, 55)
    qumcum.motor_start(True)

    qumcum.motor_angle_time(3, 110, 1000)
    qumcum.motor_start(True)
    qumcum.wait(1)

    qumcum.motor_set_pos(7, 0)
    qumcum.motor_start(True)
    qumcum.wait(5)

    qumcum.motor_angle_multi_time(0, 90, 90, 90, 90, 90, 180, 600)
    qumcum.motor_start(True)
    qumcum.wait(1)


def robot_pose_hans_up_right():
    qumcum.motor_angle_time(3, 125, 500)
    qumcum.motor_start(True)

    qumcum.motor_angle_time(5, 70, 2000)
    qumcum.motor_start(True)
    qumcum.wait(2)

    qumcum.motor_set_pos(1, 180)
    qumcum.motor_start(True)
    qumcum.wait(5)

    qumcum.motor_angle_multi_time(0, 90, 90, 90, 90, 90, 180, 600)
    qumcum.motor_start(True)
    qumcum.wait(1)


def robot_turn_right():
    for i in range(4):
        qumcum.motor_set_pos(5, 55)
        qumcum.motor_start(True)
        qumcum.wait(1)
        qumcum.motor_angle_time(3, 110, 750)
        qumcum.motor_start(True)
        qumcum.wait(1)
        qumcum.motor_set_pos(2, 65)
        qumcum.motor_start(True)
        qumcum.wait(1)

        qumcum.motor_angle_multi_time(0, 70, 90, 90, 90, 90, 180, 600)
        qumcum.motor_start(True)
        qumcum.wait(1)
        qumcum.motor_set_pos(2, 90)
        qumcum.motor_start(True)
        qumcum.wait(1)


def robot_turn_left():
    for i in range(4):
        qumcum.motor_set_pos(3, 125)
        qumcum.motor_start(True)
        qumcum.wait(1)
        qumcum.motor_angle_time(5, 70, 750)
        qumcum.motor_start(True)
        qumcum.wait(1)
        qumcum.motor_set_pos(6, 115)
        qumcum.motor_start(True)
        qumcum.wait(1)

        qumcum.motor_angle_multi_time(0, 90, 90, 90, 90, 115, 180, 600)
        qumcum.motor_start(True)
        qumcum.wait(1)
        qumcum.motor_set_pos(6, 90)
        qumcum.motor_start(True)
        qumcum.wait(1)
