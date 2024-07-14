---
title: "Kategorie"
layout: page
permalink: /category
---

<ul class="cloud weighted-high" role="navigation">
    {% assign categories_list = site.categories %}
    {% if categories_list.first[0] == null %}
    {% for category in categories_list %}
    <li><a href="{{site.baseurl}}/category/{{ category | url_escape | strip | replace: ' ', '-' }}" data-weight="{{ site.categories[category].size }}">#{{ category | camelcase }}</a></li>
    {% endfor %}
    {% else %}
    {% for category in categories_list %}
    <li><a href="{{site.baseurl}}/category/{{ category[0] | url_escape | strip | replace: ' ', '-' }}"  data-weight="{{ category[1].size }}">#{{ category[0] | camelcase }}</a></li>
    {% endfor %}
    {% endif %}
    {% assign categories_list = nil %}
</ul>
