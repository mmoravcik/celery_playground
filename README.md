Playing around with celery and django

Installation
------------
* `pip install -r requirements.txt`
* `manage.py migrate`

Running Celery
--------------
* `redis-server` to start redis (or broker of your choice)
*  `celery -A celery_playground worker -l info`

Playground
----------
* `./manage.py shell`
* `from celery_playground.tasks import add,mul,xsum; from celery import group,chor`
* `res = group((add.s(i, i) for i in xrange(18)))()`  # run tasks in a group
* `res.get()`
* `res.ready(); res.failed()`
* `GroupResult.restore(res.id)`  # retrieve group later

