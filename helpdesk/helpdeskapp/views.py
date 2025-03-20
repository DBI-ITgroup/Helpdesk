# helpdeskapp/views.py

from django.shortcuts import render, redirect


def home(request):
    return render(request, 'base.html')
#def register(request):
 #   if request.method == 'POST':
  #      form = UserRegistrationForm(request.POST)
  #      if form.is_valid():
   #         # Save the new user with the form data
   #         form.save()  # Save the new CustomUser
    #        return redirect('login')  # Redirect to login after registration
    #else:
    #    form = UserRegistrationForm()

    #return render(request, 'register.html', {'form': form})
