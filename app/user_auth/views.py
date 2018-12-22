from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth


@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    print("user: ", user)
    return render(request,'user_auth/top.html',{'user': user})
