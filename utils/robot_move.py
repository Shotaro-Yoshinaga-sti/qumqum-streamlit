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


def robot_arms_up_dance(num, speed=1000):
    """
    両手足を上げ下げするダンス

    Args:
        num (int): 踊る回数
        speed(int): モーター動作時間(単位:msec)
    """
    # モーター電源ON
    qumcum.motor_power_on(500)

    for _ in range(num):
        qumcum.motor_angle_multi_time(70, 70, 70, 70, 70, 70, 70, speed)
        qumcum.motor_start()
        qumcum.motor_angle_multi_time(0, 90, 90, 90, 90, 90, 180, speed)
        qumcum.motor_start()

        qumcum.motor_angle_multi_time(110, 110, 110, 110, 110, 110, 110, speed)
        qumcum.motor_start()
        qumcum.motor_angle_multi_time(0, 90, 90, 90, 90, 90, 180, speed)
        qumcum.motor_start()

    # モーター電源OFF
    qumcum.motor_power_off()


def robot_kubifuri_kyoshu():
    """
    首振り挙手

    Args:
        なし
    """
    # モーター電源ON
    qumcum.motor_power_on(500)

    qumcum.voice("hajimeruyo-")
    qumcum.wait(1)
    qumcum.motor_angle_time(4, 120, 100)
    qumcum.motor_set_pos(1, 180)
    qumcum.motor_start()
    qumcum.voice("i-chi")
    qumcum.motor_angle_time(4, 60, 100)
    qumcum.motor_set_pos(1, 0)
    qumcum.motor_start()
    qumcum.motor_angle_time(4, 120, 100)
    qumcum.motor_set_pos(1, 180)
    qumcum.motor_start()
    qumcum.voice("ni-")
    qumcum.motor_angle_time(4, 60, 100)
    qumcum.motor_set_pos(1, 0)
    qumcum.motor_start()
    qumcum.motor_angle_time(4, 120, 100)
    qumcum.motor_set_pos(1, 180)
    qumcum.motor_start()
    qumcum.voice("sa-n")
    qumcum.motor_angle_time(4, 60, 100)
    qumcum.motor_set_pos(1, 0)
    qumcum.motor_start()
    qumcum.motor_angle_time(4, 90, 100)
    qumcum.motor_start()

    # モーター電源OFF
    qumcum.motor_power_off()


def robot_banzai(num, speed=300):
    """
    バンザイ

    Args:
        num (int): バンザイする回数
        speed(int): モーター動作時間(単位:msec)
    """
    # モーター電源ON
    qumcum.motor_power_on(speed)

    for _ in range(num):
        qumcum.motor_angle_multi_time(180, 90, 60, 90, 120, 90, 0, speed)
        qumcum.motor_start()
        qumcum.voice_speed(100)
        qumcum.voice('banzai')

        qumcum.motor_angle_multi_time(0, 90, 90, 90, 90, 90, 180, speed)
        qumcum.motor_start()

    # モーター電源OFF
    qumcum.motor_power_off()


def robot_arms_shake_dance(num, speed=300):
    """
    首を左右に、左右の手を上下に振るダンス
    
    Args:
        num (int): 手を上下に振る回数
        speed(int): モーター動作時間(単位:msec)
    """
    # モーター電源ON
    qumcum.motor_power_on(speed)

    for _ in range(num):
        qumcum.motor_angle_multi_time(45, 90, 90, 60, 90, 90, 45, speed)
        qumcum.motor_start()
        qumcum.motor_angle_multi_time(135, 90, 90, 120, 90, 90, 135, speed)
        qumcum.motor_start()
    qumcum.motor_angle_multi_time(0, 90, 90, 90, 90, 90, 180, speed)
    qumcum.motor_start()

    # モーター電源OFF
    qumcum.motor_power_off()


def robot_jidanda(num, speed=300):
    """
    右足で地団駄を踏む

    Args:
        num (int): 地団駄を踏む回数
        speed(int): モーター動作時間(単位:msec)
    """
    # モーター電源ON
    qumcum.motor_power_on(speed)

    for _ in range(num):
        qumcum.motor_angle_multi_time(90, 90, 65, 90, 90, 90, 90, speed)
        qumcum.motor_start()

        qumcum.motor_angle_multi_time(0, 90, 90, 90, 90, 90, 180, speed)
        qumcum.motor_start()
        qumcum.voice('kuyashii')

    # モーター電源OFF
    qumcum.motor_power_off()
