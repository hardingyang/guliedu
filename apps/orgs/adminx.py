import xadmin
from .models import OrgInfo,CityInfo,TeacherInfo

class CityInfoXadmin(object):
    list_display=['name','add_time']

#机构表管理
class OrgInfoXadmin(object):
    list_display=['image','name','course_num','study_num','love_num','click_num','cetegory','cityInfo']

#老师表管理
class TeacherInfoXadmin(object):
    list_display=['image','name','work_year','work_position','work_style','age','gender','love_num','click_num']

xadmin.site.register(CityInfo,CityInfoXadmin)
xadmin.site.register(OrgInfo,OrgInfoXadmin)
xadmin.site.register(TeacherInfo,TeacherInfoXadmin)