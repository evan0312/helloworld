import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        html = '''
        <html>
        <head>
	    <title>九九乘法表</title>
	    <style>
	    table{
            width:600px;
		    border-collapse:collapse;
		    }
	    table td{
            text-align:center;
		    border:#145b7d 1px solid
		    }
	    </style>
	    </head>
        <body>
        <table>
        '''

        for i in range(1,10):
            html += '<tr>'
            for j in range(1, i+1):
                html += '<td>%d*%d=%d</d>'%(i,j,i*j)
            html += '</tr>'
        
        html += '''
        </table>
        </body>
        </html>
        '''
        self.write(html)

class SecondHandler(tornado.web.RequestHandler):
    def get(self,m):
        m = int(m)
        html = '''
        <html>
        <head>
	    <title>乘法表</title>
	    <style>
	    table{
		    width:600px;
		    border-collapse:collapse;
		    }
	    table td{
	        text-align:center;
		    border:#145b7d 1px solid
		    }
	    </style>
	    </head>
        <body>
        <table>
        '''

        for i in range(1,m+1):
            html += '<tr>'
            for j in range(1, i+1):
                html += '<td>%d*%d=%d</d>'%(i,j,i*j)
            html += '</tr>'
        
        html += '''
        </table>
        </body>
        </html>
        '''
        self.write(html)
        
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/([0-9])", SecondHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
