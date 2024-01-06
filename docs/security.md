# Security

## HTML Injection Attacks

Liku is designed to be secure, having the code really simple is part of the effort to make it secure as well.

Every single node that is NOT a liku component will always be escaped using Python's
[`html.escape()`](https://docs.python.org/3/library/html.html#html.escape) function. These includes children
and props/attributes values. **Props key are not escaped.**

For instance, take a look at the following component:

```py
e.div(
    props={"class_": "mx-auto container"},
    children=[
        e.img(props={"src": '"onload="alert(1)"'}),
        e.p(children='<img src="" onerror="alert(99)" />')
    ]
)
```

Liku will generate the following HTML code:

```html
<div class="mx-auto container">
    <img src="&quot;onload=&quot;alert(1)&quot;"></img>
    <p>&lt;img src=&quot;&quot; onerror=&quot;alert(99)&quot; /&gt;</p>
</div>
```

The `safe=True` parameter can be used to mark the children as safe to render, and is not going to be escaped.
**Currently, there is no way to mark props value as safe.**

For instance, for the same component:

```py
e.div(
    props={"class_": "mx-auto container"},
    children=[
        e.img(props={"src": '"onload="alert(1)"'}, safe=True),
        e.p(children='<img src="" onerror="alert(99)" />', safe=True)
    ]
)
```

Liku will generate the following HTML:

```html
<div class="mx-auto container">
    <img src="&quot;onload=&quot;alert(1)&quot;"></img>
    <p><img src="" onerror="alert(99)" /></p>
</div>
```

## Security Tips

- **Only use `safe=True` sparsely.** In general, if you do not need to mark it as safe, keep it as default (False).
- **Avoid giving children to `<script>` and `<style>` tag.** By default, these childrens will also be escaped, so they will not be able
  to execute properly in the first place. Your only option is to consciously set `safe=True`, which is not recommended. You should use
  a separate `.css` or `.js` file to run them.
- **Avoid using `on*` handlers.** They might be fine if you hardcode the value, but setting the value dynamically is a no-go. Despite
  attempts of escaping via `html.escape()`, they could still pass through. For example: `alert(document.cookie)` will still execute correctly,
  since `html.escape()` does not escape the brackets.
