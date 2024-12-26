from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from accounts.models import User

@csrf_exempt
def about_us(request):
    if request.method == 'GET':
        users = User.objects.all()
        names_list = [user.get_full_name() for user in users if user.get_full_name().strip()]
        context = {'users': names_list}
        return render(request=request, template_name='about_us.html', context=context)


