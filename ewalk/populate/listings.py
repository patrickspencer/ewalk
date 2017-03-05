import time
import sched
import datetime
from stubhub.models.queueitem import QueueItem
from stubhub.models import dbsession

# This starts a scheduler. Every 6 seconds it runs the command
# add_listings_to_db_and_log(event_id) where event_id is taken from the queue_items
# table in the database. When there are no more queue items left, clear all
# rows in the queue_items table so it's clean.
#
# We have to wait 6 seconds between each request because Stubhub
# will only let non-paying users make 10 queries a minute
s = sched.scheduler(time.time, time.sleep)

def calc_time_to_finish(num_events):
    """
    Returns a string of the form "54.20". It's a string because the
    truncate function used turns it into one.

    It takes about 7 seconds on average to load an event.
    time to complete fetch = number of active events * 7 seconds
    divided by 60 seconds in a minutes
    """
    seconds = num_events * 7
    if seconds > 60:
        minutes = seconds // 60
        seconds %= 60
        time_string = '%s:%s' % (minutes, seconds)
        return datetime.datetime.strptime(time_string, '%M:%S')\
            .strftime('%M minutes and %S seconds')
    else:
        return datetime.datetime.strptime(str(seconds), '%S')\
            .strftime('%S seconds')

# status 0 means not started. This is supposing we only have to options for
# status i.e. 0 for not started and 1 for completed. If we add three
# possibilities i.e. 0 for not started, 1 for active, and 2 for completed then
# we should replace ==0 with !=2

def deactivate_queue_item(queue_item_id):
    dbsession.query(QueueItem).filter(QueueItem.id == queue_item_id)\
            .update({QueueItem.status: 1})
    dbsession.commit()

all_queue_items = dbsession.query(QueueItem)
queue_items_total_count = all_queue_items.count()

def do_something(sc):
    results = dbsession.query(QueueItem)\
            .filter(QueueItem.status == 0)

    if results.count() == 0:
        return
    else:
        next_item = results.first()
        items_left = results.count()
        items_completed = queue_items_total_count - results.count()
        minutes_left = calc_time_to_finish(items_left)
        optional_string = " item %s of %s, about %s left -" %\
                (items_completed+1, queue_items_total_count, minutes_left)
        add_listings_to_db_and_log(stubhub_event_id=next_item.stubhub_id,
                optional_string=optional_string)
        deactivate_queue_item(next_item.id)

        # delete all rows in queue_items when we have no more to do
        if results.count() == 0:
            for queue_item in all_queue_items.all():
                dbsession.delete(queue_item)
        dbsession.commit()

    sc.enter(5.5, 1, do_something, (sc,))

if queue_items_total_count == 0:
    print('No items in queue. Run \'python populate/makequeue.py\' to populate queue')
else:
    results = dbsession.query(QueueItem)\
            .filter(QueueItem.status==0)
    print("Number of items in queue: %s" % queue_items_total_count)
    print("Estimated time to finish: about %s" % calc_time_to_finish(results.count()))
    s.enter(0, 1, do_something, (s,))
    s.run()
