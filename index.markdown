---
layout: product
title: "Catálogo de Productos"
---

# Catálogo de Productos

Bienvenido a nuestro catálogo interactivo de productos Azaleia.

<ul>
  {% for product in site.productos %}
    <li>
 <a href="{{ site.baseurl }}/productos/{{ product.name | slugify }}/">{{ product.name }}</a>
    </li>
  {% endfor %}
</ul>
