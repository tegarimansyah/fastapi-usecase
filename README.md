# FastAPI Use Case

A collection of [FastAPI](https://fastapi.tiangolo.com/) use cases. Work in progress.

## How to use

1. Clone this repo
2. Install deps with `poetry install`
3. Run `poetry run uvicorn main:app --reload`

## Use Case

1. File-based Routing With Jinja Templating

 Normally, we will create one function for one path, hardcode the template path and give the context (data). With this method, we only need to define single path and create our template and function in the same path we want. 

See [main.py](./main.py) and search for `catch_all` functions. It will search for `index.html` in the same path as request and if `get_context` function exists in `__init__.py` then it will be pass the context to the template. You can see the hierarchy here in [src/file-based-templates](./src/file-based-templates/index.html) 

It's inspired by Next.js file-based routing (okay, PHP do that in the very beginning).

2. FastAPI with HTMX

TBA

---

Have any other ideas for use case? [Request in the issues section](https://github.com/tegarimansyah/fastapi-usecase/issues/new).