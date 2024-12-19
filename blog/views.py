from datetime import date
from django.shortcuts import render

# Create your views here.
all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Rubesh",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views You get when hiking in the mountains! \nAnd I wasn't even prepared for what happened while I was enjoying this view!",
        "content": """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente perferendis ducimus repellendus est vel suscipit libero, laudantium tempore alias at nulla natus aperiam consequuntur cupiditate. Nesciunt quidem animi alias consectetur!
    Earum voluptatibus sint nesciunt ad numquam ratione, sequi in eum, repudiandae illum quidem voluptates itaque quas aliquid veniam doloremque! In ducimus, dolorum dolorem harum iure possimus nulla deserunt iste ex.
    Ducimus vel nisi recusandae molestiae voluptatem in inventore veritatis, sed architecto excepturi, aliquam quibusdam quia quis aut earum temporibus distinctio a maxime ipsum odit veniam necessitatibus voluptas iusto. Voluptatibus, illum.
    Vitae odio sint at? Totam earum quisquam dignissimos fugit ut, iure laboriosam soluta recusandae numquam nam, itaque, voluptas voluptatibus molestias maiores maxime enim minus labore blanditiis a perferendis officiis illo?
    Quia ad odit culpa blanditiis officiis reiciendis necessitatibus ducimus fugiat neque voluptas magni iste, ut a, odio temporibus quibusdam maxime, ab eaque vitae iusto. Dignissimos fuga reprehenderit aut expedita tempora!
    """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
