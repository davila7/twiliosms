""" Basic restful using webpy 0.3 """
import web
import sms
import model
import json

### Urls

urls = (
    '/api/sms', 'Index',
    '/api/sms/(.+)', 'Show'
)


### Templates
render = web.template.render('templates', base='base')


class Index:

    form = web.form.Form(
        web.form.Textbox('body', web.form.notnull, 
            description="Body:"),
        web.form.Button('Send')
    )

    def GET(self):
        messages = model.get_messages()
        form = self.form()
        return render.index(messages,form)

    def POST(self):
        form = self.form()
        if not form.validates():
            messages = model.get_messages()
            return render.index(messages,form)
        listdata = sms.send(form.d.body)
        model.new_mesagge(listdata)
        return json.dumps({'message': form.d.body})



class Show:

    def GET(self, sid):
        data = model.get_message(sid)
        return json.dumps({'body': data[0].body})

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()