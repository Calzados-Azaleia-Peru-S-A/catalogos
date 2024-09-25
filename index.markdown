---
layout: default
title: "Catálogo de Productos"
---

# Catálogo de Productos

Bienvenido a nuestro catálogo interactivo de productos Azaleia.

<ul>
  {% for product in site.pages %}
    {% if product.layout == "product" %}
      <li>
        <a href="{{ product.url }}">{{ product.name }} - S/. {{ product.price }}</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>
