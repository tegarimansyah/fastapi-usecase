# FastAPI Use Case

A collection of [FastAPI](https://fastapi.tiangolo.com/) use cases. Work in progress.

## How to use

1. Clone this repo
2. Install deps with `poetry install`
3. Run `poetry run uvicorn main:app --reload`

## Use Case

1. **File-based Routing With Jinja Templating**

Normally, we will create one function for one path, hardcode the template path and give the context (data). With file-based routing, we only need to define a single path that catches all, then create our template and function in the directory with the same name with path. 

See [main.py](./main.py) and search for `catch_all` functions. It will search for `index.html` in the same path as request and if `get_context` function exists in `__init__.py` then it will be pass the context to the template. You can see the hierarchy here in [src/file-based-templates](./src/file-based-templates/index.html).

For Example:

```
example.com ==> /index.html
example.com/about ==> /about/index.html
example.com/nested/path/should/works ==> /nested/path/should/works/index.html

It will also looking for __init__.py for context
```

> **Note 1:** It's inspired by Next.js file-based routing (okay, PHP do that in the very beginning).

> **Note 2:** I also try to use [HTMX](https://htmx.org/) with [hx-boost](https://htmx.org/attributes/hx-boost/). So if I click a navigation link, it will not reload the whole page but only replace the element that changed. Just like modern JS framework

2. Hot reload the HTML in browser

TBA. Great candidate: https://github.com/florimondmanca/arel. The example of usage https://gist.github.com/vrslev/6d0602bfa939a01844f645c608afb85a

Using `uvicorn main:app --reload --reload-include *.html` will reload the uvicorn but not the browser


---

Have any other ideas for use case? [Request in the issues section](https://github.com/tegarimansyah/fastapi-usecase/issues/new).