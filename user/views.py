from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from .forms import UserForm,UserAccountForm
from .models import UserAccount
def reg_form(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form_data = form.save(commit = False)
        new_user = User.objects.create(
            username = form_data.email,
            email = form_data.email,
            first_name = form_data.first_name,
            last_name = form_data.last_name,
            is_active = False,
        )
        new_user.set_password(form_data.password)
        new_user.useraccount = UserAccount()
        new_user.save()
        form = UserForm()
    content = {
        'sign_up_form': form,
    }
    return render(request, 'user/signup.html', content)
