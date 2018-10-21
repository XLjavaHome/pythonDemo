import time

import pywifi
from pywifi import const
def testwifi(ssidname, password):
    wifi = pywifi.PyWiFi()  # 抓取网卡接口
    ifaces = wifi.interfaces()[0]  # 获取网卡
    ifaces.disconnect()  # 断开无限网卡连接
    profile = pywifi.Profile()  # 创建wifi连接文件
    profile.ssid = ssidname  # 定义wifissid
    profile.auth = const.AUTH_ALG_OPEN  # 网卡的开放
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
    profile.cipher = const.CIPHER_TYPE_CCMP  ##加密单元
    profile.key = password  # wifi密码
    ifaces.remove_all_network_profiles()  # 删除其他所有配置文件
    # const.IFACE_CONNECTED
    tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件
    ifaces.connect(tmp_profile)  # 连接wifi
    time.sleep(5)
    if ifaces.status() == const.IFACE_CONNECTED:
        return True
    else:
        # print("[-]WiFi connection failure!")
        return False
    # ifaces.disconnect()#断开连接
    # time.sleep(1)
    return True
print(testwifi('Xiaomi_4221', '66046604'))
