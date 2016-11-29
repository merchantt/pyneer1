import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango.settings')

import django
django.setup()
from rango.models import Notice, UserProfile, Compared


def add_compared(user,title,url):
    c = Compared(user=user,title=title,url=url)
    c.save(force_insert=True)
    return c

userprofiles = UserProfile.objects.all()


notices = Notice.objects.filter(unread=True)
for notice in notices:
    for user in userprofiles:
        keywords = [user.keyword1, user.keyword2]
        for keyword in keywords:
            if keyword in notice.title:
                url = "http://www.skku.edu/new_home/campus/skk_comm/notice_view.jsp?boardNum="
                url += str(notice.num)
                add_compared(user.user.id, notice.title, url)
                break

