from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from story.forms import StoryForm
from story.models import Story


# def home(request):
#     stories = Story.objects.order_by('-created').filter()[:3]
#     return render(request, 'index.html', {'stories':stories})


class Home(ListView):
    template_name = 'index.html'
    context_object_name = 'stories'
    ordering = '-created'

    def get_queryset(self):
        return Story.objects.filter()[:3]


# @login_required
# def all_story(request):
#     stories = Story.objects.all()
#     return render(request, 'story/story_list.html', {'stories':stories})


class AllStory(LoginRequiredMixin, ListView):
    template_name = 'story/story_list.html'
    context_object_name = 'stories'
    ordering = '-created'

    def get_queryset(self):
        return Story.objects.all()


def create_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            cs = form.save(commit=False)
            cs.user = request.user
            cs.title = form.cleaned_data['title']
            cs.sound = request.FILES['sound']
            cs.cover = request.FILES['cover']
            cs.caption = form.cleaned_data['caption']
            cs.save()
            messages.success(request, 'Your story sent successfully')
            return redirect('story:home')
    form = StoryForm()
    return render(request, 'story/story_create.html', {'form':form})


class CreateStory(CreateView):
    pass


# def edit_story(request, user_id, story_id):
#     if user_id == request.user.id:
#         story = get_object_or_404(Story, id=story_id)
#         if request.method == 'POST':
#             form = StoryForm(request.POST, request.FILES, instance=story)
#             es = form.save(commit=False)
#             es.user = request.user
#             es.save()
#             messages.success(request, 'Your story edited successfully')
#             return redirect('profile:profile', user_id)
#         else:
#             form = StoryForm(instance=story)
#         return render(request, 'story/story_edit.html', {'form':form})
#     return redirect('story:home')


class EditStory(SuccessMessageMixin, UpdateView):
    model = Story
    fields = ('title', 'sound', 'cover', 'caption')
    template_name = 'story/story_edit.html'
    success_message = 'Your story edited successfully'

    def get_success_url(self):
        return reverse('profile:profile', kwargs={'pk':self.request.user.id})


# def delete_story(request, user_id, story_id):
#     if user_id == request.user.id:
#         Story.objects.filter(id=story_id).delete()
#         messages.success(request, 'Your story deleted successfully')
#         return redirect('profile:profile', user_id)
#     else:
#         return redirect('story:home')


class DeleteStory(SuccessMessageMixin, DeleteView):
    model = Story
    template_name = 'story/story_delete.html'
    success_message = 'Your story deleted successfully'

    def get_success_url(self):
        return reverse('profile:profile', kwargs={'pk':self.request.user.id})


