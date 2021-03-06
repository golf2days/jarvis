import os
from react import jsx
from jarvis import conf

if not os.path.exists(conf.BUILD_PATH):
    os.makedirs(conf.BUILD_PATH)

def build():
    transformer = jsx.JSXTransformer()
    for jsx_path, js_path in conf.JSX_PATHS:
        jsx_path_abs = os.path.join(conf.STATIC_FILES_DIR, jsx_path)
        js_path_abs = os.path.join(conf.STATIC_FILES_DIR, js_path)
        transformer.transform(jsx_path_abs, js_path=js_path_abs, harmony=True)
