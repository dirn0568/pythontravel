import os

from django.contrib.auth.models import User
from django.shortcuts import render

from chatapp.forms import ChatForm
from chatapp.models import ChatModel


def chatview(request, pk):
    if request.method == "POST":
        chat_text = request.POST.get('chat_text')
        chat_file = request.FILES.getlist('submit_file')
        receive = User.objects.filter(pk=pk)
        for list in receive:
            receive_user = list
        for i in range(len(chat_file)):
            if i != 0:
                chat_text = ''
            file_temp = str(chat_file[i])
            name, ext = os.path.splitext(file_temp)
            model = ChatModel(send_user=request.user,
                                receive_user=receive_user,
                                chat_line=chat_text,
                                chat_img=chat_file[i],
                                chat_img_ext=ext)
            model.save()
    context = {}
    chat_users_list = []
    chat_users_post_list = []
    receive_user = User.objects.filter(pk=pk)
    for list in receive_user:
        chat_users = ChatModel.objects.filter(send_user=request.user, receive_user=list)
        chat_switch_users = ChatModel.objects.filter(send_user=list, receive_user=request.user)
    for i in range(len(chat_users)):
        chat_users_list.append(chat_users[i].pk)
    for j in range(len(chat_switch_users)):
        chat_users_list.append(chat_switch_users[j].pk)
    chat_users_list.sort()
    for i in range(len(chat_users_list)):
        chat_users_post_list.append(ChatModel.objects.filter(pk=chat_users_list[i]))
    context['chat_form'] = ChatForm
    context['chat_pk'] = pk
    context['chat_users'] = chat_users_post_list
    return render(request, 'chat.html', context)