# Author : Ryanyi
# Creation time : 2022/12/14
# Data maintainer : Ryanyi

from kafka import KafkaProducer

import json
import time
import random

# kakfa topic
TOPIC = "test1011"

while True:
    producer = KafkaProducer(bootstrap_servers="192.168.163.143:9092", value_serializer=lambda v: json.dumps(v).encode('utf-8'),api_version=(0, 10, 1))
    send_list = []
    timestamp = int(round(time.time() * 1000))

    # 监控对象
    monitor_obj_list = ["zj_Apa"]
    monitor_obj_id_list = [4678,4681]
    for obj_str in monitor_obj_list:
        for i in monitor_obj_id_list:
            send_msg = {
                "bk_obj_id": obj_str,
                "bk_inst_id": i,
                "instance_name": "{}_{}".format(obj_str, i),
                "data": [
                    {
                        "metrics": {"{obj_str}1".format(obj_str=obj_str):  random.randint(0,100), "{obj_str}2".format(obj_str=obj_str):  random.randint(0,100)},
                        "dimension": {"table_id":  "muyitest1"},
                        "timestamp": timestamp
                    },{
                        "metrics": {"{obj_str}_database_metric1".format(obj_str=obj_str):  random.randint(0,100), "{obj_str}_database_metric2".format(obj_str=obj_str):  random.randint(0,100)},
                        "dimension": {"database_name":  "muyitest2"},
                        "timestamp": timestamp
                    },
                ]
            }
            producer.send(TOPIC, send_msg)
    producer.flush()
    time.sleep(60)
