import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self, m):
        if m == None:
            m = 9;
        else:
            m = int(m);
        num = int(self.get_argument('n',10))
        if 0< num <10:
            m = num
        html = '''
        <html>
        <head>
	    <title>乘法表</title>
	    <style>
	    table{
            width: 600px;
            border-collapse: collapse;
		    }
	    table td{
            text-align: center;
            border: #145b7d 1px solid
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
    (r"/([0-9])?", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
