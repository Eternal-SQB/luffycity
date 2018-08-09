import json
import redis

from django.conf import settings
from django.shortcuts import HttpResponse

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from api.utils.response import BaseResonse
from django.db import transaction

from api import models

# class ShopingCarView(ViewSetMixin,APIView,BaseResonse):
#
#     def create(self,request,*args,**kwargs):
#         """
#         1. 接受用户选中的课程ID和价格策略ID
#         2. 判断合法性
#             - 课程是否存在？
#             - 价格策略是否合法？
#         3. 把商品和价格策略信息放入购物车 SHOPPING_CAR
#
#         注意：用户ID=1
#         """
#         try:
#             ret = BaseResonse()
#             print(request.data)
#             course_id = int(request.data.get("course_id"))
#             price_id = int(request.data.get("price_id"))
#
#             obj = models.Course.objects.filter(id=course_id).first()
#             if obj:
#                 id_list = obj.price_policy.values_list("id")
#                 for price_policy_id in id_list:
#                     if price_id in price_policy_id:
#                         price_policy_list = obj.price_policy.values("id", "valid_period", "price")
#                         choice_price_policy = models.PricePolicy.objects.filter(id=price_id).values("id", "valid_period", "price")
#                         with transaction.atomic():
#                             global SHOPPING_CAR
#                             SHOPPING_CAR = {
#                                 1:{
#                                     course_id: {
#                                         "name": obj.name,
#                                         "course_type": obj.get_course_type_display(),
#                                         "brief": obj.brief,
#                                         "level": obj.get_level_display(),
#                                         "choice_price_policy": choice_price_policy,
#                                         "price_policy": price_policy_list,
#                                     }
#                                 }
#                             }
#                             ret.data = SHOPPING_CAR
#                             print(SHOPPING_CAR)
#                         return Response(ret.dict)
#             ret.code = 401
#             ret.error = "购物车数据有误"
#             print(SHOPPING_CAR)
#             return Response(ret.dict)
#         except Exception as e:
#             print(e)
#             ret.code = 500
#             ret.error = "请传入正确的数字"
#             return Response(ret.dict)



CONN = redis.Redis(host='192.168.11.122', port=6379)

USER_ID=1

class ShoppingCarView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret=BaseResonse()
        try:
            shopping_car_course_list=[]
            pattern=settings.LUFFY_SHAOPPING_CAR %(USER_ID,'*')

            user_key_list =CONN.keys(pattern)

            for key in user_key_list:
                temp={
                    'id':CONN.hget(key,'id').decode('utf-8'),
                    'name':CONN.hget(key,'name').decode('utf-8'),
                    'img':CONN.hget(key,'img').decode('utf-8'),
                    'default_price_id':CONN.hget(key,'default_price_id').decode('utf-8'),
                    'price_policy_dict':json.loads(CONN.hget(key,'price_policy_dict').decode('utf-8')),
                }
                shopping_car_course_list.append(temp)

                ret.data=shopping_car_course_list
        except Exception as e:
            ret.code=105
            ret.error='获取购物车失败'

        return Response(ret.dict)



    def create(self,request,*args,**kwargs):
        ret=BaseResonse()

        course_id=request.data.get('course_id')
        policy_id=request.data.get('policyid')

        course=models.Course.objects.filter(id=course_id).first()

        if not course:
            return Response({'code':101,'erroe':'课程不存在'})

        price_policy_queryset=course.price_policy.all()
        price_policy_dict={}
        for item in  price_policy_queryset:
            temp={
                'id':item.id,
                'price':item.price,
                'vaild_period':item.vaild_period,
                'vaild_period_display':item.get_vaild_period_display,
            }
            price_policy_dict[item.id]=temp
        if policy_id not in price_policy_dict:
            return Response({'code':1002,'error':'价格策略错误'})


        pattern=settings.LUFFY_SHAOPPING_CAR %(USER_ID,'*')
        keys=CONN.keys(pattern)
        if keys and len(keys) >=1000:
            return Response({'code':109,'error':'购物车东西太多，先去结算再进行购买..'})

        key =settings.LUFFY_SHAOPPING_CAR %(USER_ID ,course_id)

        CONN.hset(key, 'id', course_id)
        CONN.hset(key, 'name', course.name)
        CONN.hset(key, 'img', course.course_img)
        CONN.hset(key, 'default_price_id', policy_id)
        CONN.hset(key, 'price_policy_dict', json.dumps(price_policy_dict))

        CONN.expire(key, 20 * 60)

        return Response({'code': 10000, 'data': '购买成功'})


    def destory(self,request,*args,**kwargs):
        response = BaseResonse()
        try:
            courseid = request.GET.get('courseid')
            # key = "shopping_car_%s_%s" % (USER_ID,courseid)
            key = settings.LUFFY_SHOPPING_CAR % (USER_ID, courseid,)

            CONN.delete(key)
            response.data = '删除成功'
        except Exception as e:
            response.code = 10006
            response.error = '删除失败'
        return Response(response.dict)

    def update(self, request, *args, **kwargs):
        response = BaseResonse()
        try:
            course_id = request.data.get('courseid')
            policy_id = str(request.data.get('policyid')) if request.data.get('policyid') else None

            key = settings.LUFFY_SHOPPING_CAR % (USER_ID, course_id,)

            if not CONN.exists(key):
                response.code = 10007
                response.error = '课程不存在'
                return Response(response.dict)

            price_policy_dict = json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
            if policy_id not in price_policy_dict:
                response.code = 10008
                response.error = '价格策略不存在'
                return Response(response.dict)

            CONN.hset(key, 'default_price_id', policy_id)
            CONN.expire(key, 20 * 60)
            response.data = '修改成功'
        except Exception as e:
            response.code = 10009
            response.error = '修改失败'

        return Response(response.dict)