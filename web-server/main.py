import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4,5,6]

@app.get("/contact/", response_class=HTMLResponse)
async def read_items():
      return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <p>¡Y yo soy un parrafo!</p>
        </body>
    </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()
    