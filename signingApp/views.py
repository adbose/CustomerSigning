from django.shortcuts import render

# Create your views here.
# from django.contrib import messages
# from django.views.generic import TemplateView
#
# from .forms import AddPostForm, AddCommentForm
# from .models import Comment
#
# class AddCommentView(TemplateView):
#
#     post_form_class = AddPostForm
#     comment_form_class = AddCommentForm
#     template_name = 'blog/post.html'
#
#     def post(self, request):
#         post_data = request.POST or None
#         post_form = self.post_form_class(post_data, prefix='post')
#         comment_form = self.comment_form_class(post_data, prefix='comment')
#
#         context = self.get_context_data(post_form=post_form,
#                                         comment_form=comment_form)
#
#         if post_form.is_valid():
#             self.form_save(post_form)
#         if comment_form.is_valid():
#             self.form_save(comment_form)
#
#         return self.render_to_response(context)
#
#     def form_save(self, form):
#         obj = form.save()
#         messages.success(self.request, "{} saved successfully".format(obj))
#         return obj
#
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)

# in forms.py

# https://www.codementor.io/@lakshminp/handling-multiple-forms-on-the-same-page-in-django-fv89t2s3j



@login_required
def account(request):
    name_message = password_message = email_message = ''
    change_name_form = ChangeNameForm(data=request.POST or None, instance=request.user)
    change_password_form = PasswordChangeForm(data=request.POST or None, user = request.user)
    change_email_form = ChangeEmailForm(data=request.POST or None, instance=request.user)
    if request.method == "POST":
        if "change_name" in request.POST and change_name_form.is_valid():
            change_name_form.save()
            name_message = 'Your name has been changed.'
        if "change_password" in request.POST and change_password_form.is_valid():
            change_password_form.save()
            password_message = 'Your password has been changed.'
        if "change_email" in request.POST and change_email_form.is_valid():
            ...
            email_message = 'Please click the link in your email to confirm changes.'
    return render_to_response('userprofile/account.html',
                       {'change_name_form': change_name_form,
                        'change_email_form': change_email_form,
                        'change_password_form': change_password_form,
                        'password_message': password_message,
                        'name_message': name_message,
                        'email_message': email_message,},
                        context_instance=RequestContext(request))