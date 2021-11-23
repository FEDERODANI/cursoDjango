from django import template

register = template.Library()

@register.simple_tag
def saludar():
	return "Hola a todos, soy un tag personalizado"

@register.simple_tag
def saludar_con_nombre(nombre):
	return f"Hola {nombre}!"

def ejemplo(value, arg):
	if len(value) > 0:
		return value
	return arg
register.filter("ejemplo", ejemplo)