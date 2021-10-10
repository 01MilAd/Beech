from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView
from story.models import Story
from .forms import EditProfileForm
from .models import Profile


@login_required
def profile(request, pk):
    user = get_object_or_404(User, id=pk)
    stories = Story.objects.filter(user=user)
    self_pro = False
    if request.user.id == user.id:
        self_pro = True
    return render(request, 'profile/profile.html', {'user': user, 'stories': stories, 'self_pro': self_pro})


def add_profile(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.filter(user=user)
    if profile.exists():
        return redirect('profile:edit_profile', user.id)
    else:
        return redirect('profile:create_profile', user.id)


def create_profile(request, user_id):
    pass


class CreateProfile(SuccessMessageMixin, CreateView):
    template_name = 'profile/profile_create.html'
    model = Profile
    fields = ('phone', 'avator', 'bio', 'age', 'gender', 'birthday')
    success_message = 'Your profile created successfully'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def form_valid(self, form):
        user = User.objects.get(username=self.request.user)
        form.instance.user = user
        form.instance.id = user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile:profile', kwargs={'pk':self.object.id})


def edit_profile(request, user_id):
    if request.user.id == user_id:
        user = get_object_or_404(User, id=user_id)
        profile = get_object_or_404(Profile, id=user_id)
        if request.method == 'POST':
            form = EditProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                user.email = form.cleaned_data['email']
                user.username = form.cleaned_data['username']
                user.first_name = form.cleaned_data['firstname']
                user.last_name = form.cleaned_data['lastname']
                user.save()
                messages.success(request, 'Your profile edited successfully')
                return redirect('profile:profile', user_id)
        else:
            form = EditProfileForm(instance=profile,
                                   initial={'email': user.email,
                                            'username': user.username,
                                            'firstname': user.first_name,
                                            'lastname': user.last_name, })
        return render(request, 'profile/profile_edit.html', {'form': form})
    else:
        return redirect('login')


class EditProfile(UpdateView):
    pass
