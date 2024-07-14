---
title: "Tags"
layout: page
permalink: /tag
---

<ul class="cloud" role="navigation">
    {% assign tags_list = site.tags %}
    {% if tags_list.first[0] == null %}
    {% for tag in tags_list %}
    <li><a href="{{site.baseurl}}/tag/{{ tag | url_escape | strip | replace: ' ', '-' }}" data-weight="{{ site.tags[tag].size }}">#{{ tag | camelcase }}</a></li>
    {% endfor %}
    {% else %}
    {% for tag in tags_list %}
    <li><a href="{{site.baseurl}}/tag/{{ tag[0] | url_escape | strip | replace: ' ', '-' }}"  data-weight="{{ tag[1].size }}">#{{ tag[0] | camelcase }}</a></li>
    {% endfor %}
    {% endif %}
    {% assign tags_list = nil %}
</ul>
