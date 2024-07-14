from xml.dom.minidom import parse, parseString
import markdownify
import codecs

document = parse("wp-content.xml")
items = document.getElementsByTagName('item')
print(items.length)

records = []
for item in items:
    post_type = item.getElementsByTagName('wp:post_type')[0].childNodes[0].data
    if post_type != 'post':
        continue
    post_name = item.getElementsByTagName('wp:post_name')[0].childNodes[0].data
    title = item.getElementsByTagName('title')[0].childNodes[0].data
    date = item.getElementsByTagName('wp:post_date_gmt')[0].childNodes[0].data
    content = item.getElementsByTagName('content:encoded')[0].childNodes[0].data
    categories_el = item.getElementsByTagName('category')
    categories = []
    tags = []
    for category_el in categories_el:
        if category_el.getAttribute('domain') == 'post_tag':
            tags.append(category_el.getAttribute('nicename'))
        if category_el.getAttribute('domain') == 'category':
            categories.append(category_el.getAttribute('nicename'))

    postmetas_el = item.getElementsByTagName('wp:postmeta')
    image = title = item.getElementsByTagName('guid')[0].childNodes[0].data

    record = {
        'title': title, 'post_name': post_name, 'categories': categories, 'tags': tags, 'date': f"{date}"[:10],
        'image': image,
        "content": markdownify.markdownify(content, heading_style="ATX")
    }
    # print(f"{record}")
    records.append(record)
    # break

print(len(records))

for record in records:
    file_name = f"{record['date']}-{record['post_name']}.md"
    file = codecs.open(f"../_posts/{file_name}", "w", "utf-8")
    file.write(f"""---
layout: post
title:  "{record['title']}"
categories: {record['categories']}
tags: {record['tags']}
image: "{record['image']}"
---
{record['content']}
    """)
    file.close()
