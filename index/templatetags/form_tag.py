from django import template
# from django.http import request
# from django.http import request
from django.shortcuts import render, redirect
from index.forms import SubscribeForm
from django.contrib import messages
from django.http import HttpResponseRedirect


register = template.Library()


@register.inclusion_tag('index/tags/subs_form.html', takes_context=True)
def get_form(context):
    # request = context['request']
    # if request.method == 'POST':
    #     form = SubscribeForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, f'Your are subscribed, we will send you emails!')
    #         # return redirect('index_page')
    #         # return HttpResponseRedirect(request.path_info)
    #         # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # else:
    #     form = SubscribeForm()
    form = SubscribeForm()
    return ({"form": form })


# @register.inclusion_tag('new/userinfo.html', takes_context=True)
# def address(context):
#     request = context['request']
#     address = request.session['address']
#     return {'address':address}