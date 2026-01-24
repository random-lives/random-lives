---
layout: default
title: Blog
permalink: /blog/
---

<div class="blog">
  <h1>Blog</h1>
  <p class="intro">Essays on historical demography, methodology, and the stories behind Random Lives.</p>

  <div class="blog-posts">
    {% for post in site.posts %}
    <article class="blog-preview">
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p class="blog-date">{{ post.date | date: "%B %d, %Y" }}</p>
      <p class="blog-excerpt">{{ post.excerpt | strip_html | truncatewords: 40 }}</p>
      <a href="{{ post.url | relative_url }}" class="read-more">Read more</a>
    </article>
    {% endfor %}
  </div>
</div>
