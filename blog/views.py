from .models import Post
from django.views.generic import ListView
from django.views.generic import View
from .forms import CommentForm
from django.shortcuts import render, redirect

# Create your views here.


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    # You can add an extra entry with comma separation which will then be ordered
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# I have shifted to class based view, though tbh the function based view was better and concise
# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"]


# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts,
#     })


# def post_detail(request, slug):
#     # identified_post = next(post for post in all_posts if post['slug'] == slug)
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all(),
#     })


class SinglePostView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        return render(request, "blog/post-detail.html", {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post-detail-page", slug=slug)

        return render(request, "blog/post-detail.html", {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        })

        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data(**kwargs)
        #     context["post_tags"] = self.object.tags.all()
        #     context["comment_form"] = CommentForm()
        #     return context


class ReadLaterView(View):
    def get(self, request):
        stored_post = request.session.get("stored_posts")
        context = {}

        if stored_post is None or len(stored_post) == 0:
            context["posts"] = []
            context["has_posts"] = False

        else:
            post = Post.objects.filter(id__in=stored_post)
            context["posts"] = post
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        return redirect("/")
