from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

"""
  FILE MANAGEMENT
"""

file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.SetContentString('Hello')
file1.Upload() # Files.insert()

file1['title'] = 'HelloWorld.txt'  # Change title of the file
file1.Upload() # Files.patch()

content = file1.GetContentString()  # 'Hello'
file1.SetContentString(content+' World!')  # 'Hello World!'
file1.Upload() # Files.update()

file2 = drive.CreateFile()
file2.SetContentFile('hello.png')
file2.Upload()
print('Created file %s with mimeType %s' % (file2['title'],
file2['mimeType']))
# Created file hello.png with mimeType image/png

file3 = drive.CreateFile({'id': file2['id']})
print('Downloading file %s from Google Drive' % file3['title']) # 'hello.png'
file3.GetContentFile('world.png')  # Save Drive file as a local file

# or download Google Docs files in an export format provided.
# downloading a docs document as an html file:
docsfile.GetContentFile('test.html', mimetype='text/html')

"""
  FILE LISTING PAGINATION
"""

# Auto-iterate through all files that matches this query
file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))

# Paginate file lists by specifying number of max results
for file_list in drive.ListFile({'maxResults': 10}):
  print 'Received %s files from Files.list()' % len(file_list) # <= 10
  for file1 in file_list:
    print('title: %s, id: %s' % (file1['title'], file1['id']))
    
"""
  CONCURRENT ACCESS
"""

# Create httplib.Http() object.
http = drive.auth.Get_Http_Object()

# Create file object to upload.
file_obj = drive.CreateFile()
file_obj['title'] = "file name"

# Upload the file and pass the http object into the call to Upload.
file_obj.Upload(param={"http": http})
