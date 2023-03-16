# import json
# from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
# from functools import wraps
# from accounts.models import VolunteerExtraDetails, VerifyMobileOtp
# from masters.models import MemberType
# from django.contrib.auth import logout


# def check_user_info(function):
#     def wrap(request, *args, **kwargs):
#         type = VolunteerExtraDetails.objects.filter(user_id=request.user.id).values('member_type')
#         if type:
#             if type[0]['member_type']:
#                 type = MemberType.objects.filter(id=type[0]['member_type']).values('member_type')
#                 type = type[0]['member_type']
#                 paid = VolunteerExtraDetails.objects.get(user_id=request.user.id)

#                 if request.user.role.get().name == "Volunteer" and (type == "Primary Member" or type == "Active Member") and paid.is_paid is False:
#                     if request.is_ajax():
#                         pass
#                     else:
#                         return HttpResponseRedirect('/accounts/membership_fee/')
#                 # elif request.user.role.get().name == "Volunteer" and type == "Active Member" \
#                 #         and (paid.is_paid is False or paid.membership_status == 'Pending' or paid.membership_status == 'Rejected'):
#                 #     if request.is_ajax():
#                 #         pass
#                 #     else:
#                 #         return HttpResponseRedirect('/accounts/membership_fee/')
#             else:
#                 return function(request, *args, **kwargs)

#         if request.user.is_authenticated and "Admin" not in request.user.role.all().values_list("name", flat=True):
#             if "Volunteer" in request.user.role.all().values_list("name", flat=True):
#                 if request.user.is_active:
#                     return function(request, *args, **kwargs)
#                 else:
#                     # response = HttpResponseRedirect('/')
#                     # response.set_cookie(key="popup_check", value="True")
#                     # response.set_cookie(key="number", value=request.user.mobile_number)
#                     return HttpResponseRedirect('/')
#                     # return response
#             elif "Donor" in request.user.role.all().values_list("name", flat=True):
#                 if request.user.is_active:
#                     return function(request, *args, **kwargs)
#                 else:
#                     return HttpResponseRedirect('/accounts/user_info/')
#         else:
#             return function(request, *args, **kwargs)
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap

# from django.utils import translation

# def admin_login_required(view_func):
#     def wrap(request, *args, **kwargs):

#         translation.activate('en')
#         if not request.user.is_authenticated:
#             return HttpResponseRedirect("/admin_login/")
#         elif not request.user.is_superuser and not request.user.is_staff:
#             return HttpResponse('<h1>You do not have permission to perform this action.</h1>')
#         else:
#             if VerifyMobileOtp.objects.filter(mobile_number=request.user.mobile_number).exists():
#                 # Admin Login but OTP Verification NOT done
#                 logout(request)
#                 request.session.flush()
#                 return HttpResponseRedirect("/admin")
#             return view_func(request, *args, **kwargs)

#     wrap.__doc__ = view_func.__doc__
#     wrap.__name__ = view_func.__name__
#     return wrap

# def user_login_required(view_func):
#     def wrap(request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return HttpResponseRedirect("/accounts/login/")
#         else:
#             return view_func(request, *args, **kwargs)

#     wrap.__doc__ = view_func.__doc__
#     wrap.__name__ = view_func.__name__
#     return wrap