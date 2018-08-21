import psutil
import os
from hurry.filesize import size
from flask_restful import Resource


class Stat(Resource):
    def get(self):
        result = disk_statistics()
        return result
#Displays all available drives and brief statistics
def disk_statistics():
    usage_list = []
    for partition in psutil.disk_partitions():
        # skip empty cd-rom
        if os.name == 'nt':
            if 'cdrom' in partition.opts or partition.fstype == '':
                continue
        usage = psutil.disk_usage(partition.mountpoint)
        partition_info = {"Drive": partition.mountpoint,
                              "total": size(usage.total), "used": size(usage.used), "free": size(usage.free),
                              "percent": usage.percent}
        usage_list.append(dict(partition_info))
    return usage_list
