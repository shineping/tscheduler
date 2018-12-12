from aiohttp import web,log
import zerorpc
client = zerorpc.Client()
client.connect('tcp://127.0.0.1:9000')

async def hanlde(request:web.Request):
    txt = '<h1>hello world</h1>'
    return web.Response(text=txt,status=200,content_type='text/html')


async def targethanlder(request:web.Request):
	txt = client.get_agents()
	return web.json_response(txt)

async def taskhanlder(request:web.Request):
    j = await request.json()
    task = client.add_task(j)
    task_id = '-'.join(task)
    print(task_id)
    return web.Response(text=task_id, status=201)

async def get_result(request:web.Request):
    path_info = request.path_qs
    _,task_id = path_info.split('=')
    return web.json_response(client.get_result(task_id))

app = web.Application()
app.add_routes([web.get('/',hanlde),web.get('/agents',targethanlder),web.post('/task',taskhanlder),web.get('/task',get_result)])

web.run_app(host='127.0.0.1',port=9900,app=app)