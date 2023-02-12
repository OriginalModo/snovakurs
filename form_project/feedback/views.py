from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import *
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView


# Create your views here.

class FeedBackViewUpdate(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    # fields = '__all__'
    template_name = 'feedback/feedback.html'
    success_url = '/done'


class FeedBackView(CreateView):
    model = Feedback
    # fields = ['name', 'surname']
    # fields = '__all__'
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

    # def form_valid(self, form):
    #     form.save()
    #     return super(FeedBackView, self).form_valid(form)

# class FeedBackView(FormView):
#     form_class = FeedbackForm
#     template_name = 'feedback/feedback.html'
#     success_url = '/done'
#
#     def form_valid(self, form):
#         form.save()
#         return super(FeedBackView, self).form_valid(form)



    # def post(self, request):
    #     form = FeedbackForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/done')
    #     return render(request, 'feedback/feedback.html', {'form': form})

# class FeedBackView(View):
#
#     def get(self, request):
#
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', {'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', {'form': form})




def index(request):

    if request.method =='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(request,'feedback/feedback.html', context={'form': form})

def update_feedback(request, id_feedback):
    feed = Feedback.objects.get(id=id_feedback)
    if request.method =='POST':
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm(instance=feed)
    return render(request,'feedback/feedback.html', context={'form': form})

class FeedBackUpdateView(View):
    def get(self, request , id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', {'form': form})

    def post(self , request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')


class DoneView(TemplateView):
    template_name =  'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super(DoneView, self).get_context_data(**kwargs)
        context['name'] = 'Cool O.P.'
        context['date'] = '01.01.2022'
        return context

def done(request):
    return render(request,'feedback/done.html')




# class ListFeedBack(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ListFeedBack, self).get_context_data(**kwargs)
#         context['feedbacks'] = Feedback.objects.all()
#         return context


class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks'



    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(rating__lt=10)
        return filter_qs



# class DetailFeedBack(TemplateView):
#     template_name = 'feedback/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(DetailFeedBack, self).get_context_data(**kwargs)
#         context['feedback'] = Feedback.objects.get(id=kwargs['id_feedback'])
#         return context




class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
    # context_object_name = 'feedback'

    # def get_context_data(self, **kwargs):
    #     context = super(DetailFeedBack, self).get_context_data(**kwargs)
    #     context['feedback'] = Feedback.objects.get(id=kwargs['id_feedback'])
    #     return context


