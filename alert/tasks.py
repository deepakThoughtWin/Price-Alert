from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime
from celery.utils.log import get_task_logger
from alert.utils import get_realtime_price,send_alert_email,trigger,get_alert

logger = get_task_logger(__name__)


@shared_task(name = "get_realtime_price_tasks")
def get_realtime_price_tasks():
    """
    get_realtime_price_tasks: used for getting real time current price of btc

    Match the price

    Send the Alert
    
    """
    data=get_realtime_price()
    price=data['current_price']
    name=data['name']

    print(f"Fetching Price...! of {name}")
    logger.info(f"fetched Price of Bitcoin!! is {price}")
    # alerts=Alert.objects.filter(price=price,status='created')
    alerts=get_alert(price)
    if alerts.exists():
        print(f"{len(alerts)} Alert Matched...!")
        receivers=[alert.user.email for alert in alerts]
        alert=[alert.id for alert in alerts]

        if len(receivers)>0:
            send_alert_to_user.delay(receivers,price)
            print(f"Alert Sent To..! {receivers}")
            is_triggered=trigger(alert)
            print(is_triggered)

    else:
        print(f"No Alert Match...!")

    return 'Success'

    


@shared_task(name = "send_alert")
def send_alert_to_user(receivers,price):
    """
    
    send_alert_to_user: Sending Alert Using Email

    """
    is_sent=send_alert_email(receivers,price)
    return is_sent
