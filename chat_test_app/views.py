from django.shortcuts import render

# Create your views here.

def stateview(request):
    context = {}
    return render(request, 'state.html', context)

def connectview(request):
    pass

def test_room(request, room_name):
    print("테스트 실행중")
    context = {}
    return render(request, 'test_room.html', context)