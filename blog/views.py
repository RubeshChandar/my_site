from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView


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


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context
