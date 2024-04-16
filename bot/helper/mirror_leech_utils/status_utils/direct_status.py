from bot.helper.ext_utils.status_utils import (
    MirrorStatus,
    get_readable_file_size,
    get_readable_time,
)

engine_ = f"Aria2 v{aria2.client.get_version()['version']}"

class DirectStatus:
    def __init__(self, listener, obj, gid):
        self._gid = gid
        self._obj = obj
        self.listener = listener
        self.engine = engine_

    def gid(self):
        return self._gid

    def progress_raw(self):
        try:
            return self._obj.processed_bytes / self.listener.size * 100
        except:
            return 0

    def progress(self):
        return f"{round(self.progress_raw(), 2)}%"

    def speed(self):
        return f"{get_readable_file_size(self._obj.speed)}/s"

    def name(self):
        return self.listener.name

    def size(self):
        return get_readable_file_size(self.listener.size)

    def eta(self):
        try:
            seconds = (self.listener.size - self._obj.processed_bytes) / self._obj.speed
            return get_readable_time(seconds)
        except:
            return "-"

    def status(self):
        if self._obj.download_task and self._obj.download_task.is_waiting:
            return MirrorStatus.STATUS_QUEUEDL
        return MirrorStatus.STATUS_DOWNLOADING

    def processed_bytes(self):
        return get_readable_file_size(self._obj.processed_bytes)

    def task(self):
        return self._obj
