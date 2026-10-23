from common import *

body = open(os.path.join(os.path.dirname(__file__), "content", "librarian-vs-leader.html")).read()
content = f'''
<p class="small muted"><a href="blog.html">Writing</a> / Leadership</p>
<article class="article" style="margin:0">
  <h1 class="statement" style="margin-top:12px">Most design system leads are just librarians</h1>
  <p class="sub muted">12 min read. Published 27 February 2026.</p>
  <div class="wcard" style="margin-top:20px;padding:10px"><div class="m"><img src="assets/images/blog/librarian-vs-leader.png" alt="Illustration contrasting a librarian with a leader"></div></div>
  <div class="prose" style="margin-top:28px">{body}</div>
</article>
'''
write("blog-librarian-vs-leader.html", head("Most design system leads are just librarians — Layer One",
      "Why maintaining a library isn't the same as leading a design system.", og="assets/images/blog/librarian-vs-leader.png")
      + shell("writing", [("All writing", "blog.html")], content, card="bar"))
