from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required
from itertools import chain
# Create your views here.


def index(request):
    user_follow = request.user.follow.all()
    follow_list = chain(user_follow, [request.user])
    posts = Post.objects.order_by('-id').filter(user__in=follow_list)
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'posts/index.html', context)


def all(request):
    posts = Post.objects.all().order_by('-id')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'posts/index.html', context)


def create(request):
    # 1. get 방식으로 데이터를 입력할 수 있는 form을 요청한다.
    # 4. 사용자가 데이터를 입력해서 post요청을 보낸다.
    # 9. 사용자가 적절한 데이터를 입력해서 post 요청을 보낸다.
    if request.method == "POST":
        # 5. post방식으로 저장요청을 받고, 데이터를 받아서 PostForm을 인스턴스화 한다.
        # 10. 데이터를 받아서 PostForm을 인스턴스화 한다.
        form = PostForm(request.POST, request.FILES)
        # 6. 데이터 검증을 한다.
        # 11. 데이터 검증을 한다
        if form.is_valid():
            # 12. 적절한 데이터가 들어온다. 저장을 하고 인덱스로 보낸다.
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("posts:index")
        else:
            # 7. 적절하지 않은 데이터가 들어온다.
            pass
    else:
        # 2.PostForm을 인스턴스화 해서 form 변수에 저장
        form = PostForm()
    context = {
        'form': form,
    }
    # 3. 만들어진 form을 create.html에 담아서 전송
    # 8. 사용자가 정확하게 입력한 데이터를 유지한 상태의 form을 전송
    return render(request, 'posts/form.html', context)


@login_required
def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user == post.user:
        # 내가 작성한 글일때
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)  # data = request.POST(기존데이터), instance (덮어씌울 데이터)
            if form.is_valid():
                form.save()
                return redirect("posts:index")
            else:
                pass
        else:
            form = PostForm(instance=post)
        return render(request, 'posts/form.html', {'form': form})
    else:
        # 내가 작성하지 않은 글일때
        return redirect("posts:index")


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("posts:index")


@login_required
def comment_create(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('posts:index')


@login_required()
def likes(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    # 이미 좋아요가 눌러졌으면 좋아요 취소
    if user in post.like_users.all():
        post.like_users.remove(user)
    # 좋아요 안했으면 좋아요 추가
    else:
        post.like_users.add(user)
    return redirect('posts:index')
