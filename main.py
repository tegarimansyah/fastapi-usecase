from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import importlib

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# ========================================
# File-based Routing With Jinja Templating
# ========================================
templates_dir = "src/file-based-templates"
templates = Jinja2Templates(directory=templates_dir)

def get_context(path, request):
    '''
    This function search for function `get_context` in `{path}/__init__.py`
    The `get_context` will process server-side logic and pass a dict to template
    If not found, then pass empty dict
    '''
    normalized_path = path.rstrip('/').replace("/", ".")
    templates_dir_path = templates_dir.replace("/", ".")
    module_name = f"{templates_dir_path}.{normalized_path}"

    try:
        main_module = importlib.import_module(module_name)
        get_context_function = getattr(main_module, "get_context")
        return get_context_function(request)
    except (ModuleNotFoundError, AttributeError):
        return {}

@app.get("/{path:path}", response_class=HTMLResponse)
async def catch_all(request: Request, path: str):
    '''
    Normally, we will create one function for one path, hardcode the template path 
    and give the context (data). With this method, we only need to define single path 
    and create our template and function in the same path we want. 

    It's inspired by Next.js file-based routing (okay, PHP do that in the very beginning).
    '''
    
    # TODO add fallback if the path does not exist
    template_path = f"{path}/index.html"
    context = get_context(path, request)
    return templates.TemplateResponse(template_path, {"request": request, **context})
