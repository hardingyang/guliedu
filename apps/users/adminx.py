import xadmin
from .models import BannerInfo,EmailVerifyCode
class BannerInfoXadmin(object):
    #这里面和原生django的admin语法是一样的，不过这里面不能提示了
    list_display=['image','url','add_time',]
    #搜索框
    search_fields=['image','url']
    #过滤器
    list_filter=['image','url']
class EmailVerifyCodeXadmin(object):
    list_display=['code','email','send_type',]

xadmin.site.register(BannerInfo,BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeXadmin)