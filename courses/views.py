from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Course, Lesson
from cloudipsp import Api, Checkout
import time

secret_key = 'test'


def tarifsPage(request):

    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": 1500,
        'order_desc': 'Покупка подписки на сайте',
        'order_id': str(time.time())
    }
    url = checkout.url(data).get('checkout_url')
    return render(request, 'courses/tarifs.html', {'title': 'Тарифы на сайте', 'url': url})

class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']


    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        return ctx


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx

class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lesson-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

        lesson.video = lesson.video.split("=")[1]

        ctx['title'] = lesson
        ctx['lesson'] = lesson
        return ctx

class CreateCourseView(CreateView):
    model = Course
    template_name = 'courses/add_course.html'

    fields = ['slug', 'title', 'desc', 'image']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CreateCourseView, self).get_context_data(**kwargs)
        ctx['title'] = 'Добавление нового курса'
        ctx['slug'] = 'Название URL'
        return ctx
