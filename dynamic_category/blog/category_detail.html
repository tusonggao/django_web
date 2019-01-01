{% if category.parent_category %}
<p>父类别: </p>
<li><a href="{% url 'blog:category_detail' category.parent_category.slug %}">{{ category.parent_category.name }}</a></li>
{% endif %}

<p>当前类别: </p>
<li><a href="{% url 'blog:category_detail' category.slug %}">{{ category }}</a></li>

{% with category.category_set.all as categories %}
{% if categories %}
<p>子类别: </p>
{% for category in categories %}
<li> <a href="{% url 'blog:category_detail' category.slug %}">{{ category.name }}</a></li>
{% endfor %}
{% endif %}
{% endwith %}

{% with category.get_same_level_category as categories %}
{% if categories %}
<p>当前同级类别: </p>
{% for category in categories %}
<li><a href="{% url 'blog:category_detail' category.slug %}">{{ category }}</a></li>
{% endfor %}
{% endif %}
{% endwith %}