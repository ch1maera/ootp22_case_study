import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class Event(PatternMatchingEventHandler):
    def __init__(self, *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)

    def on_created(self, event):
        print('Event noticed')
        report_name = event.src_path.split('\\')[-1].split('.')[0]

        try:
            datetime.strptime(report_name, '%Y-%m-%d-%H-%M-%S')
            # Do Something Here. May need to use time.sleep() to allow the html report to fully populate
        except ValueError:
            # If the html doc that is generated doesn't follow the correct naming convetions (box scores, schedules, etc...)
			# it should throw a ValueError and the script should just ignore it then.


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = # Path to your OOTP saved_games directory
    event_handler = Event(patterns=['*.html'])
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
