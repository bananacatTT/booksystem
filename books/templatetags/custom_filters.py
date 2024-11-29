from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """
    フォームフィールドにCSSクラスを追加するカスタムフィルタ
    """
    return field.as_widget(attrs={"class": css_class})
