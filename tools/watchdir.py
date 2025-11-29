#!/usr/bin/env python3

import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyEventHandler(FileSystemEventHandler):
    def suff(self, event):
        return "/" if event.is_directory else ""

    def on_created(self, event):
        print(f"add: {event.src_path}{self.suff(event)}")

    def on_deleted(self, event):
        print(f"del: {event.src_path}{self.suff(event)}")

    def on_modified(self, event):
        print(f"mod: {event.src_path}{self.suff(event)}")

    def on_moved(self, event):
        print(f"mov: {event.src_path}{self.suff(event)} ==> {event.dest_path}{self.suff(event)}")


if __name__ == "__main__":
    path = sys.argv[1]
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)  # Set recursive=True to watch subdirectories
    observer.start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
