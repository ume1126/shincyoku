from django.shortcuts import render, redirect, reverse, get_object_or_404
# from django.utils import timezone
from .models import Shincyoku, Room
from . import forms
from django.contrib.auth import authenticate

def main(request):
    shincyoku = Shincyoku.objects.all()
    context = {'shincyoku': shincyoku}
    return render(request, 'main/mainpage.html', context)

# ―――――――――――――――――――room処理
def select_room(request):
    rooms = Room.objects.order_by('-id').all()
    context = {'rooms': rooms}
    return render(request, 'main/select_room.html', context)

def create_room(request):
    form = forms.RoomForm()
    if request.method == "POST":
        form = forms.RoomForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('main:main')
    return render(request, 'main/create_room.html', {
        'form':form
    })

# select_roomの参加する！をクリックするとここにくる
def room(request, room_pk):
    room = Room.objects.get(id=room_pk)
    shincyokus = Shincyoku.objects.filter(room=room)
    return render(request, 'main/room.html', {
        'room': room,
        'shincyokus': shincyokus
        })

def countup(request, shincyoku_pk):
    shincyoku = get_object_or_404(Shincyoku, pk=shincyoku_pk)
    if request.method == "POST":
        shincyoku.fight +=1
        shincyoku.save()
    room_id = shincyoku.room.id
    return redirect('main:room', room_pk=room_id)
    #https://tutorial.djangogirls.org/ja/extend_your_application/
    #formのPOSTはredirectを使いましょう　webアプリ開発のベストプライティクス


def delete_room(request, room_pk):
    room = Room.objects.get(id=room_pk)
    print("delete_room", room)
    if request.user.id == room.author.id:
        room.delete()
    # return render(request, 'main/mainpage.html')
    return redirect('main:main')


# ―――――――――――――――――――
def create_shincyoku(request, shincyoku_pk):
    room = Room.objects.get(id=shincyoku_pk)
    form = forms.ShincyokuForm()
    if request.method == "POST":
        form = forms.ShincyokuForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.room = room
            post.save()
        return redirect('main:room', room_pk=shincyoku_pk)
    return render(request, 'main/create_shincyoku.html', {
        'form':form
    })

def shincyoku(request, shincyoku_pk):
    shincyoku = Shincyoku.objects.get(id=shincyoku_pk)
    author = shincyoku.author
    my_shincyoku = Shincyoku.objects.filter(author=author)
    now_shincyoku = my_shincyoku.first()

    if request.method == "POST":
        shincyoku.fight += 1
        shincyoku.save()
        print("GETボタンが押されました : ", shincyoku.fight)

    context = {
        'shincyoku': shincyoku,
        'my_shincyoku': my_shincyoku,
        'now_shincyoku': now_shincyoku,
    }
    return render(request, 'main/my_shincyoku.html', context)


def delete_shincyoku(request, room_pk, shincyoku_pk):
    shincyoku = Shincyoku.objects.get(id=shincyoku_pk)
    room_id = room_pk
    print("shincyoku_pk", shincyoku_pk) #33
    print("room_id", room_id) #3
    print("request.user.id", request.user.id)
    print("shincyoku.author.id", shincyoku.author.id)
    print("shincyoku.room.author.id", shincyoku.room.author.id)

    if request.user.id == shincyoku.author.id or \
       request.user.id == shincyoku.room.author.id:
       shincyoku.delete()
       print("デリートできたよ")
    return redirect('main:room', room_pk=room_id)


def edit_shincyoku(request, shincyoku_pk):
    shincyoku = Shincyoku.objects.get(id=shincyoku_pk)

    if request.user.id == shincyoku.author.id:
        if request.method == 'POST':
            form = forms.ShincyokuForm(request.POST, instance=shincyoku)
            if form.is_valid():
                shincyoku = form.save(commit=False)
                shincyoku.author = request.user
                shincyoku.save()
            return redirect('main:shincyoku', shincyoku_pk=shincyoku.id)
        else:
            form = forms.ShincyokuForm(instance=shincyoku)
            print("elseのform(でもおんなじなんだよな): ", form)
    else:
        print("記事の投稿者じゃないです")
        return redirect('main:shincyoku', shincyoku_pk=shincyoku.id)

    context = {
        'shincyoku': shincyoku,
        'form': form,
    }
    return render(request, 'main/edit_shincyoku.html', context)
