import datetime
last_id = 0

class Note:
    '''
    该类表示笔记本中的一条记录。对于每条记录，可以通过对记录内容或标签进行字符串匹配
    '''
    def __init__(self,memo,tags=''):
        '''
        使用memo对note进行初始化，tag可选，id唯一
        '''    
        global last_id
        last_id = last_id + 1
        self.id = last_id
        self.memo = memo
        self.date = datetime.date.today()
        self.tags = tags

    def match(self,filter):
        return filter in self.memo or filter in self.tags


class NoteBook:
    '''
    该类表示笔记本
    '''

    def __init__(self):
        
        self.notes = []

    def new_note(self,memo,tags=''):
        self.notes.append(Note(memo,tags))
    
    def _find_note(self,id):
        '''
        根据id查找note
        '''
        for note in self.notes:
            if note.id == id:
                return note
        raise ValueError('can not find note whose id is {}'.format(id))

    def modify_memo(self,note_id,memo):
        '''
        使用给定id查找到对应的note，并且改变其memo
        '''
        try:
            note = self._find_note(note_id)
            note.memo =  memo
        except ValueError as ve:
            print(ve)

    def modify_tags(self,note_id,tags):
        '''
        使用给定id查找到对应的note，并且改变其tags
        '''
        try:
            note = self._find_note(note_id)
            note.memo =  tags
        except ValueError as ve:
            print(ve)
   
    def search(self,filter):
       '''
       获取所有tag或memo与filter匹配的note
       '''
       return [note for note in self.notes if note.match(filter)]

