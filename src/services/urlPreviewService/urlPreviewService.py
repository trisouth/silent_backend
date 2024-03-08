###from linkpreview import Link, LinkPreview, LinkGrabber
###
###
###class UrlPreviewService:
###
###    def __init__(self):
###        pass
###
###    def getUrlPreviewHTML(self, url):
###        grabber = LinkGrabber(
###            initial_timeout=20,
###            maxsize=1048576,
###            receive_timeout=10,
###            chunk_size=1024,
###        )
###        content, url = grabber.get_content(url)
###        link = Link(url, content)
###        preview = LinkPreview(link, parser="lxml")
###        print("title:", preview.title)
###        print("description:", preview.description)
###        print("image:", preview.image)
###        print("force_title:", preview.force_title)
###        print("absolute_image:", preview.absolute_image)
###        print("site_name:", preview.site_name)
###
###        html_template = '''\<!DOCTYPE html>
###          <html lang="en" style="width: 500px; height: 120px; background: transparent;">
###            <head>
###              <meta charset="UTF-8">
###              <meta http-equiv="X-UA-Compatible" content="IE=edge">
###              <meta name="viewport" content="width=500px, height=120px initial-scale=1.0">
###              <title>${Document}</title>
###            </head>
###            <body style="width:500px; height:120px; margin:0; padding:5px; box-sizing:content-box; font-family:sans-serif;">
###              <div style="width:100%; height:100%; display:flex; align-items:center; border:2px solid rgb(223 227 230); border-radius:0.75rem; box-sizing:inherit;">
###                ${imageSource == = "" ? "": '<img src="${imageSource}" style="width:120px; height:120px; border-top-left-radius:0.75rem; border-bottom-left-radius:0.75rem;"/>'}
###                <div style="height: 100%; padding-left:8px; display:flex; flex-direction:column; justify-content:start; box-sizing:inherit;">
###                  <div style="white-space:nowrap; text-overflow:ellipsis; padding:8px; box-sizing:inherit; overflow:hidden; width:260px; font-weight:700; color:white;">${title}</div>
###                  <div style="padding:8px; -webkit-line-clamp:4; -webkit-box-orient:vertical; display:-webkit-box; overflow:hidden; word-break:break-word; max-height:57px; font-weight:400; padding-top:0; font-size:14px; color:white;">${description}</div>
###                </div>
###              </div>
###            </body>
###          </html>'''
###
###        html_template = html_template.replace('${document}', preview.title) \
###            .replace('${imageSource}', preview.absolute_image) \
###            .replace('${title}', preview.title) \
###            .replace('${description}', preview.description)\
###            .replace('\n', '')
###
###        return html_template