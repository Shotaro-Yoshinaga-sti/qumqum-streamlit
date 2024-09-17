import os
from dotenv import load_dotenv
import qumcum_ble as qumcum

load_dotenv()


def robot_connection():
    ROBOT_ID = os.getenv("ROBOT_ID")
    [err, _] = qumcum.get_info()

    if err == -1:
        qumcum.connect(ROBOT_ID)
        [err, _] = qumcum.get_info()
        if err == -1:
            return False
        else:
            qumcum.motor_power_on(500)
            return True
    else:
        qumcum.motor_power_on(500)
        return True


def robot_disconnect():
    qumcum.motor_power_off()
    qumcum.end()
