import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import black
import isort

logging.basicConfig(level=logging.INFO)

class FormatOnSaveHandler(FileSystemEventHandler):
    def __init__(self, formatter):
        self.formatter = formatter

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            logging.info(f'File modified: {event.src_path}')
            self.formatter.format_file(event.src_path)

class Formatter:
    def __init__(self, black_args=None, isort_args=None):
        self.black_args = black_args or []
        self.isort_args = isort_args or []

    def format_file(self, file_path):
        try:
            isort.file(file_path, *self.isort_args)
            black.format_file(file_path, *self.black_args)
            logging.info(f'Formatted file: {file_path}')
        except Exception as e:
            logging.error(f'Error formatting file {file_path}: {e}')

class DirectoryWatcher:
    def __init__(self, watch_directory, formatter):
        self.watch_directory = watch_directory
        self.formatter = formatter
        self.event_handler = FormatOnSaveHandler(formatter)
        self.observer = Observer()

    def start(self):
        self.observer.schedule(self.event_handler, self.watch_directory, recursive=True)
        self.observer.start()
        logging.info('Started watching directory: {}'.format(self.watch_directory))

    def stop(self):
        self.observer.stop()
        logging.info('Stopped watching directory: {}'.format(self.watch_directory))

def format_on_save(watch_directory, black_args=None, isort_args=None):
    formatter = Formatter(black_args, isort_args)
    watcher = DirectoryWatcher(watch_directory, formatter)
    try:
        watcher.start()
        while True:
            pass  # Run indefinitely
    except KeyboardInterrupt:
        watcher.stop()