import web
import sklearn
from joblib import load

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())
render= web.template.render("views")
class Index:
    model= load("../model.joblib")
    def GET(self):
        result=None
        return render.index(result)
    
    def POST(self):
        
        form=web.input()
        x= float(form.x)
        xs=[]
        xs.append([x])
        result=self.model.predict(xs)
        print(x)
        print(result)
        return render.index("La predicción indica que el resultado es "+str(round(result[0])))
        

if __name__ == "__main__":
    app.run()