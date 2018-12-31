{% for category in category_list %}
<li><a href="{% url 'blog:category_detail' category.slug %}">{{ category.name }}</a></li>
{% endfor %}